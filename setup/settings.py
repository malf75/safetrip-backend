import os
from dotenv import load_dotenv

load_dotenv(override=True)

SECRET_KEY = str(os.getenv('SECRET_KEY'))
AMADEUS_API_KEY = str(os.getenv('AMADEUS_API_KEY'))
SQLALCHEMY_DATABASE_URL = str(os.getenv('SQLALCHEMY_DATABASE_URL'))
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 180