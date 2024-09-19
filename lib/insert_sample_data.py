from datetime import datetime
from models import Stock, FinancialStatement, MarketIndex, UserPortfolio
from models.database import session

def insert_sample_data():
    # Sample data for stocks
    stocks = [
        Stock(ticker='AAPL', date=datetime(2023, 9, 18), open_price=150.0, close_price=152.0, high_price=153.0, low_price=149.0, volume=100000),
        Stock(ticker='GOOGL', date=datetime(2023, 9, 18), open_price=2800.0, close_price=2825.0, high_price=2830.0, low_price=2790.0, volume=50000),
    ]

    # Sample data for financial statements
    financial_statements = [
        FinancialStatement(company_id=1, date=datetime(2023, 9, 19), revenue=100000, profit=50000, expenses=30000),
        FinancialStatement(company_id=2, date=datetime(2023, 9, 19), revenue=200000, profit=120000, expenses=80000),
    ]

    # Sample data for market indices
    market_indices = [
        MarketIndex(index_name='S&P 500', date=datetime(2023, 9, 18), value=4400.0),
    ]

    # Sample data for user portfolios
    user_portfolios = [
        UserPortfolio(user_id=1, ticker='AAPL', shares=10, purchase_date=datetime(2023, 9, 1)),
    ]

    # Add and commit data to the session
    session.add_all(stocks)
    session.add_all(financial_statements)
    session.add_all(market_indices)
    session.add_all(user_portfolios)
    
    session.commit()
    print("Sample data inserted successfully!")

if __name__ == "__main__":
    insert_sample_data()
