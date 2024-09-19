# lib/view_data.py

from models.database import session  # Import the session object
from models.stock import Stock
from models.financial_statement import FinancialStatement
from models.market_index import MarketIndex
from models.user_portfolio import UserPortfolio

def view_data():
    # Query and print stocks
    stocks = session.query(Stock).all()
    print("Stocks:")
    for stock in stocks:
        print(f"Ticker: {stock.ticker}, Date: {stock.date}, Close Price: {stock.close_price}")

    # Query and print financial statements
    financials = session.query(FinancialStatement).all()
    print("\nFinancial Statements:")
    for financial in financials:
        print(f"Company ID: {financial.company_id}, Date: {financial.date}, Revenue: {financial.revenue}")

    # Query and print market indices
    indices = session.query(MarketIndex).all()
    print("\nMarket Indices:")
    for index in indices:
        print(f"Index Name: {index.index_name}, Date: {index.date}, Value: {index.value}")

    # Query and print user portfolios
    portfolios = session.query(UserPortfolio).all()
    print("\nUser Portfolios:")
    for portfolio in portfolios:
        print(f"User ID: {portfolio.user_id}, Ticker: {portfolio.ticker}, Shares: {portfolio.shares}")

if __name__ == "__main__":
    view_data()
