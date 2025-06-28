# RAG-Assistant

RAG-Assistant is a minimal and extensible implementation of a Retrieval-Augmented Generation (RAG) system for question answering. It leverages vector databases and large language models (LLMs) to retrieve relevant information from indexed documents and generate concise, context-aware answers to user queries.

## Features

- **Retrieval-Augmented Generation (RAG):** Combines information retrieval from a vector database with generative capabilities of LLMs for precise answers.
- **FastAPI Backend:** Provides a RESTful API for pushing, indexing, searching, and answering questions over project-specific document sets.
- **Multi-language Support:** Includes prompt templates for both English and Arabic, supporting multi-lingual queries and responses.
- **Flexible Vector Database Integration:** Index and search your own documents using embeddings and vector search.
- **LLM Agnostic:** Easily pluggable with different LLM providers (OpenAI, Cohere, Gemini) for text generation.
- **Dockerized Deployment:** Ready-to-use Docker Compose setup for easy local or cloud deployment.
- **Environment Configurable:** All keys and settings managed via `.env` files for secure configuration.

## Requirements

- Python 3.10 or later
- Docker (optional, for containerized deployment and mongodb usage)
- API key for your LLM provider (e.g., OpenAI)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Environment Variables

Copy the environment template and update credentials:
```bash
cp .env.example .env
# Edit .env to set your LLM/api keys and database settings
```

### 3. Run with Docker Compose (Optional if you already have mongodb)

```bash
cd docker
cp .env.example .env
# Edit docker/.env with your settings
sudo docker compose up -d
```

### 4. Run FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## API Overview

- `GET /api/v1/`: base API
- `POST /api/v1/data/upload/{project_id}`: upload documents with unique name in a project
- `POST /api/v1/data/process/{project_id}`: split the uploaded documents into small chunks
- `POST /api/v1/nlp/index/push/{project_id}`: Index documents for a specific project.
- `GET /api/v1/nlp/index/info/{project_id}`: Get info about the indexed collection.
- `POST /api/v1/nlp/index/search/{project_id}`: Search for relevant chunks in the vector DB.
- `POST /api/v1/nlp/index/answer/{project_id}`: Get an answer to a question using RAG.


## How to use



### **upload documents (text/pdf)**
- use this API (`/api/v1/data/upload/{project_id}`) to store the documents in this path "`/src/assets/files/(project_id value (ex. 1,2))/(document unique name)`".
- you can put all relative documents in one project.
##### **example**
![](/images/upload.png)






### **split text content**
- use this API (`/api/v1/data/process/{project_id}`) to split the documents and store the chunks in mongodb
- parameters:
    1. **file_id:** if you want process specific document if you do not fill it will process all documents in the project_id
    2. **chunk_size:** number of character in each chunk
    3. **overlap_size:** number of overlapped characters in every two adjacent chunks
    4. **do_reset:** remove all chunks for this project in mongodb
##### **example**
![](/images/process.png)




### **Indexing Documents:**

- Push and index your document chunks into a vector database(Qdrant) using the API (`/api/v1/nlp/index/push/{project_id}`).

- parameters:
    1. **do_reset:** if you want remove all current data from qdrantDB
##### **example**
![](/images/index.png)


### **Get Info:**
- use this API (`/api/v1/nlp/index/info/{project_id}`) to get info about all chunks in a project



### **Searching & Retrieval:**
- use this API (`/api/v1/nlp/index/search/{project_id}`) to search about relative chunks in QdrantDB
- parameters:
    1. **text:** user query
    2. **limit:** number of related chunks you want in response
##### **example**
![](/images/Search.png)

### **Answer Generation:**
- An LLM generates an answer based on the prompt, optionally maintaining chat history for context.
- use this API (`/api/v1/nlp/index/answer/{project_id}`) to chat with the LLM.
    1. **text:** user query
    2. **limit:** number of related chunks you want to give to the LLM
![](/images/answer.png)

## Customization

- **Prompt Templates:** Located under `src/stores/llm/template/locales/` (English & Arabic).
- **LLM Providers:** Easily extend or swap the LLM provider(Gemini, OpenAI, CoHere) in `src/stores/llm/providers/`.
- **Vector DB:** Swap or extend the vector database backend as needed.

## License

[Apache License 2.0](LICENSE)

## contact with me
[LinkedIn profile](https://www.linkedin.com/in/ahmed-ayman-25a9b2248/)
[Gmail](ai388981@gmail.com)
