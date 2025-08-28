import os

from dotenv import load_dotenv
load_dotenv()  # carga variables desde .env

MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB = os.getenv("MYSQL_DB", "contacto_db")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")  # útil si luego usas CSRF/flash
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
