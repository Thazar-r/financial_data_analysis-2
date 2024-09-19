from flask import Flask, render_template
from lib.models.database import session  # Adjusted import
from lib.models.stock import Stock  # Adjusted import


app = Flask(__name__)

@app.route('/')
def index():
    stocks = session.query(Stock).all()
    return render_template('index.html', stocks=stocks)

if __name__ == '__main__':
    app.run(debug=True)
