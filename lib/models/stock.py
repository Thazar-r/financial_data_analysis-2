from .database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True)
    date = Column(Date)
    open_price = Column(Float)
    close_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    volume = Column(Integer)

    @classmethod
    def create(cls, session, **kwargs):
        stock = cls(**kwargs)
        session.add(stock)
        session.commit()

    @classmethod
    def delete(cls, session, stock_id):
        stock = session.query(cls).get(stock_id)
        if stock:
            session.delete(stock)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
