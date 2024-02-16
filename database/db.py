from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, declared_attr

from config import DATA_BASE, DATA_BASE_FRAMEWORK, USER_NAME, USER_PASSWORD, URL, PORT, DB_NAME

DB_CONNECT = f"{DATA_BASE}://{USER_NAME}:{USER_PASSWORD}@{URL}:{PORT}/{DB_NAME}"

engine = create_engine(
    DB_CONNECT,
    # connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    __absctract__ = True

    @declared_attr.directive
    def __table_name__(cls) -> str:
        return f"{cls.__name__.lower}s"

    id: Mapped = mapped_column(primary_key=True)


def get_db():
    """DB connect"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
