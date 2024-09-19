import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///financial_data.db")

def fetch_stock_data(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=IJSAZWNGBKF1DBOY"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("Time Series (Daily)", {})
        except ValueError:
            print("Error parsing JSON response.")
            return {}
    else:
        print(f"Error fetching data: {response.status_code}")
        return {}

def initialize_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()
