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
      
