from fastapi import APIRouter
from schemas.base import CalculoDieta
from services.dieta_service import calcular_macros

router = APIRouter()

router = APIRouter(
    prefix="/api",               # Define um prefixo (opcional)
    tags=["Cálculo de Dieta"]      # Nome que aparecerá na documentação
)

@router.post("/calcularDieta")
def calcular(input: CalculoDieta):
    return calcular_macros(input)