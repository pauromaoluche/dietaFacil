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
- **peso**: Peso do usuário (kg)
- **altura**: Altura do usuário (cm)
- **idade**: Idade do usuário
- **sexo**: Sexo do usuário (masculino ou feminino)
- **frequencia_atividade**: Nível de atividade física do usuário (sedentário, moderado, ativo)
- **objetivo**: Objetivo do usuário (emagrecer, hipertrofia ou manter peso)
- **nivel_calorico**: Percentual de ajuste calórico para atingir o objetivo (ex: de 0 a 50%)

### Resposta:
Retorna os valores dos macronutrientes recomendados (proteínas, gorduras e carboidratos) em gramas e seus respectivos percentuais em relação ao total de calorias ajustadas, além do gasto basal e total de calorias.
""",
    response_description="Retorna os valores diarios da dieta",
    response_model=ResultadoDieta
)
def calcular(input: CalculoDieta):
    return calcular_macros(input)
