from schemas.base import CalculoDieta
from services.corporal import estimar_perc_gordura, calc_massa_magra, get_peso_referencia
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum, EstadoFisicoEnum

def calcular_proteina(input: CalculoDieta): 
    peso = get_peso_referencia(input)
    proteina_por_kg = get_proteina_por_kg(input.atividade)
      
    if isinstance(proteina_por_kg, tuple):
        valor_proteina = (
            proteina_por_kg[0] if input.objetivo == ObjetivoEnum.emagrecer else
            proteina_por_kg[1] if input.objetivo == ObjetivoEnum.hipertrofia else
            sum(proteina_por_kg) / 2
        )
    else:
        valor_proteina = proteina_por_kg[0]
    
    return round(valor_proteina * peso, 2)


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
