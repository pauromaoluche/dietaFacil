from schemas.base import CalculoDieta
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum
from services.corporal_service import imc, peso_idel

def calcular_carboidratos(input: CalculoDieta):

    calc_imc = imc(input.peso, input.altura)
    peso_referencia = input.peso
    if input.percentual_gordura > 25:
        if calc_imc["imc"] > 24.9:
            peso_referencia = round(peso_idel(24.9, input.altura), 1)

    carboidrato_por_atividade = get_carboidrato_por_atividade(input.atividade)
        
    if isinstance(carboidrato_por_atividade, tuple):
        match input.objetivo:
            case ObjetivoEnum.emagrecer:
                valor_carboidrato = carboidrato_por_atividade[0]
            case ObjetivoEnum.manter:
                valor_carboidrato = sum(carboidrato_por_atividade) / 2
            case ObjetivoEnum.hipertrofia:
                valor_carboidrato = carboidrato_por_atividade[1]
    else:
        valor_carboidrato = carboidrato_por_atividade[0]
    
    return round(valor_carboidrato * peso_referencia, 2)

def get_carboidrato_por_atividade(atividade: NivelAtividadeEnum) -> tuple[float, float]:
    match atividade:
        # Manutenção ou leve redução
        case NivelAtividadeEnum.sedentario:
            return (2.0, 3.0)
        # Leve a moderado (3~4g/kg massa magra)
        case NivelAtividadeEnum.atleta_esporadico:
            return (3.0, 3.0)
        # Endurance realista, para amadores
        case NivelAtividadeEnum.resistencia:
            return (4.0, 5.0)  
        # Combinação de força + cardio
        case NivelAtividadeEnum.misto:
            return (3.5, 4.5)  
        # Hipertrofia/força recreacional
        case NivelAtividadeEnum.forca:
            return (3.5, 4.5) 
        case _:
            return (2.0, 3.0)