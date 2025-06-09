from services.proteina_service import calcular_proteina
from services.gordura_service import calcular_gordura
from services.gasto_basal import gasto_energetico_total, calculo_basal
from schemas.base import CalculoDieta, GastoTotal, CalculoBasal, ObjetivoEnum, ResultadoDieta

def calcular_macros(input: CalculoDieta) -> ResultadoDieta:
    info_basal = CalculoBasal(
        peso = input.peso,
        altura = input.altura,
        idade = input.idade,
        sexo = input.sexo
    )

    basal = calculo_basal(info_basal).gasto_basal

    gasto_total = GastoTotal(
        basal = basal,
        frequencia_atividade = input.frequencia_atividade
    )

    tdee = gasto_energetico_total(gasto_total).gasto_energetico_total

    # Ajuste calórico baseado no objetivo e porcentagem personalizada
    if input.objetivo == ObjetivoEnum.emagrecer:
        calorias_ajustadas = tdee * (1 - (input.nivel_calorico / 100))  # déficit
    elif input.objetivo == ObjetivoEnum.hipertrofia:
        calorias_ajustadas = tdee * (1 + (input.nivel_calorico / 100))  # superávit
    else:  # manter
        calorias_ajustadas = tdee

    proteina = calcular_proteina(input).proteinas
    calorias_proteina = proteina * 4

    gordura = calcular_gordura(input).gordura
    calorias_gordura = gordura * 9

    calorias_alocadas = calorias_proteina + calorias_gordura
    calorias_restantes = calorias_ajustadas - calorias_alocadas

    carboidrato = round(calorias_restantes / 4, 2)
    calorias_carboidrato = carboidrato * 4

    # Porcentagens
    pct_proteina = (calorias_proteina / calorias_ajustadas) * 100
    pct_gordura = (calorias_gordura / calorias_ajustadas) * 100
    pct_carboidrato = (calorias_carboidrato / calorias_ajustadas) * 100

    return ResultadoDieta(
        gasto_basal=basal,
        gasto_energetico_total=tdee,
        calorias=round(calorias_ajustadas, 2),
        proteina={
            "gramas": proteina,
            "percentual": round(pct_proteina, 2)
        },
        gordura={
            "gramas": gordura,
            "percentual": round(pct_gordura, 2)
        },
        carboidrato={
            "gramas": carboidrato,
            "percentual": round(pct_carboidrato, 2)
        }
    )
