from schemas.base import CalculoDieta
from schemas.enum import NivelAtividadeEnum, EstadoFisicoEnum, ObjetivoEnum
from services.corporal import estimar_perc_gordura, calc_massa_magra

def calcular_carboidratos(input: CalculoDieta):
    carboidrato_por_atividade = get_carboidrato_por_atividade(input.atividade)
    
    if hasattr(input, 'percentual_gordura') and input.percentual_gordura > 25:
        # Faz a estimativa de quanto a pessoa tem de massa magra, para fazer o calculo de proteina, caso a pessoa tenha mais de 30% de gordura
        massa_magra = calc_massa_magra(input.percentual_gordura, input.peso)
        peso_referencia = massa_magra["massa_magra"]
    elif hasattr(input, 'estado_fisico') and input.estado_fisico >= EstadoFisicoEnum.sobrepeso:
        estimar_gordura = estimar_perc_gordura(input.estado_fisico, input.sexo)
        
        massa_magra = calc_massa_magra(estimar_gordura, input.peso)
        peso_referencia = massa_magra["massa_magra"]
        
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
    
    return valor_carboidrato * peso_referencia

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