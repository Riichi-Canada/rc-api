from sqlalchemy import Column, Integer, String, Numeric
from app.db.database import Base, engine


class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True, index=True)
    club_name = Column(String, index=True)
    club_short_name = Column(String)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    player_region = Column(Integer)
    player_club = Column(Integer)
    player_score_2025_cycle = Column(Numeric)
    player_score_2028_cycle = Column(Numeric)

class EventResult(Base):
    __tablename__ = 'event_results'

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer)
    player_id = Column(Integer)
    player_first_name = Column(String)
    player_last_name = Column(String)
    placement = Column(Integer)
    score = Column(Numeric)

# class PlayerScores2025(Base):
#     __tablename__ = 'player_scores_2025_cycle'
#
#     id = Column(Integer, primary_key=True, index=True)
#     player_id = Column(Integer)
#     total_score = Column(Numeric)
#     out_of_region_live = Column(Integer)
#     other_live_1 = Column(Integer)
#     other_live_2 = Column(Integer)
#     any_event_1 = Column(Integer)
#     any_event_2 = Column(Integer)
#     tank_1 = Column(Integer)
#     tank_2 = Column(Integer)
#     tank_3 = Column(Integer)
#     tank_4 = Column(Integer)
#     tank_5 = Column(Integer)


def create_database():
    Base.metadata.create_all(bind=engine)
