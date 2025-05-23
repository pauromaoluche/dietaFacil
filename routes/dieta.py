from fastapi import APIRouter

router = APIRouter()

router = APIRouter(
    prefix="/api",               # Define um prefixo (opcional)
    tags=["Cálculo de Dieta"]      # Nome que aparecerá na documentação
)

@router.post("/calcularDieta")
def calcular(teste):
    return "teste"