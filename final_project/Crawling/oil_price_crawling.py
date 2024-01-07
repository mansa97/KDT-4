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

values = []
dates = []
for i in tqdm(range(627)):
    try:
        time.sleep(1.5+random.random())
        url = f'https://finance.naver.com/marketindex/worldDailyQuote.naver?fdtc=2&marketindexCd=OIL_DU&page={i+1}'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        date_ = soup.find_all('td', class_='date')
        # print(date_)
        for d in date_:
            dates.append(d.get_text(strip=True))

        value = []
        value_ = soup.find_all('td', class_='num')

        for v in value_:
            # print(v.get_text(strip=True))
            value.append(v.get_text(strip=True))

        for a in range(0,len(value),3):
            values.append(float(value[a].replace(',','')))
        values

        # df = pd.DataFrame({'date':dates,'gold':values})
        # result_df = pd.concat([result_df,df], ignore_index=True)
    
    except:
        break
    # print(values)
    # print(values)
all_values.append(values)
df = pd.DataFrame({'date':dates,'oil_price':all_values[0]})
df['date']=pd.to_datetime(df['date'])
df.to_csv('./data/oil_price.csv',index=False)
