import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd
from models.stock import Stock
from models.financial_statement import FinancialStatement
from models.market_index import MarketIndex
from models.user_portfolio import UserPortfolio

DATABASE_URL = "sqlite:///financial_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def exit_program():
    print("Goodbye!")
    exit()

def display_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Manage Stocks")
    print("2. Manage Portfolios")

def fetch_stock_data(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=IJSAZWNGBKF1DBOY"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("Time Series (Daily)", {})
    else:
        print(f"Error fetching data: {response.status_code}")
        return {}

def handle_stock_commands():
    session = Session()
    while True:
        print("1. Add Stock")
        print("2. View All Stocks")
        print("3. Delete Stock")
        print("0. Return to Main Menu")
        choice = input("> ")
        
        if choice == "1":
            ticker = input("Enter stock ticker: ").strip().upper()
            stock_data = fetch_stock_data(ticker)
            if stock_data:
                # Assume you save the necessary data to Stock model
                Stock.create(session, ticker=ticker, date=..., open_price=..., close_price=..., high=..., low=..., volume=...)
                print(f"Added stock {ticker}.")
            else:
                print("Failed to fetch stock data.")
        
        elif choice == "2":
            stocks = Stock.get_all(session)
            for stock in stocks:
                print(f"{stock.ticker} - {stock.date} - Close: {stock.close_price}")
        
        elif choice == "3":
            stock_id = input("Enter stock ID to delete: ")
            Stock.delete(session, stock_id)
            print(f"Deleted stock ID {stock_id}.")
        
        elif choice == "0":
            break

    session.close()

def plot_stock_data(stock_data):
    df = pd.DataFrame(stock_data).T
    df.index = pd.to_datetime(df.index)
    df['close'] = df['4. close'].astype(float)
    df['close'].plot(title='Stock Price Trend', ylabel='Price', xlabel='Date')
    plt.show()
