from fastapi import FastAPI, Depends
from amadeusapi import requestAmadeus
from sqlalchemy.orm import Session
from models import Base, Item
from database import engine, get_db

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/busca")
async def read_item(origem: str, destino: str, moeda: str, data: str, db: Session = Depends(get_db)):
    city = db.query(Item).filter(Item.city_code == destino).first()
    if not city:
        return {"error":"City not found"}
    city_status = city.status
    amadeus_response = requestAmadeus(origem, destino, moeda, data)
    return {"city_status": city_status, "amadeus_response": amadeus_response}