from fastapi import APIRouter

router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Carboidratos"]
)

@router.post("/calcularProteinas")
def calcular(input: CalculoDieta):
    return calcular_proteina(input)