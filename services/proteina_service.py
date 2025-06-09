from schemas.base import CalculoProteina, ResultadoProteina
from schemas.enum import NivelAtividadeEnum
from services.corporal_service import get_peso_referencia

def calcular_proteina(input: CalculoProteina): 

    peso_referencia = get_peso_referencia(input)

    valor_final = round(2 * peso_referencia)
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
