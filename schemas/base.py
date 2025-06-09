from typing import Optional
from schemas.enum import NivelAtividadeEnum, ObjetivoEnum, SexoEnum, NafEnum, EstadoFisicoEnum
from pydantic import BaseModel, Field, model_validator

class CalculoDieta(BaseModel):
    atividade: NivelAtividadeEnum = Field(
        ...,
        description=(
            "- **Nível** de atividade:\n"
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
    ),
    altura: int = Field(..., description="Altura em cm"),
    idade: int = Field(..., description="Sua idade"),
    nivel_calorico: int = Field(..., description="de 0 a 50%"),
    frequencia_atividade: NafEnum = Field(
        ...,
        description=(
            "Nível de atividade:\n"
            "0 = Sedentário (pouca ou nenhuma atividade)\n"
            "1 = atleta esporádico (1-3 dias por semana)\n"
            "2 = ativa (3-5 dias por semana)\n"
            "3 = muito ativa (5-7 dias por semana)\n"
            "4 = muito ativa e intensa (diária, incluindo exercícios pesados)"
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
    basal: float = Field(..., description="Seu peso em kg"),
    frequencia_atividade: NafEnum = Field(
        ...,
        description=(
            "Nível de atividade:\n"
            "0 = Sedentário (pouca ou nenhuma atividade)\n"
            "1 = atleta esporádico (1-3 dias por semana)\n"
            "2 = ativa (3-5 dias por semana)\n"
            "3 = muito ativa (5-7 dias por semana)\n"
            "4 = muito ativa e intensa (diária, incluindo exercícios pesados)"
        )
    )   

class CalculoProteina(BaseModel):
    peso: float = Field(..., description="Seu peso em kg"),
    altura: int = Field(..., description="Altura em cm"),
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
    
class ResultadoProteina(BaseModel):
    proteinas: float = Field(..., description="Gramas de proteína recomendadas")

class ResultadoGEB(BaseModel):
    gasto_basal: int = Field(..., description="Gasto basal")

class ResultadoGET(BaseModel):
    gasto_energetico_total: int = Field(..., description="Gasto basal")