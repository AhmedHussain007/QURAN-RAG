from fastapi import APIRouter
from ..models.query import QueryRequest, QueryResponse , HadithOnlyResponse, HadithAndNaratorsResponse , NaratorsResponse
import os
from ..services.quran_services import validate_hadith
from ..rag.narators_hadith import extract_narrators_chain_with_llm
from typing import Dict
import string
router = APIRouter()

@router.post("/get_hadith_related_ayahs", response_model=QueryResponse)
async def search_ayahs(request: QueryRequest):
    return validate_hadith(request.query)


@router.post('/get_hadith_narators', response_model=NaratorsResponse)
async def extract_narators(request: QueryRequest):
    narators, _ = extract_narrators_chain_with_llm(request.query)
    return {"narrators": narators}


@router.post('/get_hadith_content', response_model=HadithOnlyResponse)
async def extract_narators(request: QueryRequest):
    _, content = extract_narrators_chain_with_llm(request.query)
    return {"hadith_content": content}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
unique_words_path = os.path.abspath(os.path.join(BASE_DIR, "..", "unique_words.txt"))

@router.post("/keyword_search", response_model=Dict)
async def keyword_search(request: QueryRequest):
    _ , content = extract_narrators_chain_with_llm(request.query)

    content_cleaned = content.translate(str.maketrans('', '', string.punctuation))
    query_words = content_cleaned.lower().split()

    with open(unique_words_path, "r", encoding="utf-8") as f:
        unique_word_set = set(word.strip() for word in f)

    known_words = [word for word in query_words if word in unique_word_set]
    unknown_words = [word for word in query_words if word not in unique_word_set]

    return {
        "query_words": query_words,
        "known_words": known_words,
        "unknown_words": unknown_words
    }

from ..models.query import HadithCompleteInfoResponse

@router.post("/get_hadith_complete_info", response_model=HadithCompleteInfoResponse)
async def get_hadith_complete_info(request: QueryRequest):
    narrators, content = extract_narrators_chain_with_llm(request.query)
    related_ayahs_response = validate_hadith(request.query)
    content_cleaned = content.translate(str.maketrans('', '', string.punctuation))
    query_words = content_cleaned.lower().split()

    with open(unique_words_path, "r", encoding="utf-8") as f:
        unique_word_set = set(word.strip() for word in f)

    known_words = [word for word in query_words if word in unique_word_set]
    unknown_words = [word for word in query_words if word not in unique_word_set]

    return {
        "hadith_content": content,
        "narrators": narrators,
        "related_ayahs": related_ayahs_response.results,
        "keywords": {
            "query_words": query_words,
            "known_words": known_words,
            "unknown_words": unknown_words
        }
    }
