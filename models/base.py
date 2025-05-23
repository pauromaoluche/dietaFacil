from enum import IntEnum

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