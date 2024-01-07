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
# -----------------------------------------------------------------------------------------
# 2023.11.08 크롤링 + DB추가
# -----------------------------------------------------------------------------------------
# 모델 불러오기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from tqdm import tqdm
# -----------------------------------------------------------------------------------------
# 테이블 만들기
def make_table():
    driver.find_element(By.TAG_NAME,'table')
    colList=driver.find_element(By.TAG_NAME,'table').find_elements(By.TAG_NAME,'th')
    colbox=[]
    for i in colList:
        if i.text != '날짜' and '날짜' not in i.text and i.text!='':
            colbox.append(i.text)
            colbox.append(i.text+'증감')
        else:
            colbox.append('날짜')
    print(colbox)
    
    rowList=driver.find_element(By.TAG_NAME,'table').find_elements(By.TAG_NAME,'td')
    # 증가 감소 분리해서 한 행씩 리스트에 담기
    onerow=[]
    allrow=[]
    cnt=0
    for i in rowList:
        if '\n▼' in i.text:
            price, ud= i.text.split('\n▼  ')
            onerow.append(int(price))
            onerow.append(int(ud))
            cnt+=2
        elif '\n▲' in i.text:
            price, ud= i.text.split('\n▲  ')
            onerow.append(int(price))
            onerow.append(int(ud))
            cnt+=2
        elif '\n-' in i.text:
            price, ud= i.text.split('\n-  ')
            onerow.append(int(price))
            onerow.append(int(ud))
            cnt+=2
        else:      
            onerow.append(i.text)
            cnt+=1
        # 모든 행 크롤링
        if cnt==len(colbox):
            print(onerow)
            allrow.append(onerow)
            onerow=[]
            cnt=0
        # 한행만 크롤링
        # if cnt==len(colbox):
        #     print(onerow)
        #     allrow.append(onerow)
            # break 
    result=pd.DataFrame(columns=colbox,data=allrow)
    time.sleep(4)
    return result
# -----------------------------------------------------------------------------------------
# 창 열기
service = Service(executable_path='./chromedriver.exe') 
# options=webdriver.ChromeOptions()
# driver=webdriver.Chrome(service=service,options=options)
driver=webdriver.Chrome()
driver.get("https://www.steeldaily.co.kr/")
driver.implicitly_wait(5) # 창 오픈까지 최대 10초를 기다려줌
time.sleep(2)
# -----------------------------------------------------------------------------------------
# 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, '#userLogin > li:nth-child(2) > a').click()
time.sleep(2)
# -----------------------------------------------------------------------------------------
# 아이디 및 비밀번호 입력 후 클릭
driver.find_element(By.CSS_SELECTOR, '#user_id').send_keys('steelcut_sowon')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#user_pw').send_keys('steelcut_sowon')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#loginForm > button').click()
time.sleep(2)
# -----------------------------------------------------------------------------------------
# 구독만료일 관련 안내 확인
driver.find_element(By.CLASS_NAME, 'button.nd-gray.expanded').click()
time.sleep(2)
# -----------------------------------------------------------------------------------------
# DB 센터 클릭
secline=driver.find_elements(By.CLASS_NAME, "secline")
DB_senter=secline[7]
DB_senter.click()
time.sleep(2)
# -----------------------------------------------------------------------------------------
# 프레임 변경
frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(frame)
# -----------------------------------------------------------------------------------------
# 크롤링 항목
steeldict={'busheling':'1','heavy_scrap':'2','light_scrap':'3','turning_scrap':'4'}
# -----------------------------------------------------------------------------------------
for item, num  in steeldict.items():
    # 선반 클릭하기
    driver.find_element(By.CSS_SELECTOR,f'div.left-box > div:nth-child(7) > ul > li:nth-child({num}) > a').click()
    # -----------------------------------------------------------------------------------------
    # 프레임 나오기
    driver.switch_to.default_content()
    # -----------------------------------------------------------------------------------------
    # 프레임 변경
    main_frame=driver.find_elements(By.TAG_NAME,"iframe")[0]
    driver.switch_to.frame(main_frame)
    # -----------------------------------------------------------------------------------------
    # 실행부
    df = make_table()
    print(df)
    # ----------------------------------------------------------------------------------------- 
    # connection = psycopg2.connect("host=192.168.0.1 dbname=postgres user=postgres password=1234 port=5432")
    # 또는
    # connection = psycopg2.connect(host="172.20.69.166", dbname="postgres", user="postgres", password="root", port=5432)
    connection = psycopg2.connect(**conn_params)
    cur = connection.cursor()

    # 최신 정보 갱신
    for i in range(0,len(df)):
        if len(df.columns)==7:
            try:
                cur.execute(f"INSERT INTO {item} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]},\
                            {df.iloc[i,4]}, {df.iloc[i,5]}, {df.iloc[i,6]});")
                connection.commit()
                print(df.iloc[i,0])
            except:
                continue

        elif len(df.columns)==13:
            try:
                cur.execute(f"INSERT INTO {item} VALUES ('{df.iloc[i,0]}', {df.iloc[i,1]}, {df.iloc[i,2]}, {df.iloc[i,3]}, {df.iloc[i,4]}, {df.iloc[i,5]}, {df.iloc[i,6]},\
                            {df.iloc[i,7]}, {df.iloc[i,8]}, {df.iloc[i,9]}, {df.iloc[i,10]}, {df.iloc[i,11]}, {df.iloc[i,12]});"
                            )
                connection.commit()
                print(df.iloc[i,0])
            except:
                continue


