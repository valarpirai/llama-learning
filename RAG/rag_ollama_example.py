from langchain.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.docstore.document import Document
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

# Sample documents
docs = [
    Document(page_content="Python is a versatile programming language used for web development and AI."),
    Document(page_content="JavaScript is primarily used for interactive web applications."),
    Document(page_content="AI models like LLMs can generate human-like text.")
]

# Initialize embedding model with nomic-embed-text
embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://localhost:11434")

# Create vector store
vector_store = Chroma.from_documents(docs, embeddings)

# Initialize Ollama with Qwen3 model
llm = OllamaLLM(model="qwen3:4b", base_url="http://localhost:11434")

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True  # Optional: to see retrieved docs
)

# Query the RAG system
query = "What is Python used for?"
result = qa_chain({"query": query})

# Print result
print(f"Query: {query}")
print(f"Answer: {result['result']}")
print(f"Source Documents: {[doc.page_content for doc in result['source_documents']]}")