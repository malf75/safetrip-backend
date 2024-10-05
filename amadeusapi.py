import requests
import os
from dotenv import load_dotenv

load_dotenv()

def requestAmadeus(origem, destino, moeda, data):
    headers = {
        "Authorization": f"Bearer {os.getenv('AMADEUS_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        
        "currencyCode": moeda,
        "originDestinations": [
            {
                "id": "1",
                "originLocationCode": origem,
                "destinationLocationCode": destino,
                "departureDateTimeRange": {
                    "date": data
                }
            }
        ],
        "travelers": [
            {
                "id": "1",
                "travelerType": "ADULT"
            }
        ],
        "sources": ["GDS"],
        "searchCriteria":{
        "maxFlightOffers": 5,
        }
    }

    r = requests.post('https://test.api.amadeus.com/v2/shopping/flight-offers', headers=headers, json=payload)

    return r.json()