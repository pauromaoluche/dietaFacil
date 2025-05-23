from schemas.base import CalculoDieta
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum

def calcular_proteina(input: CalculoDieta): 
    proteina_por_kg = get_proteina_por_kg(input.atividade)

    if isinstance(proteina_por_kg, tuple):
        match input.objetivo:
            case ObjetivoEnum.emagrecer:
                valor_proteina = proteina_por_kg[0]
            case ObjetivoEnum.manter:
                valor_proteina = sum(proteina_por_kg) / 2
            case ObjetivoEnum.hipertrofia:
                valor_proteina = proteina_por_kg[1]
    else:
        valor_proteina = proteina_por_kg
    
    return valor_proteina * input.peso


def get_proteina_por_kg(atividade: NivelAtividadeEnum) -> tuple[float, float]:
    match atividade:
        case NivelAtividadeEnum.sedentario:
            return (0.8)
        case NivelAtividadeEnum.atleta_esporadico:
            return (1.0)
        case NivelAtividadeEnum.resistencia:
            return (1.0, 1.6)
        case NivelAtividadeEnum.misto:
            return (1.4, 1.7)
        case NivelAtividadeEnum.forca:
            return (1.6, 2.2)
