from sqlalchemy import Column, Integer, Float, Date
from . import Base

class FinancialStatement(Base):
    __tablename__ = 'financial_statements'
    
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    revenue = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)
    expenses = Column(Float, nullable=False)

    @classmethod
    def create(cls, session, **kwargs):
        statement = cls(**kwargs)
        session.add(statement)
        session.commit()
