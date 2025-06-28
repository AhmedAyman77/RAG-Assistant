# RAG-Assistant

RAG-Assistant is a minimal and extensible implementation of a Retrieval-Augmented Generation (RAG) system for question answering. It utilizes vector databases and large language models (LLMs) to retrieve relevant information from indexed documents and generate concise, context-aware responses to user queries.

## Features

- **Retrieval-Augmented Generation (RAG):** Seamlessly integrates information retrieval via a vector database with generative capabilities of LLMs for accurate answers.
- **FastAPI Backend:** Offers a RESTful API for uploading, indexing, searching, and answering queries using project-specific document sets.
- **Multi-language Support:** Includes prompt templates in both English and Arabic, enabling multi-lingual queries and responses.
- **Flexible Vector Database Integration:** Index and search custom documents using embeddings and vector search capabilities.
- **LLM Agnostic:** Easily configurable with multiple LLM providers (OpenAI, Cohere, Gemini) for text generation.
- **Dockerized Deployment:** Ready-to-use Docker Compose setup for effortless deployment locally or in the cloud.
- **Configurable Environment:** Manage all keys and settings securely using `.env` files.

## Requirements

- Python 3.10 or higher
- Docker (optional, required for containerized deployment and MongoDB usage)
- API key for your chosen LLM provider (e.g., OpenAI)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the environment template and update credentials:
```bash
cp .env.example .env
# Edit .env to provide your LLM/API keys and database settings
```

### 3. Launch with Docker Compose (Optional, if MongoDB is not already available)

```bash
cd docker
cp .env.example .env
# Edit docker/.env with your configuration
sudo docker compose up -d
```

### 4. Start the FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## API Overview

- `GET /api/v1/`: Base API endpoint.
- `POST /api/v1/data/upload/{project_id}`: Upload documents with a unique name within a project.
- `POST /api/v1/data/process/{project_id}`: Split uploaded documents into smaller chunks.
- `POST /api/v1/nlp/index/push/{project_id}`: Index documents for a specific project.
- `GET /api/v1/nlp/index/info/{project_id}`: Retrieve information about the indexed collection.
- `POST /api/v1/nlp/index/search/{project_id}`: Search for relevant chunks in the vector database.
- `POST /api/v1/nlp/index/answer/{project_id}`: Obtain an answer to a question using the RAG pipeline.

## Usage Guide

### **Uploading Documents (Text/PDF)**
- Use the `/api/v1/data/upload/{project_id}` endpoint to store documents in the path: `/src/assets/files/(project_id)/(document_unique_name)`.
- All relevant documents can be grouped under a single project.
#### **Example**    
![](/images/UPLOAD.png)

### **Splitting Document Content**
- Use the `/api/v1/data/process/{project_id}` endpoint to split documents and store the resulting chunks in MongoDB.
- Parameters:
    1. **file_id:** Specify to process a particular document, or leave blank to process all documents in the project.
    2. **chunk_size:** Number of characters in each chunk.
    3. **overlap_size:** Number of overlapping characters between consecutive chunks.
    4. **do_reset:** Remove all existing chunks for this project in MongoDB.
#### **Example**    
![](/images/PROCESS.png)

### **Indexing Documents**
- Index your document chunks into the vector database (Qdrant) using the `/api/v1/nlp/index/push/{project_id}` endpoint.
- Parameters:
    1. **do_reset:** If true, removes all current data from QdrantDB before indexing.
#### **Example**    
![](/images/PUSH.png)

### **Retrieving Index Information**
- Use `/api/v1/nlp/index/info/{project_id}` to obtain details about all chunks in a project.
#### **Example**    
![](/images/INFO.png)

### **Searching & Retrieval**
- Use `/api/v1/nlp/index/search/{project_id}` to search for relevant chunks in QdrantDB.
- Parameters:
    1. **text:** User query.
    2. **limit:** Number of related chunks to return in the response.
#### **Example**    
![](/images/SEARCH.png)

### **Answer Generation**
- The LLM generates answers based on the constructed prompt, optionally preserving chat history for context.
- Use `/api/v1/nlp/index/answer/{project_id}` to interact with the LLM.
    1. **text:** User query.
    2. **limit:** Number of relevant chunks to provide to the LLM.
#### **Example**    
![](/images/ANSWER.png)

## Customization

- **Prompt Templates:** Located in `src/stores/llm/template/locales/` (English & Arabic).
- **LLM Providers:** Easily extend or switch LLM providers (Gemini, OpenAI, Cohere) in `src/stores/llm/providers/`.
- **Vector Database:** Swap or extend the vector database backend as needed.

## License

[Apache License 2.0](LICENSE)

## Contact

- [LinkedIn Profile](https://www.linkedin.com/in/ahmed-ayman-25a9b2248/)
- [Gmail](mailto:ai388981@gmail.com)