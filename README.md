# DataSciencePortfolio
1. Yahoo Finance Stock Price scrapper
   This is a simple web scrapping project . I have scrapped Yahoo Finance website with few selective stocks for their current value and change in stock price.
   - For implementing this code first do -pip install bs4,requests.
   - You can get your user agent by going to incognito mode and type 'my user agent'.
   - Paste the same in the headers.
   - I have used requests.get for scrapping information from the site.
     After scrapping for required stocks , the data is written into a json file.

     SOME TROUBLE SHOOTING STEPS :
     - Check whether the site that you are scrapping is successfully accessible using r.status_code
     - If you get '200' then it is success . Other status codes are '403' , '404'
     - If you get '403' the it is forbidden and you have not added headers or faulty headers while getting the requests .
     - If '404' then it is 'Page not found' . Please check the url that you have passed for scrapping.

2. Stock Data Pipeline: Yahoo Finance to MySQL                                                                                                                             
This Python script is designed to fetch daily historical stock data from Yahoo Finance using the yfinance library and store it in a MySQL database. The script performs the following steps:

     1.	Data Extraction: 
          -	Utilizes the yfinance library to fetch historical stock data for a specified symbol.
     2.	Data Loading:
          -	Inserts the fetched data into a MySQL database named "stock_app" in a table called "stock_data."
       	
Prerequisites :

Before running the script, ensure you have the following prerequisites:
-	Python installed (version 3.6 or higher)
-	yfinance library installed (pip install yfinance)
-	mysql-connector-python library installed (pip install mysql-connector-python)

Configuration :

    1.	Replace the placeholder values in the script with your MySQL credentials:
    
         pythonCopy code

         mysql_credentials = { "host": "localhost", "database": "stock_app", "user": "your_username", "password": "your_password", } 

    2.	Set the desired stock symbol in the script:
    
         pythonCopy code
         
         stock_symbol = "AAPL" 
         
Running the Script :

- Execute the script by running the following command in the terminal or command prompt:
bashCopy code --->     
python script_name.py 

- Make sure to replace "script_name.py" with the actual name of your Python script.

Output :
The script will output messages indicating the progress and status of data fetching and insertion. If successful, it will print

 "Data inserted successfully."

 3. Stock Data Visualization
Description:
    
This Python script interacts with Yahoo Finance and MySQL to fetch historical stock data, store it in a database, and generate individual plots for the closing prices of multiple stocks. The data is fetched from Yahoo Finance using the yfinance library, and the stock data is stored in a MySQL database. The generated plots are saved as separate images for each stock.

Usage:

- Install Required Libraries:
- Ensure that you have the required Python libraries installed. You can install them using the following command:
Copy code :
         pip install yfinance mysql-connector-python pandas matplotlib
  
MySQL Database Setup:
   
-	Set up a MySQL database named stock_app.
-	Replace the placeholder values <db_username> and <db_password> in the script with your actual MySQL credentials.

Excel File:
-	Create an Excel file named stocks.xlsx with a column named "Symbol" containing the stock symbols you want to analyze.
  
Run the Script:
-	Execute the script using the following command:
Copy code :
         python script_name.py

-	Replace script_name.py with the actual filename of your Python script.
  
Troubleshooting:
-	If you encounter MySQL connection issues, verify that your MySQL server is running, and your credentials are correct.
-	Ensure that the required Python libraries are installed. Use the pip install command mentioned in step 1 to install any missing libraries.
-	Check for typos or formatting issues in your Excel file.
  
Note:
-  The script saves individual stock plots with filenames in the format <symbol>_plot.png in the current working directory.
-	Adjust the MySQL and Excel file details as needed.
-	Make sure to comply with Yahoo Finance's terms of service when using their data.



    
