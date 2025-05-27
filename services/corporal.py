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
        