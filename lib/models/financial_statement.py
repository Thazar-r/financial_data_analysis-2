from .database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class FinancialStatement(Base):
    __tablename__ = 'financial_statements'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    date = Column(Date)
    revenue = Column(Float)
    profit = Column(Float)
    expenses = Column(Float)

    @classmethod
    def create(cls, session, **kwargs):
        statement = cls(**kwargs)
        session.add(statement)
        session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
