from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


URI = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'

engine = create_engine(URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_session():
    """Менеджер контексту для автоматичного закриття сесії"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()