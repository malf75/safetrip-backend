from fastapi import Depends
from auth.auth import oauth2_scheme
from fastapi.responses import RedirectResponse
from services.amadeusapi import requestAmadeus
from sqlalchemy.orm import Session
from models.models import Base, Item
from db.database import engine, get_db
from setup.settings import app

Base.metadata.create_all(bind=engine)

@app.get("/")
async def redirect_index():
    return RedirectResponse("/docs")

@app.post("/busca/")
async def read_item(origem: str, destino: str, moeda: str, data: str, viajantes: dict, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    Formato Viajantes: {"id": id, "travelerType: "ADULT"} tipos: [ADULT, CHILD, SENIOR, YOUNG, HELD_INFANT, SEATED_INFANT, STUDENT]\n
    Formato Data: yyyy-mm-dd\n
    Formato Moeda: BRL\n
    Formato Cidade: MCZ\n
    """
    city_destiny = db.query(Item).filter(Item.city_code == destino).first()
    city_origin = db.query(Item).filter(Item.city_code == origem).first()
    if not city_destiny or not city_origin:
        return {"Erro":"Cidade não encontrada"}
    city_status = city_destiny.status
    amadeus_response = requestAmadeus(origem, destino, moeda, data, viajantes)
    return {f"{city_destiny.city}": city_status, "amadeus_response": amadeus_response, "token":token}