from sqlmodel import Session, create_engine
DATABASE_URL = "postgresql+psycopg://postgres:menta0805@localhost:5432/Miniproyecto"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session