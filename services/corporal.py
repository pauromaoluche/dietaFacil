from schemas.base import CalculoDieta
from schemas.enum import EstadoFisicoEnum, SexoEnum

def estimar_perc_gordura(estado: EstadoFisicoEnum, sexo: SexoEnum) -> float:
    match sexo:
        case SexoEnum.homem:
            map = {
                EstadoFisicoEnum.muito_magro: 7.0,
                EstadoFisicoEnum.magro: 10,
                EstadoFisicoEnum.normal: 15,
                EstadoFisicoEnum.sobrepeso: 22,
                EstadoFisicoEnum.obeso: 30,
            }
        case SexoEnum.mulher:
            map = {
                EstadoFisicoEnum.muito_magro: 10,
                EstadoFisicoEnum.magro: 15,
                EstadoFisicoEnum.normal: 22,
                EstadoFisicoEnum.sobrepeso: 30,
                EstadoFisicoEnum.obeso: 36.0,
            }
    return map[estado]


def calc_massa_magra(percGordura: float, peso: float) -> dict:
    gordura = (percGordura / 100) * peso
    massa_magra = peso - gordura
    
    return {
        "gordura": gordura,
        "massa_magra": massa_magra
    }
        
def get_peso_referencia(input: CalculoDieta) -> float:
    if getattr(input, 'percentual_gordura', None) and input.percentual_gordura >= 25.0:
        return calc_massa_magra(input.percentual_gordura, input.peso)["massa_magra"]
    elif getattr(input, 'estado_fisico', None) is not None and input.estado_fisico >= EstadoFisicoEnum.sobrepeso:
        estimado = estimar_perc_gordura(input.estado_fisico, input.sexo)
        return calc_massa_magra(estimado, input.peso)["massa_magra"]
    return input.peso