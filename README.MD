#  Voice-Enabled Customer Support RAG Assistant

An AI-powered Customer Support Assistant built using Django, ChromaDB, HuggingFace Embeddings, and Ollama (Llama 3.2).

The system helps customer support executives quickly retrieve answers from company policy documents using Retrieval-Augmented Generation (RAG). It also provides source citations, confidence scores, and voice playback for responses.

---

## Features

- PDF-based Knowledge Base
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Store
- HuggingFace Embeddings
- Ollama + Llama 3.2 (Local LLM)
- Source Citations
- Confidence Score
- Voice Response Playback
- Django Web Interface
- Privacy-Focused Local AI

---

## 🛠 Tech Stack

### Backend
- Django
- Python

### AI / GenAI
- LangChain
- Ollama
- Llama 3.2
- HuggingFace Embeddings

### Vector Database
- ChromaDB

### Frontend
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
customer_support_ai/

│
├── manage.py
│
├── customer_support_ai/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── support_app/
│   ├── build_db.py
│   ├── rag.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── support_app/
│           └── chat.html
│
├── data/
│   └── support_policy.pdf
│
└── chroma_db/
```

##  Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-support-rag.git

cd customer-support-rag
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Install Ollama

Download and install Ollama:

https://ollama.com

Pull Llama 3.2:

```bash
ollama pull llama3.2
```

Verify:

```bash
ollama list
```

---

##  Add Knowledge Base

Place your PDF document inside:

```text
data/support_policy.pdf
```

---

##  Build Vector Database

```bash
python support_app/build_db.py
```

Expected Output:

```text
Vector Database Created Successfully
```

---

##  Run Application

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

##  Example Questions

- What is the refund policy?
- How do customers track their orders?
- What are the support hours?
- How can a customer request a replacement?
- What payment methods are accepted?

---

## Workflow

```text
Customer Query
        ↓
Django Interface
        ↓
ChromaDB Retrieval
        ↓
Relevant PDF Chunks
        ↓
Ollama (Llama 3.2)
        ↓
Generated Answer
        ↓
Source Citations + Confidence Score
        ↓
Voice Playback
```

---

##  Future Improvements

- Multi-PDF Support
- Admin Dashboard
- Chat History Database
- User Authentication
- WhatsApp Integration
- Live Agent Handoff
- Multi-Language Support
- Speech-to-Text Input

---
