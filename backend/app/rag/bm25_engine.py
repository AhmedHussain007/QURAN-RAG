import os
from rank_bm25 import BM25Okapi

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
corpus_path = os.path.join(BASE_DIR, "..", "quran_cleaned_corpus.txt")
corpus_path = os.path.abspath(corpus_path)

class BM25Search:
    def __init__(self, file_path=corpus_path):
        with open(file_path, "r", encoding="utf-8") as f:
            self.documents = [line.strip().split() for line in f]
        self.bm25 = BM25Okapi(self.documents)

    def search(self, query: str, top_n=15):
        tokenized_query = query.lower().split()
        scores = self.bm25.get_scores(tokenized_query)
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        return [{"text": " ".join(self.documents[i]), "score": score} for i, score in ranked[:top_n]]

bm25_engine = BM25Search(corpus_path)
