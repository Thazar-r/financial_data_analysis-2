from sqlalchemy import Column, Integer, String, Float, Date
from . import Base

class MarketIndex(Base):
    __tablename__ = 'market_indices'

    id = Column(Integer, primary_key=True)
    index_name = Column(String)
    date = Column(Date)
    value = Column(Float)

    @classmethod
    def create(cls, session, **kwargs):
        index = cls(**kwargs)
        session.add(index)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
