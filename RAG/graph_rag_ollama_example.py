from neo4j import GraphDatabase
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphQAChain

# Neo4j connection (replace with your credentials)
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# Initialize Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Create sample knowledge graph
def create_sample_graph(tx):
    tx.run("""
        MERGE (python:Language {name: 'Python'})
        MERGE (javascript:Language {name: 'JavaScript'})
        MERGE (web:Domain {name: 'Web Development'})
        MERGE (ai:Domain {name: 'AI'})
        MERGE (python)-[:USED_FOR]->(web)
        MERGE (python)-[:USED_FOR]->(ai)
        MERGE (javascript)-[:USED_FOR]->(web)
    """)

# Populate graph
with driver.session() as session:
    session.write_transaction(create_sample_graph)

# Initialize Neo4j graph for LangChain
graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USER, password=NEO4J_PASSWORD)

# Initialize Ollama with Qwen3 model
llm = OllamaLLM(model="qwen3", base_url="http://localhost:11434")

# Initialize embeddings (optional for hybrid retrieval, not always used in GraphQAChain)
embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://localhost:11434")

# Create GraphQA chain
qa_chain = GraphQAChain.from_llm(llm=llm, graph=graph, verbose=True)

# Query the Graph RAG system
query = "What domains is Python used for?"
result = qa_chain.run(query)

# Print result
print(f"Query: {query}")
print(f"Answer: {result}")

# Close driver
driver.close()
