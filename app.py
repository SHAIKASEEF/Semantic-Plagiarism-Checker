from flask import Flask, request, render_template
from utils.preprocessing import preprocess_text
from utils.similarity import get_embeddings, build_faiss_index, semantic_search
import os

app = Flask(__name__)

# Load documents
DOC_FOLDER = "documents/sample_docs"
documents = []
doc_names = []

for filename in os.listdir(DOC_FOLDER):
    path = os.path.join(DOC_FOLDER, filename)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        documents.append(preprocess_text(text))
        doc_names.append(filename)

# Build embeddings and FAISS index
embeddings = get_embeddings(documents)
index = build_faiss_index(embeddings)

@app.route('/', methods=['GET', 'POST'])
def index_route():
    results = None
    if request.method == 'POST':
        query_text = preprocess_text(request.form['text'])
        query_embedding = get_embeddings([query_text])[0]

        # Semantic similarity search
        results = semantic_search(query_embedding, index, doc_names, top_k=5)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
