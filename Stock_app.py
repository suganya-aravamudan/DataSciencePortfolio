import yfinance as yf
import mysql.connector
from mysql.connector import Error

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')  # Fetch daily historical data for the last trading day

    return data

def insert_stock_data(data, symbol, cursor):
    try:
        for index, row in data.iterrows():
            cursor.execute("""
                INSERT INTO stock_data (symbol, date, open, high, low, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                symbol,
                index.strftime('%Y-%m-%d'),
                row['Open'],
                row['High'],
                row['Low'],
                row['Close'],
                row['Volume']
            ))
        print("Data inserted successfully")
    except Error as e:
        print("Error while inserting data into table")
        print(e)

def main():
    # Replace with your MySQL credentials
    mysql_credentials = {
        "host": "localhost",
        "database": "stock_app",
        "user": <db_username>,
        "password": <db_password>,
    }

    # Replace with the desired stock symbol
    stock_symbol = "AAPL"

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(**mysql_credentials)
        conn.autocommit = True
        cursor = conn.cursor()

        # Create stock_data table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                symbol VARCHAR(10),
                date DATE,
                open DOUBLE,
                high DOUBLE,
                low DOUBLE,
                close DOUBLE,
                volume DOUBLE
            )
        """)

        # Fetch stock data
        stock_data = fetch_stock_data(stock_symbol)

        # Insert data into MySQL table
        insert_stock_data(stock_data, stock_symbol, cursor)

    except Error as e:
        print("Error: ", e)

    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
