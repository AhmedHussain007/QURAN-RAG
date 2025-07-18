from fastapi import APIRouter
from ..models.query import QueryRequest, QueryResponse , HadithOnlyResponse, HadithAndNaratorsResponse , NaratorsResponse
from ..services.quran_services import validate_hadith
from ..rag.narators_hadith import extract_narrators_chain_with_llm
router = APIRouter()

@router.post("/validate", response_model=QueryResponse)
async def search_ayahs(request: QueryRequest):
    return validate_hadith(request.query)


@router.post('/get_naraters', response_model=NaratorsResponse)
async def extract_narators(request: QueryRequest):
    narators, _ = extract_narrators_chain_with_llm(request.query)
    return {"narrators": narators}


@router.post('/get_hadith', response_model=HadithOnlyResponse)
async def extract_narators(request: QueryRequest):
    _, content = extract_narrators_chain_with_llm(request.query)
    return {"hadith_content": content}


@router.post('/get_hadith_and_narators', response_model=HadithAndNaratorsResponse)
async def extract_narators(request: QueryRequest):
    narators, content = extract_narrators_chain_with_llm(request.query)
    return {
        "hadith_content": content,
        "narrators": narators
    }
