from fastapi import APIRouter
from services.dashboard_service import gerar_resumo_por_vime

router = APIRouter()

@router.get("/resumo/{ano}/{vime}")
def resumo(ano: str, vime: str):
    return gerar_resumo_por_vime(vime, ano)