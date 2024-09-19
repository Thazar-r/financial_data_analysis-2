from sqlalchemy import Column, Integer, String, Date
from . import Base

class UserPortfolio(Base):
    __tablename__ = 'user_portfolios'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    ticker = Column(String, nullable=False)
    shares = Column(Integer, nullable=False)
    purchase_date = Column(Date, nullable=False)

    @classmethod
    def create(cls, session, **kwargs):
        portfolio = cls(**kwargs)
        session.add(portfolio)
        session.commit()
