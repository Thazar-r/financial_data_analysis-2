from sqlalchemy import Column, Integer, String, Date
from . import Base

class UserPortfolio(Base):
    __tablename__ = 'user_portfolios'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    ticker = Column(String)
    shares = Column(Integer)
    purchase_date = Column(Date)

    @classmethod
    def create(cls, session, **kwargs):
        portfolio = cls(**kwargs)
        session.add(portfolio)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
