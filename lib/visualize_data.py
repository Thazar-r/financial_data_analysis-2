import matplotlib.pyplot as plt
from models.database import session
from models.stock import Stock

def visualize_stock_prices():
    # Fetch all stock records from the database
    stocks = session.query(Stock).all()
    
    # Extract tickers and close prices
    tickers = [stock.ticker for stock in stocks]
    close_prices = [
        stock.close if hasattr(stock, 'close') else stock.close_price
        for stock in stocks
    ]
    
    # Create the bar chart
    plt.figure(figsize=(10, 6))  # Adjust figure size
    plt.bar(tickers, close_prices, color='skyblue')
    plt.xlabel('Stock Ticker', fontsize=12)
    plt.ylabel('Close Price', fontsize=12)
    plt.title('Stock Prices', fontsize=14)
    
    # Rotate x-ticks for better readability
    plt.xticks(rotation=45)
    
    # Add a grid for easier readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Display the plot
    plt.tight_layout()  # Adjust layout to fit everything
    plt.show()

# Call the function to visualize
visualize_stock_prices()
