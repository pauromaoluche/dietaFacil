from fastapi import APIRouter

from schemas.base import CalculoProteina, ResultadoProteina
from services.proteina_service import calcular_proteina

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Proteinas"]
)

@router.post(
    "/calcularProteinas",
    summary="Calcula a quantidade de proteinas de acordo com o Imc Ideal, 24,9",
    description="""
    Este endpoint calcula as proteinas de acordo com o Imc ideal 24,9(padrão).

### Parâmetros de entrada:
- **peso**: Peso do usuário (kg)
- **altura**: Altura do usuário (cm)
- **percentual_gordura**: Percentual de gordura(Opcional)
- **estado_fisico**: Se não informar percentual, escolha uma opção:
  - muito_magro = 0
  - magro = 1
  - normal = 2
  - sobrepeso = 3
  - obeso = 4
""",
    response_description="Retorna o valor em gramas de proteina",
    response_model=ResultadoProteina
)
def calcular(input: CalculoProteina):
    return calcular_proteina(input)
