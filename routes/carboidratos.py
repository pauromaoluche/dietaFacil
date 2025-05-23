from fastapi import APIRouter
from schemas.base import CalculoDieta

router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Carboidratos"]
)

@router.post("/calcularProteinas")
def calcular(input: CalculoDieta):
    return calcular_proteina(input)