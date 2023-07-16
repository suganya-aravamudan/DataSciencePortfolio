import requests
from bs4 import BeautifulSoup
import json

mystocks=['0MRI.IL','ICON.L','MNRG.L','MXC.L']
stockdata=[]
def getData(symbol):
    headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url= 'https://uk.finance.yahoo.com/quote/{symbol}'
    r=requests.get(url,headers=headers)
    # print(r.text)
    soup=BeautifulSoup(r.text,'html.parser')
    # stock = soup.find_all('div',{'class':'D(ib) Mend(20px)'})
    # stock=stock.find_all('fin-streamer')
    stock={
    'symbol':symbol,
    'price':soup.find('div').find_all('fin-streamer')[0].text,
    'change' : soup.find('div').find_all('fin-streamer')[1].text}
    
    return stock
for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ',item)
with open('stockdata.json','w') as f:
    json.dump(stockdata,f)
print('Fin.')