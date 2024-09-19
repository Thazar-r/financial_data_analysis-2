from models.database import session
from models.stock import Stock

def average_stock_price():
    stocks = session.query(Stock).all()
    total_price = sum(stock.close for stock in stocks)
    avg_price = total_price / len(stocks) if stocks else 0
    print(f'Average Stock Price: {avg_price}')

if __name__ == "__main__":
    average_stock_price()
