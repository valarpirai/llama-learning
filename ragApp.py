from markitdown import MarkItDown
from langchain_text_splitters import RecursiveCharacterTextSplitter

import ollama
import chromadb

class ChatPDF:

	def __init__(self, llm_model: str = "qwen2.5"):
		self.md = MarkItDown()
		self.text_splitter = RecursiveCharacterTextSplitter(
			chunk_size=1024, chunk_overlap=100, length_function=len
		)
		self.vector_store = chromadb.HttpClient(host='localhost', port=8000)
		try:
			self.vector_store.get_or_create_collection(name="docs")
		except Exception:
			print("Vector collection already exists")

		self.collection = None

	def ask(self, query: str):
		if not self.vector_store:
			self.vector_store = chromadb.HttpClient(host='localhost', port=8000)

		try:
			self.collection = self.vector_store.get_or_create_collection(name="docs")
		except Exception:
			print("Vector collection already exists")

		response = ollama.embeddings(
			prompt=query,
			model="mxbai-embed-large"
		)

		results = self.collection.query(
			query_embeddings=[response["embedding"]],
			n_results=1
		)

		if len(results['documents'][0]) > 0:
			data = results['documents'][0][0]
		else:
			data = ""

		output = ollama.generate(
			model="llama3.2",
			prompt=f"Using this data: {data}. Respond to this prompt: {query}"
		)

		return output['response']

	def ingest(self, pdf_file_path: str):
		result = self.md.convert(pdf_file_path)
		chunks = self.text_splitter.split_text(result.text_content)
		
		try:
			self.collection = self.vector_store.get_or_create_collection(name="docs")
		except Exception:
			print("Vector collection already exists")

		for i, d in enumerate(chunks):
			response = ollama.embeddings(model="mxbai-embed-large", prompt=d)
			embedding = response["embedding"]
			self.collection.add(
				ids=[str(i)],
				embeddings=[embedding],
				documents=[d]
			)


	def clear(self):
		self.collection = None
		try:
			self.vector_store.delete_collection(name="docs")
		except Exception:
			print("Vector collection already deleted")
