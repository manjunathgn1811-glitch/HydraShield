import os

class Config:
    SECRET_KEY = "hydrashield-secret-key"

    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "hydrashield"
    DB_USER = "postgres"
    DB_PASSWORD = "postgres"

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    LOG_DIR = "logs"