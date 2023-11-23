from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Load the PDF document and split it to use as context
pdf_loader = PyPDFLoader("inventario_simulado_amoxarifado.pdf")  # Replace "your_document.pdf" with your PDF file path
documents = pdf_loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="dexter")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

user_input = input("Por favor, faça uma pergunta em inglês e escreva o nome do item que deseja buscar em português: ")

for s in chain.stream(user_input):
    print(s, end="", flush=True)
