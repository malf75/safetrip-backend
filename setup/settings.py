import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 180