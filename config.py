import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# caminho absoluto para funcionar tambem no PythonAnywhere
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-de-desenvolvimento")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///hacknite.db")  # fica em instance/
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    LOG_DIR = os.path.join(BASE_DIR, "logs")
