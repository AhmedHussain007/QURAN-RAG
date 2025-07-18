import os
import numpy as np
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from typing import List
from ..models.query import AyahResult
import json
import string
load_dotenv()

embedding_client = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_key=os.getenv("OPENAI_API_KEY")
);


def get_embedding(text):
    try:
        embedding = embedding_client.embed_query(text)
        return list(np.array(embedding, dtype=np.float32))
    except Exception as e:
        print("Error while getting embedding:", e)
        return None



def get_qdrant_client():
    return QdrantClient(
        url=os.getenv("QDRANT_URL"),
        api_key=os.getenv("QDRANT_API_KEY"),
        prefer_grpc=False,
        timeout=30.0
    )


def search_ayahs(query_vector: List[float], limit: int = 15) -> List[AyahResult]:
    client = get_qdrant_client()
    search_response = client.search(
        collection_name="quran_embeddings",
        query_vector=query_vector,
        limit=limit
    )
    return [
        AyahResult(
            score=hit.score,
            english_translation=hit.payload["english_translation"],
            surah_name_english=hit.payload["surah_name_english"],
            aya_number=hit.payload["aya_number"],
            arabic_diacritics=hit.payload.get("arabic_diacritics", "")
        )
        for hit in search_response
    ]


def preprocess_text(text: str) -> str:
    """Lowercase and remove punctuation from a string."""
    return text.strip().lower().translate(str.maketrans("", "", string.punctuation))


def map_bm25_hits_to_ayahs(keyword_hits: list[dict]) -> list[AyahResult]:
    """Map BM25 keyword hits to actual AyahResult objects using Quran metadata with preprocessing match."""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    metadata_path = os.path.join(BASE_DIR, "..", "quran_metadata.json")
    metadata_path = os.path.abspath(metadata_path)

    with open(metadata_path, "r", encoding="utf-8") as f:
        quran_metadata = json.load(f)

    # Preprocess ayah translations once
    processed_ayah_map = {
        preprocess_text(ayah["english_translation"]): ayah
        for ayah in quran_metadata
    }

    results = []
    for hit in keyword_hits:
        cleaned_hit_text = preprocess_text(hit["text"])
        if cleaned_hit_text in processed_ayah_map:
            ayah = processed_ayah_map[cleaned_hit_text]
            results.append(
                AyahResult(
                    score=float(hit["score"]),
                    english_translation=ayah["english_translation"],
                    surah_name_english=ayah["surah_name_english"],
                    aya_number=ayah["aya_number"],
                    arabic_diacritics=ayah.get("arabic_diacritics", "")
                )
            )

    return results
