# -----------------------------------------------------------------------------------------
# PostgreSQL & Python 연동
# -----------------------------------------------------------------------------------------
# 모듈 로딩
import sys
import psycopg2
import pandas as pd
from datetime import datetime
# -----------------------------------------------------------------------------------------
# PostgreSQL 접속값
conn_params={'host':'localhost',
             'dbname':'steelcut',
            'port':5432,
            'user':'postgres',
            'password':'root'
            }

#---------------------------------------------------------------------------------------------------------------------
# 환율 최신정보 갱신

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
    try:
        time.sleep(1.5+random.random())
        url = f'https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{code}&page=1'

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
        print(f'{col} 크롤링 중 오류가 발생하였습니다.')
        break
    # print(values)
    # print(values)
    all_values.append(values)
df = pd.DataFrame({'date':dates,'dollar':all_values[0],'yen':all_values[1],'euro':all_values[2],'yuan':all_values[3]})
df['date']=pd.to_datetime(df['date'])
print(df)

# DB에 저장
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()
df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO exchange_rate VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]},\
                    {df.iloc[i,4]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4])

    except:
        continue
#---------------------------------------------------------------------------------------------------------------------
# 금 최신정보 갱신

result_df=pd.DataFrame(columns=['date','gold'])
try:
    time.sleep(1.5+random.random())
    url = f'https://finance.naver.com/marketindex/goldDailyQuote.naver?&page=1'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dates = []
    date_ = soup.find_all('td', class_='date')
    for d in date_:
        dates.append(d.get_text(strip=True))

    value = []
    value_ = soup.find_all('td', class_='num')
    for v in value_:
        value.append(v.get_text(strip=True))

    values = []
    for a in range(0,len(value),2):
        values.append(float(value[a].replace(',','')))
    values
except:
    print('금시세 크롤링 중 오류가 발생하였습니다.')

df = pd.DataFrame({'date':dates,'gold':values})
print(df)

# DB에 저장
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO gold_price VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1])

    except:
        continue
#---------------------------------------------------------------------------------------------------------------------
# 유가(두바이) 갱신

all_values=[]

values = []
dates = []

try:
    time.sleep(1.5+random.random())
    url = f'https://finance.naver.com/marketindex/worldDailyQuote.naver?fdtc=2&marketindexCd=OIL_DU&page=1'

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
    print('유가(두바이) 크롤링 중 오류가 발생하였습니다.')

all_values.append(values)
df = pd.DataFrame({'date':dates,'oil_price':all_values[0]})
df['date']=pd.to_datetime(df['date'])
print(df)
# DB에 저장
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO oil_price VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1])

    except:
        continue

#---------------------------------------------------------------------------------------------------------------------
# 비철금속 갱신

code_dict={'CDY':'copper', 'PDY':'plumbum', 'ZDY':'zinc', 'NDY':'nickel', 'AAY':'aluminum_alloy', 'SDY':'stannum'}

all_values=[]

for code,col in code_dict.items():
    values = []
    dates = []
    cnt=1
    while True:
        try:
            time.sleep(1+random.random())
            url = f'https://finance.naver.com/marketindex/worldDailyQuote.naver?fdtc=2&marketindexCd=CMDT_{code}&page=1'

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

            for a in range(0,len(value),3):
                values.append(float(value[a].replace(',','')))
            values

        except:
            print(f'{col} 크롤링 중 오류가 발생하였습니다.')
            break

        df = pd.DataFrame({'date':dates,col:values})
        print(df)
        nonferrous_metal_pathlist=['copper','plumbum','zinc','nickel','aluminum_alloy','stannum']

        connection = psycopg2.connect(**conn_params)
        cur = connection.cursor()

        df=df.drop_duplicates(subset='date')
        for i in range(0,len(df)):
            try:
                cur.execute(f"INSERT INTO {col} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
                connection.commit()
                print(df.iloc[i,0],df.iloc[i,1])

            except:
                continue
            
        if cnt==1:
                break