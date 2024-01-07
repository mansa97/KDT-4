import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from tqdm import tqdm

code_dict={'USDKRW':'dollar', 'JPYKRW':'yen', 'EURKRW':'euro', 'CNYKRW':'yuan'}
# for code,col in code.items():
#     print(code,col)

# result_df=pd.DataFrame(columns=['date','dollar','yen','euro','yuan'])
all_values=[]
for code,col in code_dict.items():
    values = []
    dates = []
    cnt = 1
    for i in tqdm(range(490)):
        try:
            time.sleep(1.5+random.random())
            url = f'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{code}&page={i+1}'

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            date_ = soup.find_all('td', class_='date')
            # print(date_)
            for d in date_:
                dates.append(d.get_text(strip=True))

            value = []
            value_ = soup.find_all('td', class_='num')
            for v in value_:
                value.append(v.get_text(strip=True))

            for a in range(0,len(value),2):
                values.append(float(value[a].replace(',','')))
            values
            # print(values)

            # df = pd.DataFrame({'date':dates,'gold':values})
            # result_df = pd.concat([result_df,df], ignore_index=True)
        
        except:
            break
        # print(values)
        # print(values)
    all_values.append(values)
df = pd.DataFrame({'date':dates,'dollar':all_values[0],'yen':all_values[1],'euro':all_values[2],'yuan':all_values[3]})
df['date']=pd.to_datetime(df['date'])
df.to_csv('./data/exchange_rate.csv',index=False)