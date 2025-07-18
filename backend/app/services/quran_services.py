from ..models.query import QueryResponse
from ..utils.query_ayahs import get_embedding, search_ayahs,map_bm25_hits_to_ayahs
from ..utils.get_hadith import extract_narrators_chain_with_llm
from ..rag.ayah_filter import filter_relevant_ayahs
from ..rag.bm25_engine import bm25_engine



def validate_hadith(query: str):
    narrators , query = extract_narrators_chain_with_llm(query)
    query_vector = get_embedding(query)
    ayahs = search_ayahs(query_vector=query_vector, limit=15)
    filtered_ayahs = filter_relevant_ayahs(ayahs=ayahs, hadith_text=query)

    keyword_hits = bm25_engine.search(query, top_n=15)
    bm25_results = map_bm25_hits_to_ayahs(keyword_hits)

    return QueryResponse(results=filtered_ayahs + bm25_results)
