from typing import Optional
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum, SexoEnum, NafEnum, EstadoFisicoEnum
from pydantic import BaseModel, Field, model_validator

class CalculoDieta(BaseModel):
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
    peso: float = Field(..., description="Seu peso em kg"),
    sexo: SexoEnum = Field(
        ...,
        description=(
            "0 = Homem "
            "1 = Mulher"
        )
    )
    percentual_gordura: Optional[float] = Field(
        None, description="Percentual de gordura corporal, se souber"
    )
    estado_fisico: Optional[EstadoFisicoEnum] = Field(
        None, description="Seu estado físico estimado (caso não saiba o percentual de gordura)"
    )
    @model_validator(mode="after")
    def validar_gordura_ou_estado(self) -> 'CalculoDieta':
        if self.percentual_gordura is None and self.estado_fisico is None:
            raise ValueError("Informe ao menos 'percentual_gordura' ou 'estado_fisico'")
        return self
    
class CalculoBasal(BaseModel):
    peso: float = Field(..., description="Seu peso em kg"),
    altura: int = Field(..., description="Altura em cm"),
    idade: int = Field(..., description="Sua idade"),
    sexo: SexoEnum = Field(
        ...,
        description=(
            "0 = Homem "
            "1 = Mulher"
        )
    )
    
class GastoTotal(BaseModel):
    peso: float = Field(..., description="Seu peso em kg"),
    altura: int = Field(..., description="Altura em cm"),
    idade: int = Field(..., description="Sua idade"),
    sexo: SexoEnum = Field(
        ...,
        description=(
            "0 = Homem "
            "1 = Mulher"
        )
    )
    nivel_atividade: NafEnum = Field(
        ...,
        description=(
            "0 = sedentario "
            "1 = atleta_esporadico "
            "2 = ativo "
            "3 = muito_ativo "
            "4 extremamente_ativo"
        )
    )   