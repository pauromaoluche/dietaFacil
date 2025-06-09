from fastapi import APIRouter

from schemas.base import CalculoGordura, ResultadoGordura
from services.gordura_service import calcular_gordura

router = APIRouter(
    prefix="/api",
    tags=["Calcular gorduras"]
)

@router.post(
    "/calcularGordura",
    summary="Calcula as gorduras necessarias de acordo com o objetivo",
    description="""
Este endpoint calcula os macronutrientes necessários para uma dieta personalizada com base nas informações fornecidas pelo usuário. 

### Parâmetros de entrada:
- **peso**: Peso do usuário (kg)
- **altura**: Altura do usuário (cm)
- **objetivo**
  - emagrecer = 0
  - manter = 1
  - hipertrofia = 2
- **percentual_gordura**: Percentual de gordura(Opcional)
- **estado_fisico**: Se não informar percentual, escolha uma opção:
  - muito_magro = 0
  - magro = 1
  - normal = 2
  - sobrepeso = 3
  - obeso = 4
""",
    response_description="Retorna o valor em gramas de gordura por dia de acordo com o objetivo.",
    response_model=ResultadoGordura
)
def calcular(input: CalculoGordura):
    return calcular_gordura(input)
