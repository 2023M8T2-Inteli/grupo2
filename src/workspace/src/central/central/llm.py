from rclpy.node import Node
from std_msgs.msg import String
import rclpy
from langchain.llms import Ollama
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
            | Ollama(base_url=base_url, model=model_name)
        )

        # Configuração do ROS
        self.subscription = self.create_subscription(
            String, "llm_command", self.listener_callback, 10
        )
        self.publisher_ = self.create_publisher(String, "llm_response", 10)
        self.get_logger().info("LLM Node está rodando e esperando por comandos...")

    def run_ollama(self, text):
        try:
            ollama_response = ""
            pattern = re.compile(r"\(x: (\d+)\), \(y: (\d+)\)")  
            pattern2 = re.compile(r"\[\(x: \d+\), \(y: \d+\)\]")
            end_marker = "<|im_end|>"

            for s in self.chain.stream(text):
                ollama_response += s
                self.get_logger().info(s)

                if pattern.search(ollama_response) or pattern2.search(ollama_response) or end_marker in ollama_response:
                    break

            return ollama_response
        except Exception as exp:
            self.get_logger().info(exp)
            return "Erro ao processar a resposta."

    def listener_callback(self, msg):
        self.get_logger().info(f'LLM recebeu: "{msg.data}"')
        response = self.run_ollama(msg.data)
        self.get_logger().info(f'LLM retornou: "{response}"')

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
