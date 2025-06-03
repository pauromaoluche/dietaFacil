from schemas.base import CalculoDieta
from services.corporal import estimar_perc_gordura, calc_massa_magra
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum, EstadoFisicoEnum

def calcular_proteina(input: CalculoDieta): 
    proteina_por_kg = get_proteina_por_kg(input.atividade)
    
    if hasattr(input, 'percentual_gordura') and input.percentual_gordura >= 25:
        # Faz a estimativa de quanto a pessoa tem de massa magra, para fazer o calculo de proteina, caso a pessoa tenha mais de 30% de gordura
        massa_magra = calc_massa_magra(input.percentual_gordura, input.peso)
        input.peso = massa_magra["massa_magra"]
    elif hasattr(input, 'estado_fisico') and input.estado_fisico >= EstadoFisicoEnum.sobrepeso:
        estimar_gordura = estimar_perc_gordura(input.estado_fisico, input.sexo)
        
        massa_magra = calc_massa_magra(estimar_gordura, input.peso)
        input.peso = massa_magra["massa_magra"]
        
    if isinstance(proteina_por_kg, tuple):
        match input.objetivo:
            case ObjetivoEnum.emagrecer:
                valor_proteina = proteina_por_kg[0]
            case ObjetivoEnum.manter:
                valor_proteina = sum(proteina_por_kg) / 2
            case ObjetivoEnum.hipertrofia:
                valor_proteina = proteina_por_kg[1]
    else:
        valor_proteina = proteina_por_kg[0]
    
    return valor_proteina * input.peso


def get_proteina_por_kg(atividade: NivelAtividadeEnum) -> tuple[float, float]:
    match atividade:
        case NivelAtividadeEnum.sedentario:
            return (0.8, 1.0)
        case NivelAtividadeEnum.atleta_esporadico:
            return (1.0, 1.1)
        case NivelAtividadeEnum.resistencia:
            return (1.0, 1.5)
        case NivelAtividadeEnum.misto:
            return (1.4, 1.6)
        case NivelAtividadeEnum.forca:
            return (1.5, 2.0)
