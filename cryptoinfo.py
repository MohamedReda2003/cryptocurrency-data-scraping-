import pandas as pd
from bs4 import *
import requests
import datetime
from datetime import datetime,date
import  matplotlib
from matplotlib import pyplot as plt
import streamlit as st
import time 
import random
t1=time.time()
def initial():
    names=[]
    prices=[]
    rprices=[]
    
    html_text=requests.get('https://coinmarketcap.com/').text
    soup=BeautifulSoup(html_text,'lxml')
    
    cryptocurrencies_names=soup.find_all('div',class_="sc-16r8icm-0 sc-1teo54s-0 dBKWCw")
    cryptocurrencies_prices=soup.find_all('div',class_="sc-131di3y-0 cLgOOr")
    
    for currency in cryptocurrencies_names:
        try:
            name = currency.find('p',class_="sc-1eb5slv-0 iworPT").text
            names.append(name)
        except AttributeError:
            continue
    
    for currency in cryptocurrencies_prices:
        try:
            price=currency.find('span').text
            prices.append(price)
        except AttributeError: 
            continue 
        
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today= date.today()
    today=today.strftime("%d/%m/%Y")
    for price in prices:
        price =price[1:]
        price =price.replace(',','')
        price =float(price)
        rprices.append(price)
        

    
    
    # data=pd.DataFrame([rprices], columns=names)
    
    # data.index=[f'PRICES IN $ at {current_time} on {today}']
    data =pd.DataFrame({'NAMES':names,f'PRICES IN $ at {current_time} on {today}':rprices})
    data.to_csv('Cryptocurrencyinfo.csv' )
    # data.to_excel(writer,sheet_name='sheet1')
    # writer.save()
    return data
    
def second():
    prices2=[]
    rprices2=[]
    html_text=requests.get('https://coinmarketcap.com/').text
    soup=BeautifulSoup(html_text,'lxml')
    
    cryptocurrencies_prices=soup.find_all('div',class_="sc-131di3y-0 cLgOOr")
    
    for currency in cryptocurrencies_prices:
        try:
            price=currency.find('span').text
            prices2.append(price)
        except AttributeError: 
            continue 
        
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    tday= date.today()
    tday=tday.strftime("%d/%m/%Y")
    for price in prices2:
        price =price[1:]
        price =price.replace(',','')
        price =float(price)
        rprices2.append(price)
    print(rprices2)
    df = pd.read_csv('Cryptocurrencyinfo.csv')
    df=pd.DataFrame(df)
    for column in df.columns:
        if 'Unnamed' in column:
            del df[column]
    
    df[f'PRICES IN $ at {current} on {tday}']=rprices2
    
    # rprices2.insert(0,1)
    # print(rprices2[:len(rprices2)])
    # df=pd.DataFrame(df)
    # df = df.append(pd.Series(rprices2, index=df.columns[:len(rprices2)]), ignore_index=True)
    
    
    for column in df.columns:
        try:
            if "Unnamed" in column:
                del df[column]
        except :
            continue
    print(df)
    df.to_csv('Cryptocurrencyinfo.csv')
    dates=[]
    ss=[]
    for column in df.columns :
        try:
            if ":" not in column:
                continue
            if 'on'in column:
                column=column.replace('on','')
        except :
            continue
        column=column[15:]
        date_time_str = column
        date_time_obj = datetime.strptime(date_time_str,'%H:%M:%S %d/%m/%Y')
        dates.append(date_time_str)
        ss.append(column)
        
        
    data=pd.read_csv('Cryptocurrencyinfo.csv')
    print(len(data.index))
    print(data.index[len(data.index)-1])
    names=[]
    for name in data['NAMES']:
            names.append(name)
    # data.index[1]=[f'PRICES IN $ at {current} on {tday}']
    data.to_csv('Cryptocurrencyinfo.csv')
    # data.plot()
    # for i in range (len(data.index)):
    #     data.plot(names[i],rprices2[i])
    #     plt.show()
    del data['NAMES']
    figure, axis = plt.subplots(3,4)
    h=0
    c=0
    for index,row in data.iterrows():
                    plt.title(names[index])
                    plt.xlabel("Time")
                    plt.ylabel("Price")
            # plt.plot(row)
                    
                    axis[h,c].plot(row)
                    axis[h,c].set_title(names[index])
                    h+=1
                    if h==3:
                        h=0
                        c+=1
    #plt.pause(30)
    #plt.close()
    # t2=time.time() 
    # print(t2-t1)
    
    
    plt.show()
    
    time.sleep(60)
    
    return data
def principe():    
    try:
        while True:
            
            data=second()
            
        # names=[]
        # for name in data.columns:
        #     names.append(name)
            
        # print(names)
        # del data['NAMES']
        # print(data)    
        
      
        
        # for index,row in data.iterrows():
        #     # plt.title(names[index])
        #     # plt.xlabel("Time")
        #     # plt.ylabel("Price")
        #     # plt.plot(row)
        #     # plt.show()
        #     st.line_chart(row)
    except FileNotFoundError:
        data=initial()
        
        #print(dt)
    
            
        # print(names)
        # del data['NAMES']
    print(data)
        # print(data)    
    
    
   
      
    
    
        #     #st.line_chart(row,width=10, height=40)
        #     line_chart = alt.Chart(row).mark_line(interpolate='basis').encode(
        #         alt.X('x', title='TIME'),
        #         alt.Y('y', title='PRICE'),
        #         color='category:N'
        #     ).properties(
        #         title=names[index]
        #     )
            
        #     st.altair_chart(line_chart,width=1,height=20)

  
principe()
  
# def main():
#         st.set_page_config(page_title="Cryptocurrency evolution", layout="wide")
#         st.title("My streamlit website")
#         if int(time.strftime('%H'))<15:
#             st.header("Good Morning")
#         elif int(time.strftime('%H'))>=15:
#             st.header("Good Evening")
            
#         principe()


# if __name__ == "__main__":
#     main()


    