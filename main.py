from fastapi import Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import Annotated
from services.amadeusapi import requestAmadeus
from sqlalchemy.orm import Session
from models.models import Base, Item
from db.database import engine, get_db
from setup.settings import app
from auth.auth import router, get_current_user

Base.metadata.create_all(bind=engine)
app.include_router(router)
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/")
async def redirect_index():
    return RedirectResponse("/docs")

@app.post("/busca", status_code=status.HTTP_200_OK)
async def read_item(origem: str, destino: str, moeda: str, data: str, viajantes: dict, user: user_dependency, db: Session = Depends(get_db)):
    """
    Formato Viajantes: {"id": id, "travelerType: "ADULT"} tipos: [ADULT, CHILD, SENIOR, YOUNG, HELD_INFANT, SEATED_INFANT, STUDENT]\n
    Formato Data: yyyy-mm-dd\n
    Formato Moeda: BRL\n
    Formato Cidade: MCZ\n
    """
    city_destiny = db.query(Item).filter(Item.city_code == destino).first()
    city_origin = db.query(Item).filter(Item.city_code == origem).first()
    if not city_destiny or not city_origin:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")
    city_status = city_destiny.status
    amadeus_response = requestAmadeus(origem, destino, moeda, data, viajantes)
    return {f"{city_destiny.city}": city_status, "amadeus_response": amadeus_response}