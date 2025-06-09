from schemas.base import CalculoProteina, ResultadoProteina
from schemas.enum import EstadoFisicoEnum, NivelAtividadeEnum
from services.corporal import imc, peso_idel

def calcular_proteina(input: CalculoProteina): 
    calc_imc = imc(input.peso, input.altura)
    peso_referencia = input.peso

    if ((getattr(input, 'percentual_gordura', None) is not None and input.percentual_gordura >= 25.0) or
        (getattr(input, 'estado_fisico', None) is not None and input.estado_fisico >= EstadoFisicoEnum.sobrepeso)):
        if calc_imc["imc"] > 24.9:
            peso_referencia = round(peso_idel(24.9, input.altura), 1)

    valor_final = round(2 * peso_referencia, 2)
    return ResultadoProteina(proteinas=valor_final)

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
