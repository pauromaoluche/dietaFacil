from fastapi import APIRouter
from schemas.base import CalculoBasal, GastoTotal
from services.gasto_basal import calculo_basal, gasto_energetico_total


router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Gasto Basal"]
)

@router.post("/calculoBasal")
def calculo_Basal(input: CalculoBasal):
    return calculo_basal(input)

@router.post("/gastoEnergeticoTotal")
def gasto_de_energia_total(input: GastoTotal):
    return gasto_energetico_total(input)