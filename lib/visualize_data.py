import matplotlib.pyplot as plt
from models.database import session
from models.stock import Stock

def visualize_stock_prices():
    stocks = session.query(Stock).all()
    
    tickers = [stock.ticker for stock in stocks]
    close_prices = [stock.close if hasattr(stock, 'close') else stock.close_price for stock in stocks]
    
    plt.bar(tickers, close_prices)
    plt.xlabel('Stock Ticker')
    plt.ylabel('Close Price')
    plt.title('Stock Prices')
    plt.show()


if __name__ == "__main__":
    visualize_stock_prices()
