from fastapi import FastAPI
from amadeusapi import requestAmadeus
from models import Base
from database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/busca/")
async def read_item(origem: str, destino: str, moeda: str, data: str):
    return requestAmadeus(origem, destino, moeda, data)