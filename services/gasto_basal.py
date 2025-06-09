from schemas.base import CalculoBasal, ResultadoGEB, GastoTotal, ResultadoGET
from schemas.enum import SexoEnum, NafEnum
from services.corporal import imc, peso_idel

def calculo_basal(input: CalculoBasal) -> int:

    calc_imc = imc(input.peso, input.altura)
    peso_referencia = input.peso
    if calc_imc["imc"] > 24.9:
        peso_referencia = round(peso_idel(24.9, input.altura), 1)

    match input.sexo:
        # Formula de Mifflin-St Jeor para calculo de gasto basal
        case SexoEnum.homem:
            calc = (10 * peso_referencia) + (6.25 * input.altura) - (5 * input.idade) + 5
        case SexoEnum.mulher:
            calc = (10 * peso_referencia) + (6.25 * input.altura) - (5 * input.idade) - 161

    return ResultadoGEB(gasto_basal=round(calc))
        
def gasto_energetico_total(input: GastoTotal) -> float:
    
    match input.frequencia_atividade:
        case NafEnum.sedentario:
            calc = input.basal * 1.2
        case NafEnum.atleta_esporadico:
            calc = input.basal * 1.375
        case NafEnum.ativo:
            calc = input.basal * 1.55
        case NafEnum.muito_ativo:
            calc = input.basal * 1.725
        case NafEnum.extremamente_ativo:
            calc = input.basal * 1.9

    return ResultadoGET(gasto_energetico_total=round(calc))