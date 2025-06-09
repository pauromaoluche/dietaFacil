from fastapi import APIRouter

from schemas.base import CalculoBasal, GastoTotal, ResultadoGEB, ResultadoGET
from services.gasto_basal import calculo_basal, gasto_energetico_total

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Gasto Basal"]
)

@router.post(
    "/calculoBasal",
    summary="Calcula o seu gasto basal.",
    description="""
    Quantidade de calorias que seu corpo precisa por dia, GEB(Gasto Energetico Basal).

### Parâmetros de entrada:
- **peso**: Peso do usuário (kg)
- **altura**: Altura do usuário (cm)
- **sexo**
  - masculino = 0
  - feminino = 1
""",
    response_description="Retorna a calorias que seu corpo precisa por dia.",
    response_model=ResultadoGEB
)
def calculo_Basal(input: CalculoBasal):
    return calculo_basal(input)

@router.post(
    "/gastoEnergeticoTotal",
    summary="Calcula o seu Gasto de Energia Total",
    description="""
    Quantidade Gasto de Energia Total de acordo com sua atividade fisica.

### Parâmetros de entrada:
- **basal**: seu gasto basal
- **frequencia_atividade**:
  - Sedentário (pouca ou nenhuma atividade) = 0
  - Atleta esporádico (1-3 dias por semana) = 1
  - Ativa (3-5 dias por semana) = 2
  - Muito ativa (5-7 dias por semana) = 3
  - Muito ativa e intensa (diária, incluindo exercícios pesados) = 4
""",
    response_description="Retorna suas calorias de acordo com sua frequencia fisica.",
    response_model=ResultadoGET
)
def gasto_de_energia_total(input: GastoTotal):
    return gasto_energetico_total(input)