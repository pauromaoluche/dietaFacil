from fastapi import FastAPI
from routes import dieta, proteina, gasto_basal, gordura

app = FastAPI()
app.include_router(dieta.router)
app.include_router(proteina.router)
app.include_router(gasto_basal.router)
app.include_router(gordura.router)
