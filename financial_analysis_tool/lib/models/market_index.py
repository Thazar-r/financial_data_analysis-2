from sqlalchemy import Column, Integer, String, Float, Date
from . import Base

class MarketIndex(Base):
    __tablename__ = 'market_indices'
    
    id = Column(Integer, primary_key=True)
    index_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)

    @classmethod
    def create(cls, session, **kwargs):
        index = cls(**kwargs)
        session.add(index)
        session.commit()
