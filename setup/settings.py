import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(override=True)
app = FastAPI()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
AMADEUS_API_KEY = str(os.getenv('AMADEUS_API_KEY'))
SQLALCHEMY_DATABASE_URL = str(os.getenv('SQLALCHEMY_DATABASE_URL'))
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 180

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)