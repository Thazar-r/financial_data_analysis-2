from datetime import datetime
from models import Stock, FinancialStatement, MarketIndex, UserPortfolio
from models.database import session

def clear_existing_data():
    """Clear existing data from the database."""
    session.query(Stock).delete()
    session.query(FinancialStatement).delete()
    session.query(MarketIndex).delete()
    session.query(UserPortfolio).delete()
    session.commit()
    print("Existing data cleared.")

def insert_sample_data():
    """Insert sample data into the database."""
    # Sample data for stocks
    stocks = [
        Stock(ticker='AAPL', date=datetime(2023, 9, 18), open_price=150.0, close_price=152.0, high_price=153.0, low_price=149.0, volume=100000),
        Stock(ticker='GOOGL', date=datetime(2023, 9, 18), open_price=2800.0, close_price=2825.0, high_price=2830.0, low_price=2790.0, volume=50000),
        Stock(ticker='AMZN', date=datetime(2023, 9, 18), open_price=3300.0, close_price=3350.0, high_price=3360.0, low_price=3280.0, volume=70000),
        Stock(ticker='MSFT', date=datetime(2023, 9, 18), open_price=300.0, close_price=305.0, high_price=307.0, low_price=298.0, volume=80000),
        Stock(ticker='TSLA', date=datetime(2023, 9, 18), open_price=800.0, close_price=820.0, high_price=825.0, low_price=790.0, volume=120000),
        Stock(ticker='NFLX', date=datetime(2023, 9, 18), open_price=500.0, close_price=510.0, high_price=515.0, low_price=495.0, volume=60000),
        Stock(ticker='FB', date=datetime(2023, 9, 18), open_price=350.0, close_price=355.0, high_price=357.0, low_price=345.0, volume=75000),
        Stock(ticker='NVDA', date=datetime(2023, 9, 18), open_price=200.0, close_price=205.0, high_price=207.0, low_price=198.0, volume=90000),
        Stock(ticker='CSCO', date=datetime(2023, 9, 18), open_price=55.0, close_price=57.0, high_price=58.0, low_price=54.0, volume=40000),
        Stock(ticker='ADBE', date=datetime(2023, 9, 18), open_price=500.0, close_price=510.0, high_price=512.0, low_price=495.0, volume=65000),
        Stock(ticker='ORCL', date=datetime(2023, 9, 18), open_price=90.0, close_price=92.0, high_price=93.0, low_price=89.0, volume=30000),
    ]

    # Sample data for financial statements
    financial_statements = [
        FinancialStatement(company_id=1, date=datetime(2023, 9, 19), revenue=100000, profit=50000, expenses=30000),  # AAPL
        FinancialStatement(company_id=2, date=datetime(2023, 9, 19), revenue=200000, profit=120000, expenses=80000),  # GOOGL
        FinancialStatement(company_id=3, date=datetime(2023, 9, 19), revenue=150000, profit=75000, expenses=45000),  # AMZN
        FinancialStatement(company_id=4, date=datetime(2023, 9, 19), revenue=180000, profit=90000, expenses=60000),  # MSFT
        FinancialStatement(company_id=5, date=datetime(2023, 9, 19), revenue=220000, profit=110000, expenses=70000),  # TSLA
        FinancialStatement(company_id=6, date=datetime(2023, 9, 19), revenue=80000, profit=40000, expenses=25000),   # NFLX
        FinancialStatement(company_id=7, date=datetime(2023, 9, 19), revenue=90000, profit=45000, expenses=30000),   # FB
        FinancialStatement(company_id=8, date=datetime(2023, 9, 19), revenue=130000, profit=65000, expenses=40000),  # NVDA
        FinancialStatement(company_id=9, date=datetime(2023, 9, 19), revenue=110000, profit=55000, expenses=35000),  # CSCO
        FinancialStatement(company_id=10, date=datetime(2023, 9, 19), revenue=95000, profit=48000, expenses=25000),   # ADBE
        FinancialStatement(company_id=11, date=datetime(2023, 9, 19), revenue=88000, profit=44000, expenses=30000),   # ORCL
    ]

    # Sample data for market indices
    market_indices = [
        MarketIndex(index_name='S&P 500', date=datetime(2023, 9, 18), value=4400.0),
        MarketIndex(index_name='NASDAQ', date=datetime(2023, 9, 18), value=15000.0),
        MarketIndex(index_name='DOW JONES', date=datetime(2023, 9, 18), value=34000.0),
    ]

    # Sample data for user portfolios
    user_portfolios = [
        UserPortfolio(user_id=1, ticker='AAPL', shares=10, purchase_date=datetime(2023, 9, 1)),
        UserPortfolio(user_id=1, ticker='GOOGL', shares=5, purchase_date=datetime(2023, 9, 5)),
        UserPortfolio(user_id=1, ticker='AMZN', shares=2, purchase_date=datetime(2023, 9, 10)),
        UserPortfolio(user_id=1, ticker='MSFT', shares=7, purchase_date=datetime(2023, 9, 12)),
        UserPortfolio(user_id=1, ticker='TSLA', shares=4, purchase_date=datetime(2023, 9, 15)),
        UserPortfolio(user_id=1, ticker='NFLX', shares=3, purchase_date=datetime(2023, 9, 17)),
        UserPortfolio(user_id=1, ticker='FB', shares=6, purchase_date=datetime(2023, 9, 20)),
        UserPortfolio(user_id=1, ticker='NVDA', shares=5, purchase_date=datetime(2023, 9, 21)),
        UserPortfolio(user_id=1, ticker='CSCO', shares=10, purchase_date=datetime(2023, 9, 22)),
        UserPortfolio(user_id=1, ticker='ADBE', shares=8, purchase_date=datetime(2023, 9, 23)),
        UserPortfolio(user_id=1, ticker='ORCL', shares=12, purchase_date=datetime(2023, 9, 24)),
    ]

    try:
        # Add and commit data to the session
        session.add_all(stocks)
        session.add_all(financial_statements)
        session.add_all(market_indices)
        session.add_all(user_portfolios)
        
        session.commit()
        print("Sample data inserted successfully!")
    
    except Exception as e:
        session.rollback()  # Roll back changes if any error occurs
        print(f"Error inserting sample data: {e}")

if __name__ == "__main__":
    clear_existing_data()  # Clear data first
    insert_sample_data()  # Then insert new data
