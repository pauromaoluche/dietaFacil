from fastapi import APIRouter
from models.dieta import CalculoProteinaInput
from services.proteina_service import calcular_proteina

router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Proteinas"]
)

@router.post("/calcularProteinas")
def calcular(input: CalculoProteinaInput):
    return calcular_proteina(input)