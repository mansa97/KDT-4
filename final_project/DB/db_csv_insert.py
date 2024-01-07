# ----------------------------------------------------------------------------------------- 
# MariaDB & Python 연동
# ----------------------------------------------------------------------------------------- 
# 모듈 로딩
# import mariadb as mdb
import sys
import psycopg2
import pandas as pd
from datetime import datetime

# PostgreSQL 접속값
conn_params={'host':'localhost',
             'dbname':'steelcut',
            'port':5432,
            'user':'postgres',
            'password':'root'
            }
# ----------------------------------------------------------------------------------------- 
# 철스크랩 가격
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

# 기존 csv파일 불러와서 DB에 추가
# df=pd.read_csv('./data/선반.csv')
# df=df.drop_duplicates(subset='날짜')
steelfiles={'busheling':'./data/scrap/Busheling_price.csv','heavy_scrap':'./data/scrap/HeavyScrap_price.csv','light_scrap':'./data/scrap/LightScrap_price.csv','turning_scrap':'./data/scrap/TurningScrap_price.csv'}
print(steelfiles)
for filename, path in steelfiles.items():
    df=pd.read_csv(path)
    df=df.drop_duplicates(subset='날짜')
    print(len(df.columns))
    for i in range(0,len(df)):
        if len(df.columns)==7:
            try:
                cur.execute(f"INSERT INTO {filename} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]},\
                            {df.iloc[i,4]}, {df.iloc[i,5]}, {df.iloc[i,6]});")
                connection.commit()
                print(df.iloc[i,0])
            except:
                continue


        elif len(df.columns)==13:
            try:
                cur.execute(f"INSERT INTO {filename} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]}, {df.iloc[i,4]}, {df.iloc[i,5]}, {df.iloc[i,6]},\
                        {df.iloc[i,7]}, {df.iloc[i,8]}, {df.iloc[i,9]}, {df.iloc[i,10]}, {df.iloc[i,11]}, {df.iloc[i,12]});"
                        )
                connection.commit()
                print(df.iloc[i,0])
            except:
                continue

# ----------------------------------------------------------------------------------------- 
# 환율
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

exchange_files='./data/feature/exchange_rate.csv'
print(exchange_files)
df=pd.read_csv(exchange_files)
df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO exchange_rate VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]},\
                    {df.iloc[i,4]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1],df.iloc[i,2],df.iloc[i,3],df.iloc[i,4])

    except:
        continue
# ----------------------------------------------------------------------------------------- 
# 금
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

gold_files='./data/feature/gold.csv'
print(gold_files)
df=pd.read_csv(gold_files)
df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO gold_price VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1])

    except:
        continue
# ----------------------------------------------------------------------------------------- 
# 무역수지
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

trade_balance_file='./data/feature/trade_balance.xlsx'
df=pd.read_excel(trade_balance_file,header=3)
print(trade_balance_file)
df.dropna(inplace=True)
df.rename({'Unnamed: 0':'date'},axis=1,inplace=True)
df['date']=pd.to_datetime(df['date'].str.replace('월','').str[0:4]+'-'+df['date'].str.replace('월','').str[4:6]+'-'+'15')
df['무역수지']=df['무역수지'].str.replace(',','').astype(float)
df[['date','무역수지']]
df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO trade_balance VALUES ('{df.iloc[i,0]}', {df.iloc[i,6]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,6])

    except:
        continue
# ----------------------------------------------------------------------------------------- 
# 유가(두바이)
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

oil_price_file='./data/feature/oil_price.csv'
df=pd.read_csv(oil_price_file)
print(oil_price_file)
df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO oil_price VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1])

    except:
        continue
# ----------------------------------------------------------------------------------------- 
# 철광석 usd 가격
connection = psycopg2.connect(**conn_params)
cur = connection.cursor()

iron_ore_file='./data/feature/iron_ore_price.csv'
df=pd.read_csv(iron_ore_file)

df.rename({'날짜':'date'},inplace=True,axis=1)
df['date']=pd.to_datetime(df['date'])
df=df.drop_duplicates(subset='date')
for i in range(0,len(df)):
    try:
        cur.execute(f"INSERT INTO iron_ore VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
        connection.commit()
        print(df.iloc[i,0],df.iloc[i,1])

    except:
        continue
# ----------------------------------------------------------------------------------------- 
# 비철금속
nonferrous_metal_pathlist=['copper','plumbum','zinc','nickel','aluminum_alloy','stannum']
for item in nonferrous_metal_pathlist:
    connection = psycopg2.connect(**conn_params)
    cur = connection.cursor()

    path=f'./data/feature/{item}_price.csv'
    df=pd.read_csv(path)
    print(path)
    df=df.drop_duplicates(subset='date')
    for i in range(0,len(df)):
        try:
            cur.execute(f"INSERT INTO {item} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]});")
            connection.commit()
            print(df.iloc[i,0],df.iloc[i,1])

        except:
            continue
# ----------------------------------------------------------------------------------------- 
