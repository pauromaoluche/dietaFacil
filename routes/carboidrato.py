from fastapi import APIRouter
from schemas.base import CalculoDieta
from services.carboidrato_service import calcular_carboidratos

router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Carboidratos"]
)

@router.post("/calcularCarboidratos")
def calcular(input: CalculoDieta):
    return calcular_carboidratos(input)