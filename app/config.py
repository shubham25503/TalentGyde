import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MODEL_NAME = os.getenv("MODEL")

settings = Settings()
