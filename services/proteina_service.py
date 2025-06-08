from schemas.base import CalculoDieta
from services.corporal import estimar_perc_gordura, calc_massa_magra, get_peso_referencia, imc, peso_idel
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum, EstadoFisicoEnum

def calcular_proteina(input: CalculoDieta): 
    calc_imc = imc(input.peso, input.altura)
    peso_referencia = input.peso
    if input.percentual_gordura > 25:
        if calc_imc["imc"] > 24.9:
            peso_referencia = round(peso_idel(24.9, input.altura), 1)   
    return round(2 * peso_referencia, 2)
    #return round(valor_proteina * peso_referencia, 2)

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
