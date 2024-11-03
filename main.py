from fastapi import FastAPI, Depends
from services.amadeusapi import requestAmadeus
from sqlalchemy.orm import Session
from models.models import Base, Item
from db.database import engine, get_db

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/busca/")
async def read_item(origem: str, destino: str, moeda: str, data: str, viajantes: dict, db: Session = Depends(get_db)):
    city_destiny = db.query(Item).filter(Item.city_code == destino).first()
    city_origin = db.query(Item).filter(Item.city_code == origem).first()
    if not city_destiny or not city_origin:
        return {"error":"City not found"}
    city_status = city_destiny.status
    amadeus_response = requestAmadeus(origem, destino, moeda, data, viajantes)
    return {"city_status": city_status, "amadeus_response": amadeus_response}