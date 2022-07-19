from bs4 import *
import requests

evo24hs=[]
names=[]
prices=[]
html_text=requests.get('https://coinmarketcap.com/').text

# soup=BeautifulSoup(html_text,'lxml')
soup=BeautifulSoup(html_text,'html.parser')

cryptocurrencies_names=soup.find_all('div',class_="sc-16r8icm-0 sc-1teo54s-0 dBKWCw")
cryptocurrencies_names2=soup.find_all('div',class_="sc-16r8icm-0 sc-1teo54s-1 dNOTPP")
cryptocurrencies_prices=soup.find_all('div',class_="sc-131di3y-0 cLgOOr")
cryptocurrencies_evo24h=soup.find_all("span",class_="sc-15yy2pl-0 feeyND")
bb=soup.find('Bitcoin')
print(bb)
for currency in cryptocurrencies_evo24h:
    try:    
        
        evo24h=currency.find("span",class_="sc-15yy2pl-0 hzgCfk").text
        evo24hs.append(evo24h)
    except :
        print(evo24hs)



# for currency in cryptocurrencies_evo24h:
#     try:
#         evo24h = currency.find('span',class_="sc-15yy2pl-0 hzgCfk").text
#         evo24hs.append(evo24h)
#     except AttributeError:
#         continue
        

for currency in cryptocurrencies_names:
    try:
        name = currency.find('p',class_="sc-1eb5slv-0 iworPT").text
        names.append(name)
    except AttributeError:
        continue

# for currency in cryptocurrencies_names2:
#     try:
#         name = currency.find('p',class_="sc-1eb5slv-0 iworPT").text
#         if name not in names:
#             names.append(name)
    except AttributeError:
        continue
        
for currency in cryptocurrencies_prices:
    try:
        price=currency.find('span').text
        prices.append(price)
    except AttributeError: 
        continue 
print(prices)
print(names)
print(evo24hs)