from schemas.base import CalculoGordura, ResultadoGordura
from schemas.enum import ObjetivoEnum
#from services.corporal_service import get_peso_referencia

def calcular_gordura(input: CalculoGordura) -> int:
    match input.objetivo:
        case ObjetivoEnum.emagrecer:
            quantidade = 0.8
        case ObjetivoEnum.hipertrofia:
            quantidade = 1.5
        case _:
            quantidade = 1.2

    #peso_referencia = get_peso_referencia(input)
    
    gordura = round(quantidade * input.peso)
    return ResultadoGordura(gordura=gordura)
