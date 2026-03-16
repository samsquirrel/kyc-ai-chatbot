# AI KYC Verification Chatbot

## Project Overview

This project is an **AI-powered KYC (Know Your Customer) Verification Chatbot** built using modern AI tools and frameworks.
The system allows users to interact with a chatbot interface to ask questions about KYC regulations, upload identity documents, and verify information using OCR and AI agents.

The chatbot integrates **Large Language Models, Retrieval-Augmented Generation (RAG), vector databases, and multiple AI agents** to provide intelligent responses.

This project demonstrates how modern AI systems can assist with **identity verification, compliance guidance, and document processing**.

---

# System Architecture

User
↓
Streamlit Chat Interface
↓
Router Agent
↓
-

| Search Agent (Internet)      |
| RAG Agent (Knowledge Base)   |
| OCR Agent (Document Scan)    |
| Verification Agent           |
--------------------------------

↓
Gemini LLM
↓
Vector Database (FAISS)
↓
LangSmith Monitoring

---

# Key Features

| Feature              | Description                                |
| -------------------- | ------------------------------------------ |
| Chatbot UI           | Interactive chat interface using Streamlit |
| Gemini LLM           | Uses Google Gemini model for AI responses  |
| RAG Pipeline         | Retrieves information from KYC documents   |
| Vector Database      | Uses FAISS for semantic search             |
| OCR Support          | Extracts text from uploaded documents      |
| Internet Search      | Retrieves real-time information            |
| Multi-Agent System   | Multiple AI agents with different tasks    |
| LangSmith Monitoring | Traces agent execution and workflows       |

---

# Technologies Used

| Component       | Technology            |
| --------------- | --------------------- |
| LLM             | Gemini API            |
| Framework       | LangChain             |
| Agent Workflow  | LangGraph             |
| Vector Database | FAISS                 |
| Embeddings      | Sentence Transformers |
| OCR             | Tesseract OCR         |
| Frontend        | Streamlit             |
| Monitoring      | LangSmith             |

---

# Project Structure

```
kyc-ai-chatbot/

│
├── app.py
├── requirements.txt
├── README.md
│
├── agents
│   ├── router_agent.py
│   ├── search_agent.py
│   ├── rag_agent.py
│   ├── ocr_agent.py
│   └── verification_agent.py
│
├── database
│   └── vector_store.py
│
├── utils
│   ├── llm.py
│   └── embeddings.py
│
├── documents
│   └── kyc_rules.pdf
│
└── .streamlit
    └── config.toml
```

---

# Installation Guide

## Step 1 — Clone Repository

```
git clone https://github.com/yourusername/kyc-ai-chatbot.git

cd kyc-ai-chatbot
```

---

## Step 2 — Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

---

## Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

---

## Step 4 — Add API Keys

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_gemini_api_key

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=kyc-chatbot
```

---

# Run the Chatbot

Start the Streamlit server:

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# How the System Works

## 1. Router Agent

The router agent analyzes the user's query and decides which agent should handle the request.

Example:

User Question → Router → Appropriate Agent

---

## 2. Search Agent

The search agent retrieves information from the internet using a search tool.

Used for:

* KYC regulations
* compliance updates
* general information

---

## 3. RAG Agent

The RAG (Retrieval Augmented Generation) agent retrieves relevant information from uploaded documents.

Workflow:

Documents
↓
Chunking
↓
Embedding
↓
Vector Database
↓
Similarity Search
↓
LLM Response

---

## 4. OCR Agent

The OCR agent extracts text from uploaded documents.

Example supported documents:

* National ID
* Passport
* Driving License

---

## 5. Verification Agent

This agent analyzes the extracted text and determines whether the uploaded document appears to be a valid identity document.

---

# LangSmith Monitoring

LangSmith is used for monitoring and tracing the chatbot workflow.

It provides visibility into:

* Agent execution
* Tool usage
* Prompt chains
* LLM responses

This helps developers debug and optimize AI systems.

---

# Example Queries

Users can ask questions such as:

```
What is KYC verification?

What documents are required for KYC?

How do banks verify identity?

Explain AML compliance.
```

Users can also upload identity documents to extract and verify information.

---

# Future Improvements

Possible improvements include:

* Face verification
* Fraud detection
* Support for more document types
* Better UI design
* Cloud deployment

---

# Project Demonstration

This project demonstrates the integration of:

* AI agents
* RAG pipelines
* document processing
* vector databases
* LLM-powered assistants

It serves as a practical example of building modern AI applications.

---

# Author

Student Project – AI Chatbot Application
Built using LangChain, Gemini API, and Streamlit.
