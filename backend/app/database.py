import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Читаем .env и делаем переменные доступными через os.getenv
load_dotenv()

# Достаём строку подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# ENGINE — постоянная связь с базой, создаётся один раз на приложение
engine = create_engine(DATABASE_URL)

# Фабрика сессий: SessionLocal() будет штамповать сессии для каждой операции
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех будущих моделей (таблиц)
Base = declarative_base()