import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Достаём строку подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# ENGINE — постоянная связь с базой, создаётся один раз на приложение
engine = create_engine(DATABASE_URL)

# Фабрика сессий: SessionLocal() будет штамповать сессии для каждой операции
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех будущих моделей (таблиц)
Base = declarative_base()


#уть yield: он отдаёт сессию эндпоинту 
# и "ставит функцию на паузу"; когда эндпоинт закончил — 
# управление возвращается сюда, в finally, 
# и сессия закрывается. 
# Гарантированно, даже при ошибке. Это конвейер 
# "открыл → поработал → закрыл", который FastAPI 
# прокрутит сам на каждый запрос.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
