from pydantic import BaseModel, Field
from models.base import NivelAtividadeEnum, ObjetivoEnum

class CalculoProteinaInput(BaseModel):
    atividade: NivelAtividadeEnum = Field(
        ...,
        description=(
            "Nível de atividade:\n"
            "0 = sedentário\n"
            "1 = atleta esporádico\n"
            "2 = resistência\n"
            "3 = misto\n"
            "4 = força"
        )
    )
    objetivo: ObjetivoEnum = Field(
        ...,
        description=(
            "Objetivo:\n"
            "0 = emagrecer\n"
            "1 = manter\n"
            "2 = ganhar"
        )
    )
    peso: float = Field(..., description="Seu peso em kg")