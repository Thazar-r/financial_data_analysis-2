from sqlalchemy import Column, String, Float, Date
from sqlalchemy.orm import relationship
from . import Base

class Stock(Base):
    __tablename__ = 'stocks'
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    open_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

    @classmethod
    def create(cls, session, **kwargs):
        stock = cls(**kwargs)
        session.add(stock)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def delete(cls, session, stock_id):
        stock = session.query(cls).get(stock_id)
        if stock:
            session.delete(stock)
            session.commit()
