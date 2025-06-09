from fastapi import APIRouter
from schemas.base import CalculoDieta, ResultadoDieta
from services.dieta_service import calcular_macros

router = APIRouter()

router = APIRouter(
    prefix="/api",
    tags=["Cálculo de Dieta"]
)

@router.post(
    "/calcularDieta",
    summary="Calcula os macronutrientes para uma dieta personalizada",
    description="""
Este endpoint calcula os macronutrientes necessários para uma dieta personalizada com base nas informações fornecidas pelo usuário. 

### Parâmetros de entrada:
- **atividade**: Tipo de atividade:
  - sedentario (nada ou pouca atividade fisica) = 0
  - atleta_esporadico (faz atividade fisica, mas de maneira não aleatorio) = 1
  - resistencia (corrida, crossfit, etc...) = 2
  - misto (faz de tudo) = 3
  - forca (musculacao ou atividades que precisam de força) = 4
- **objetivo**: Objetivo do usuário: 
  - emagrecer = 0
  - manter = 1
  - hipertrofia = 2
- **peso**: Peso do usuário (kg)
- **sexo**: Sexo do usuário
- **altura**: Altura do usuário (cm)
- **idade**: Idade do usuário
- **nivel_calorico**: Percentual de ajuste calórico para atingir o objetivo (ex: de 0 a 50%)
- **frequencia_atividade**: Frequencia da atividade fisica:
  - sedentario (nada ou pouca atividade fisica)
  - atleta_esporadico (1-3 dias por semana)
  - ativo (3-5 dias por semana)
  - muito ativo (5-7 dias por semana)
  - muito ativa e intensa (diária, incluindo exercícios pesados)
- **percentual_gordura**: Percentual de gordura(Opcional)
- **estado_fisico**: Se não informar percentual, escolha uma opção:
  - muito_magro = 0
  - magro = 1
  - normal = 2
  - sobrepeso = 3
  - obeso = 4



### Resposta:
Retorna os valores dos macronutrientes recomendados (proteínas, gorduras e carboidratos) em gramas e seus respectivos percentuais em relação ao total de calorias ajustadas, além do gasto basal e total de calorias.
""",
    response_description="Retorna os valores diarios da dieta",
    response_model=ResultadoDieta
)
def calcular(input: CalculoDieta):
    return calcular_macros(input)
