from schemas.base import CalculoDieta
from schemas.enum import EstadoFisicoEnum, SexoEnum

def estimar_perc_gordura(estado: EstadoFisicoEnum, sexo: SexoEnum) -> float:
    match sexo:
        case SexoEnum.homem:
            map = {
                EstadoFisicoEnum.muito_magro: 10,
                EstadoFisicoEnum.magro: 17,
                EstadoFisicoEnum.normal: 20,
                EstadoFisicoEnum.sobrepeso: 29,
                EstadoFisicoEnum.obeso: 34,
            }
        case SexoEnum.mulher:
            map = {
                EstadoFisicoEnum.muito_magro: 10,
                EstadoFisicoEnum.magro: 17,
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
    calc_imc = imc(input.peso, input.altura)
    peso_referencia = input.peso
    if ((getattr(input, 'percentual_gordura', None) is not None and input.percentual_gordura >= 25.0) or
        (getattr(input, 'estado_fisico', None) is not None and input.estado_fisico >= EstadoFisicoEnum.sobrepeso)):
        if calc_imc["imc"] > 24.9:
            peso_referencia = round(peso_idel(24.9, input.altura), 1)
            
    return peso_referencia

def imc(peso: float, altura: int) -> dict:
    imc = peso / ((altura / 100 ) ** 2)

    if imc <= 18.5:
        message ="Classificação: Abaixo do peso"
    elif imc <= 24.9:
        message ="Classificação: Peso normal"
    elif imc <= 29.9:
        message ="Classificação: Sobrepeso"
    elif imc <= 34.9:
        message ="Classificação: Obesidade grau 1"
    elif imc <= 39.9:
        message ="Classificação: Obesidade grau 2"
    else:
        message ="Classificação: Obesidade grau 3 (mórbida)"

    return {
        "message": message,
        "imc": round(imc, 1)
    }

def peso_idel(imcDesejado: float, altura: float) -> float:
    return imcDesejado * ((altura / 100) ** 2)