from enum import IntEnum, Enum
class NivelAtividadeEnum(IntEnum):
    sedentario = 0
    atleta_esporadico = 1
    resistencia = 2
    misto = 3
    forca = 4

class ObjetivoEnum(IntEnum):
    emagrecer = 0
    manter = 1
    hipertrofia = 2
    
class SexoEnum(IntEnum):
    homem = 0
    mulher = 1
    
class NafEnum(IntEnum):
    sedentario = 0
    atleta_esporadico = 1
    ativo = 2
    muito_ativo = 3
    extremamente_ativo = 4
    
class EstadoFisicoEnum(IntEnum):
    muito_magro = 0
    magro = 1
    normal = 2
    sobrepeso = 3
    obeso = 4