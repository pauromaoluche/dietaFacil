from fastapi import FastAPI
from routes import dieta, proteina, gasto_basal, carboidrato

app = FastAPI()
app.include_router(dieta.router)
app.include_router(proteina.router)
app.include_router(gasto_basal.router)
app.include_router(carboidrato.router)

# class PerfilDieta(BaseModel):
#     peso: float = Field(..., gt=0, description="Peso em kg")
#     altura: float = Field(..., gt=0, description="Altura em cm")
#     idade: int = Field(..., gt=0, description="Idade em anos")
#     sexo: int = Field(..., description="Sexo (1 = masculino, 2 = feminino)")
#     atividade: int = Field(..., description="Nível de atividade (0 = sedentario, 1 = atleta esporádico, 2 = Exercicios de resistencia, 3 = misto, 4 = força)")
#     objetivo: int = Field(..., description="Objetivo (1 = emagrecer, 2 = manter, 3 = ganhar)"),
#     nivel: int = Field(..., description="Nivel da dieta (1 = leve, 2 = intermediaria, 3 = maxima)")
#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "peso": 118.5,
#                     "altura": 183,
#                     "idade": 23,
#                     "sexo": 1,
#                     "atividade": 2,
#                     "objetivo": 1,
#                     "nivel": 2
#                 }
#             ]
#         }
#     }

# class FaixaProteina(BaseModel):
#     min: float
#     max: float

# class DietaResposta(BaseModel):
#     mensagem: str
#     objetivo: str
#     faixa_proteina_g: FaixaProteina
#     perfil: PerfilDieta

# objetivos_map = {
#     1: "emagrecer",
#     2: "manter",
#     3: "hipertrofia"
# }

# recomendacoes_proteina: dict[str, Tuple[float, float]] = {
#     "emagrecer": (1.6, 2.2),
#     "manter": (1.2, 1.6),
#     "hipertrofia": (1.6, 2.4)
# }

# @app.post("/calcular-dieta/",
#     response_model=DietaResposta,
#     responses={
#         200: {
#             "description": "Cálculo de dieta com sucesso",
#             "content": {
#                 "application/json": {
#                     "example": {
#                         "mensagem": "Dieta calculada com sucesso",
#                         "objetivo": "emagrecer",
#                         "faixa_proteina_g": {
#                             "min": 189.6,
#                             "max": 260.7
#                         },
#                         "perfil": {
#                             "peso": 118.5,
#                             "altura": 183,
#                             "idade": 23,
#                             "sexo": 1,
#                             "atividade": 2,
#                             "objetivo": 1,
#                             "nivel": 2
#                         }
#                     }
#                 }
#             }
#         }
#     }
# )
# def calcular_dieta(perfil: PerfilDieta):
#     objetivo_nome = objetivos_map.get(perfil.objetivo)
#     if not objetivo_nome:
#         return {"erro": "Objetivo inválido"}

#     faixa_proteina = recomendacoes_proteina[objetivo_nome]
#     min_proteina = round(perfil.peso * faixa_proteina[0], 2)
#     max_proteina = round(perfil.peso * faixa_proteina[1], 2)

#     return DietaResposta(
#         mensagem="Dieta calculada com sucesso",
#         objetivo=objetivo_nome,
#         faixa_proteina_g=FaixaProteina(min=min_proteina, max=max_proteina),
#         perfil=perfil
#     )