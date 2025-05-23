from typing import Union, Tuple

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()
class PerfilDieta(BaseModel):
    peso: float = Field(..., gt=0, description="Peso em kg")
    altura: float = Field(..., gt=0, description="Altura em cm")
    idade: int = Field(..., gt=0, description="Idade em anos")
    sexo: int = Field(..., description="Sexo (1 = masculino, 2 = feminino)")
    atividade: int = Field(..., description="Nível de atividade (1 = leve, 2 = moderada, 3 = intensa)")
    objetivo: int = Field(..., description="Objetivo (1 = emagrecer, 2 = manter, 3 = ganhar)"),
    nivel: int = Field(..., description="Nivel da dieta (1 = leve, 2 = intermediaria, 3 = maxima)")
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "peso": 118.5,
                    "altura": 183,
                    "idade": 23,
                    "sexo": 1,
                    "atividade": 2,
                    "objetivo": 1,
                    "nivel": 2
                }
            ]
        }
    }

objetivos_map = {
    1: "emagrecer",
    2: "manter",
    3: "hipertrofia"
}

recomendacoes_proteina: dict[str, Tuple[float, float]] = {
    "emagrecer": (1.6, 2.2),
    "manter": (1.2, 1.6),
    "hipertrofia": (1.6, 2.4)
}

@app.post("/calcular-dieta/")
def calcular_dieta(perfil: PerfilDieta):
    objetivo_nome = objetivos_map.get(perfil.objetivo)
    if not objetivo_nome:
        return {"erro": "Objetivo inválido"}

    faixa_proteina = recomendacoes_proteina[objetivo_nome]
    min_proteina = round(perfil.peso * faixa_proteina[0], 2)
    max_proteina = round(perfil.peso * faixa_proteina[1], 2)

    return {
        "mensagem": "Dieta calculada com sucesso",
        "objetivo": objetivo_nome,
        "faixa_proteina_g": {
            "min": min_proteina,
            "max": max_proteina
        },
        "perfil": perfil
    }