from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime
import rclpy
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from ament_index_python.packages import get_package_share_directory
import re
import os

class LlmNode(Node):
    def __init__(self, base_url, model_name, data_file_path):
        super().__init__("llm_node")

        # Definindo o caminho para o log
        self.log_file_path = "logs_llm.txt" 
        
        # Carrega o documento e o processa para usar como contexto
        loader = TextLoader(data_file_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = Chroma.from_documents(docs, embedding_function)
        retriever = vectorstore.as_retriever()

        template = """
                    You will receive context from a text file containing details about various tools. Your task is to respond to user queries using this context when relevant. Here's how to proceed:

                    Context Use: Utilize the provided context only for queries directly related to the tools listed in the text file. The context includes tool names and coordinates in portuguese.

                    Responding to Queries: Keep the response concise and focused solely on answering the user query. Do not add any additional information or dialogue.
                    For queries asking about a specific tool, like its location, always return the information in the following format: [(x: [coordinate x]), (y: [coordinate y])]. After this, always end the conversation.

                    Context from File:
                    {context}

                    ---

                    User Query: {question}
                    """
        prompt = ChatPromptTemplate.from_template(template)
        self.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | ChatOpenAI(model="gpt-3.5-turbo", api_key='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')
        )

        # Configuração do ROS
        self.subscription = self.create_subscription(
            String, "llm_command", self.listener_callback, 10
        )
        self.publisher_ = self.create_publisher(String, "llm_response", 10)
        self.get_logger().info("LLM Node está rodando e esperando por comandos...")

    def run_model(self, text):
        try:
            model_response = ""
            # pattern = re.compile(r"\(x: (\d+)\), \(y: (\d+)\)")  
            # pattern2 = re.compile(r"\[\(x: \d+\), \(y: \d+\)\]")
            # end_marker = "<|im_end|>"

            for s in self.chain.stream(text):
                model_response += s.content
            #     self.get_logger().info(s)

            #     if pattern.search(model_response) or pattern2.search(model_response) or end_marker in model_response:
            #         break

            return model_response
        except Exception as exp:
            self.get_logger().info(exp)
            return "Erro ao processar a resposta."

    def listener_callback(self, msg):
        self.get_logger().info(f'LLM recebeu: "{msg.data}"')
        
        # Pegando o tempo e input no LLM 
        time_input = datetime.now()

        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f'User input: {msg.data}\n {time_input}')

        response = self.run_model(msg.data)
        self.get_logger().info(f'LLM retornou: "{response}"')
        
        # Pegando o tempo e resposta do LLM

        time_output = datetime.now()
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f'LLM output: {response}\n {time_output}')

        self.publisher_.publish(String(data=response))

def main(args=None):
    # Nome do seu pacote
    package_name = 'central'

    # Construa o caminho para o diretório de compartilhamento do pacote
    package_share_directory = get_package_share_directory(package_name)

    # Construa o caminho para o seu arquivo de dados dentro do diretório de recursos
    data_file_path = os.path.join(package_share_directory, 'resource', 'data.txt')

    rclpy.init(args=args)
    llm_node = LlmNode(
        base_url="http://localhost:11434",
        model_name="dolphin2.2-mistral",
        data_file_path=data_file_path
    )
    try:
        rclpy.spin(llm_node)
    except KeyboardInterrupt:
        pass
    finally:
        llm_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
