```
uv init
uv venv
```
Activate the env

## Install dependecies
`uv pip install chromadb streamlit ollama streamlit_chat markitdown langchain_text_splitters`

`uv pip install langchain langchain_community langchain_ollama chromadb neo4j`


`chroma run --path chroma_data`


## Run app
`streamlit run app.py`

## In browser
Goto - http://localhost:8501/




`docker run -d --rm -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j`