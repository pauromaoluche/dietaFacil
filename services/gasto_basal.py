from schemas.base import CalculoBasal
from schemas.enum import SexoEnum

def calculo_basal(input: CalculoBasal) -> float:
    match input.sexo:
        case SexoEnum.homem:
            return 66.5 + (13.75 * input.peso) + (5 * input.altura) - (6.75 * input.idade)
        case SexoEnum.mulher:
            return 665 + (9.6 * input.peso) + (1,8 * input.altura) - (4.7 * input.idade)