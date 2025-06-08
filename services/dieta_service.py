from services.proteina_service import calcular_proteina
from services.gordura_service import calcular_gordura
from services.gasto_basal import gasto_energetico_total, calculo_basal
from schemas.base import CalculoDieta, GastoTotal, CalculoBasal, ObjetivoEnum

def calcular_macros(input: CalculoDieta) -> dict:
    info_basal = CalculoBasal(
        peso=input.peso,
        altura=input.altura,
        idade=input.idade,
        sexo=input.sexo
    )

    basal = calculo_basal(info_basal)

    tdee = round(gasto_energetico_total(basal, input.nivel_atividade), 0)

    # Ajuste calórico baseado no objetivo e porcentagem personalizada
    if input.objetivo == ObjetivoEnum.emagrecer:
        calorias_ajustadas = tdee * (1 - (input.nivel_calorico / 100))  # déficit
    elif input.objetivo == ObjetivoEnum.hipertrofia:
        calorias_ajustadas = tdee * (1 + (input.nivel_calorico / 100))  # superávit
    else:  # manter
        calorias_ajustadas = tdee

    proteina = calcular_proteina(input)
    calorias_proteina = proteina * 4

    gordura = calcular_gordura(input.peso, input.objetivo)
    calorias_gordura = gordura * 9

    calorias_alocadas = calorias_proteina + calorias_gordura
    calorias_restantes = calorias_ajustadas - calorias_alocadas

    carboidrato = round(calorias_restantes / 4, 2)
    calorias_carboidrato = carboidrato * 4

    # Porcentagens
    pct_proteina = (calorias_proteina / calorias_ajustadas) * 100
    pct_gordura = (calorias_gordura / calorias_ajustadas) * 100
    pct_carboidrato = (calorias_carboidrato / calorias_ajustadas) * 100

    return {
        "gasto_basal": round(basal, 2),
        "gasto_energetico_total": round(tdee, 2),
        "calorias": round(calorias_ajustadas, 2),
        "proteina": {
            "gramas": round(proteina, 2),
            "percentual": round(pct_proteina, 2)
        },
        "gordura": {
            "gramas": round(gordura, 2),
            "percentual": round(pct_gordura, 2)
        },
        "carboidrato": {
            "gramas": round(carboidrato, 2),
            "percentual": round(pct_carboidrato, 2)
        }
    }
