from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a Base class for declarative models
Base = declarative_base()

# Create an SQLite database (or connect to an existing one)
DATABASE_URL = "sqlite:///financial_data.db"
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# Create all tables
def initialize_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_db()
