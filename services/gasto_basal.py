from schemas.base import CalculoBasal, GastoTotal
from schemas.enum import SexoEnum, NafEnum

def calculo_basal(input: CalculoBasal) -> float:
    match input.sexo:
        case SexoEnum.homem:
            return 66.5 + (13.75 * input.peso) + (5 * input.altura) - (6.75 * input.idade)
        case SexoEnum.mulher:
            return 665 + (9.6 * input.peso) + (1.8 * input.altura) - (4.7 * input.idade)
        
def gasto_energetico_total(input: GastoTotal) -> float:
    basal = calculo_basal(input)
    
    match input.nivel_atividade:
        case NafEnum.sedentario:
            return basal * 1.2
        case NafEnum.atleta_esporadico:
            return basal * 1.375
        case NafEnum.ativo:
            return basal * 1.55
        case NafEnum.muito_ativo:
            return basal * 1.725
        case NafEnum.extremamente_ativo:
            return basal * 1.9