## Overview

This project is designed for analyzing financial data, providing insights and visualizations to aid in decision-making. It includes functionalities for managing financial statements, stock data, market indices, and user portfolios.

## Features

- Data ingestion and processing
- Financial statement analysis
- Stock performance tracking
- Market index comparisons
- User portfolio management
- Database initialization and setup

## Directory Structure

├── Pipfile ├── Pipfile.lock ├── README.md ├── alembic │ ├── env.py │ ├── script.py.mako │ └── versions ├── lib │ ├── init.py │ ├── cli.py │ ├── debug.py │ ├── helpers.py │ ├── initialize_db.py │ └── models │ ├── init.py │ ├── stock.py │ ├── financial_statement.py │ ├── market_index.py │ ├── user_portfolio.py │ └── database.py └── .env

bash
Copy code

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Thazar-r/financial_data_analysis-2.git
   cd financial_data_analysis-2
or

bash
Copy code
git clone git@github.com:Thazar-r/financial_data_analysis-2.git
cd financial_data_analysis-2
Install the required packages:

bash
Copy code
pip install pipenv
pipenv install
Set up your environment variables by creating a .env file with the required configurations.

Usage
To initialize the database, run the following command:

bash
Copy code
python lib/initialize_db.py
You can use the CLI for various functionalities. For help, run:

bash
Copy code
python lib/cli.py --help
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

Fork the repository
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature-branch)
Open a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Pandas for data manipulation.
SQLAlchemy for database interactions.
