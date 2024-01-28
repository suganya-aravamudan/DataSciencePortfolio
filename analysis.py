import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
import pandas as pd

def fetch_stock_prices(symbol):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="stock_app",
            user="student",
            password="student",
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT date, close FROM stock_data WHERE symbol = '{symbol}'")
            data = cursor.fetchall()
            cursor.close()
            connection.close()
            return data
    except Error as e:
        print("Error: ", e)

def plot_stock_prices(data, symbol):
    dates = [entry['date'] for entry in data]
    prices = [entry['close'] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, label=f'{symbol} Closing Prices')
    plt.title(f'{symbol} Closing Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    
    # Save the plot as a separate image for each stock
    plt.savefig(f'{symbol}_plot.png')
    plt.close()  # Close the current plot to start a new one

def main():
    # Replace with your MySQL credentials
    mysql_credentials = {
        "host": "localhost",
        "database": "stock_app",
        "user": "student",
        "password": "student",
    }

    # Replace with the path to your Excel file
    excel_file_path = "stocks.xlsx"

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**mysql_credentials)
        if connection.is_connected():
            cursor = connection.cursor()

            # Read stock symbols from Excel
            stock_symbols_df = pd.read_excel(excel_file_path)
            stock_symbols = stock_symbols_df['Symbol'].tolist()

            for stock_symbol in stock_symbols:
                # Fetch stock data
                stock_prices = fetch_stock_prices(stock_symbol)

                if stock_prices:
                    # Plot stock prices and save as a separate image
                    plot_stock_prices(stock_prices, stock_symbol)
                else:
                    print(f"No data available for plotting {stock_symbol}.")

            cursor.close()
            connection.close()

    except Error as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
