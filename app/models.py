from sqlalchemy import Column, Integer, String
from db.database import Base, engine


class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True, index=True)
    club_name = Column(String, index=True)
    club_short_name = Column(String)


def create_database():
    Base.metadata.create_all(bind=engine)
