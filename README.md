# 📝 Semantic Plagiarism Checker

A web-based AI application that detects **plagiarism and semantic similarity** in text documents.  
Unlike traditional string-matching tools, this project uses **NLP embeddings** and **vector similarity search** to identify not just exact matches, but also **paraphrased or semantically similar content**.

---

## 🚀 Features
- Detects **exact matches** and **near-duplicate content**.  
- Uses **Sentence-BERT embeddings** for semantic similarity.  
- **FAISS** for fast similarity search on large text datasets.  
- **Flask web app** with file upload & real-time similarity scoring.  
- Supports multiple documents for cross-checking.  

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask  
- **NLP Models**: Sentence-BERT (`all-MiniLM-L6-v2`)  
- **Similarity Search**: FAISS  
- **Frontend**: HTML, CSS (basic UI)  
