from models import Stock, FinancialStatement, MarketIndex, UserPortfolio
from models.database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///financial_data.db"  # Adjust if using a different database

def initialize_database():
    # Create an engine
    engine = create_engine(DATABASE_URL)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    print("Database initialized and tables created.")
    return session

if __name__ == "__main__":
    initialize_database()
