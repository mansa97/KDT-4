# ----------------------------------------------------------------------------------------- 
# PostgreSQL & Python 연동
# ----------------------------------------------------------------------------------------- 
# 모듈 로딩
import sys
import psycopg2 as pg2
import pandas as pd
from datetime import datetime
# ----------------------------------------------------------------------------------------- 
# DB접속
conn_params={'host':'localhost',
             'dbname':'steelcut',
            'port':5432,
            'user':'postgres',
            'password':'root'
            }
conn = pg2.connect(**conn_params)
cur = conn.cursor()
# ----------------------------------------------------------------------------------------- 
# 생철
sql_busheling='''CREATE TABLE IF NOT EXISTS public.busheling
(
    date date NOT NULL,
    "ba_k" integer,
    "ba_k_ud" integer,
    "ba_y" integer,
    "ba_y_ud" integer,
    "ba_m" integer,
    "ba_m_ud" integer,
    CONSTRAINT steeldata_pkey PRIMARY KEY (date)
)
;'''
# ----------------------------------------------------------------------------------------- 
# 중량
sql_heavy_scrap='''CREATE TABLE IF NOT EXISTS public.heavy_scrap
(
    date date NOT NULL,
    "hsa_k" integer,
    "hsa_k_ud" integer,
    "hsa_y" integer,
    "hsa_y_ud" integer,
    "hsa_m" integer,
    "hsa_m_ud" integer,
    CONSTRAINT heavy_scrap_pkey PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 경량
sql_light_scrap='''CREATE TABLE IF NOT EXISTS public.light_scrap
(
    date date NOT NULL,
    "lsa_k" integer,
    "lsa_k_ud" integer,
    "lsa_y" integer,
    "lsa_y_ud" integer,
    "lsa_m" integer,
    "lsa_m_ud" integer,
    CONSTRAINT light_scrap_pkey PRIMARY KEY (date)
)
;'''
# ----------------------------------------------------------------------------------------- 
# 선반
sql_turning_scrap='''CREATE TABLE IF NOT EXISTS public.turning_scrap\
(
    date date NOT NULL,
    "tsa_k" integer,
    "tsa_k_ud" integer,
    "tsa_y" integer,
    "tsa_y_ud" integer,
    "tsa_m" integer,
    "tsa_m_ud" integer,
    "tsc_k" integer,
    "tsc_k_ud" integer,
    "tsc_y" integer,
    "tsc_y_ud" integer,
    "tsc_m" integer,
    "tsc_m_ud" integer,
    PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 환율
sql_exchange_rate='''CREATE TABLE IF NOT EXISTS public.exchange_rate
(
    date date NOT NULL,
    dollar double precision NOT NULL,
    yen double precision NOT NULL,
    euro double precision NOT NULL,
    yuan double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 금
sql_gold_price='''CREATE TABLE IF NOT EXISTS public.gold_price
(
    date date NOT NULL,
    gold_price double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 무역수지
sql_trade_balance='''CREATE TABLE IF NOT EXISTS public.trade_balance
(
    date date NOT NULL,
    trade_balance double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 석유(두바이)
sql_oil_price='''CREATE TABLE IF NOT EXISTS public.oil_price
(
    date date NOT NULL,
    oil_price double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 철광석
sql_iron_ore='''CREATE TABLE IF NOT EXISTS public.iron_ore
(
    date date NOT NULL,
    iron_ore double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# ----------------------------------------------------------------------------------------- 
# 비철금속
# 구리
sql_copper='''CREATE TABLE IF NOT EXISTS public.copper
(
    date date NOT NULL,
    copper double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# 납
sql_plumbum='''CREATE TABLE IF NOT EXISTS public.plumbum
(
    date date NOT NULL,
    plumbum double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# 아연
sql_zinc='''CREATE TABLE IF NOT EXISTS public.zinc
(
    date date NOT NULL,
    zinc double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# 니켈
sql_nickel='''CREATE TABLE IF NOT EXISTS public.nickel
(
    date date NOT NULL,
    nickel double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# 알루미늄 합금
sql_aluminum_alloy='''CREATE TABLE IF NOT EXISTS public.aluminum_alloy
(
    date date NOT NULL,
    aluminum_alloy double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# 주석
sql_stannum='''CREATE TABLE IF NOT EXISTS public.stannum
(
    date date NOT NULL,
    stannum double precision NOT NULL,
    PRIMARY KEY (date)
);'''
# -----------------------------------------------------------------------------------------
cur.execute(sql_busheling)
cur.execute(sql_heavy_scrap)
cur.execute(sql_light_scrap)
cur.execute(sql_turning_scrap)
cur.execute(sql_exchange_rate)
cur.execute(sql_gold_price)
cur.execute(sql_trade_balance)
cur.execute(sql_oil_price)
cur.execute(sql_iron_ore)
cur.execute(sql_copper)
cur.execute(sql_plumbum)
cur.execute(sql_zinc)
cur.execute(sql_nickel)
cur.execute(sql_aluminum_alloy)
cur.execute(sql_stannum)
conn.commit()