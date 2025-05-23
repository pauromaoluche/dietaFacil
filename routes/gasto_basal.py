from fastapi import APIRouter
from schemas.base import CalculoBasal
from services.gasto_basal import calculo_basal


router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Gasto Basal"]
)

@router.post("/calculoBasal")
def calcular(input: CalculoBasal):
    return calculo_basal(input)