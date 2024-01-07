# -----------------------------------------------------------------------------------------
# 2023.11.06 크롤링
# => 선반 항목에 대해서만 크롤링
# -----------------------------------------------------------------------------------------
# 2023.11.08 크롤링
# => 전체 항목에 대해서 크롤링
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
# 페이지 클릭 함수 정의
def click_page(page_num):
    # 페이지 클릭
    link = driver.find_element(By.XPATH, f"//a[text()='{page_num}']")
    link.click()

    # 페이지 로딩 대기
    driver.implicitly_wait(12)
# -----------------------------------------------------------------------------------------    
# 테이블 만들기
def make_table():
    time.sleep(4)
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
            onerow.append(price)
            onerow.append(ud)
            cnt+=2
        elif '\n▲' in i.text:
            price, ud= i.text.split('\n▲  ')
            onerow.append(price)
            onerow.append(ud)
            cnt+=2
        elif '\n-' in i.text:
            price, ud= i.text.split('\n-  ')
            onerow.append(price)
            onerow.append(ud) 
            cnt+=2
        else:      
            onerow.append(i.text)
            cnt+=1
        
        if cnt==len(colbox):
            print(onerow)
            allrow.append(onerow)
            onerow=[]
            cnt=0
            
    result=pd.DataFrame(columns=colbox,data=allrow)
    
    return result
# -----------------------------------------------------------------------------------------
# 크롤링 항목
steelList=['Busheling','HeavyScrap','LightScrap','TurningScrap']
steeldict={'Busheling':'1','HeavyScrap':'2','LightScrap':'3','TurningScrap':'4'}
# -----------------------------------------------------------------------------------------
# 창 열기
service = Service(executable_path='./data/chromedriver.exe') 
# options=webdriver.ChromeOptions()
# driver=webdriver.Chrome(service=service,options=options)
driver=webdriver.Chrome()
driver.get("https://www.steeldaily.co.kr/")
driver.implicitly_wait(5) # 창 오픈까지 최대 10초를 기다려줌
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# 로그인 버튼 클릭
driver.find_element(By.CSS_SELECTOR, '#userLogin > li:nth-child(2) > a').click()
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# 아이디 및 비밀번호 입력 후 클릭
driver.find_element(By.CSS_SELECTOR, '#user_id').send_keys('아이디')
time.sleep(1.5)

driver.find_element(By.CSS_SELECTOR, '#user_pw').send_keys('비밀번호')
time.sleep(1.5)

driver.find_element(By.CSS_SELECTOR, '#loginForm > button').click()
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# 구독만료일 관련 안내 확인
driver.find_element(By.CLASS_NAME, 'button.nd-gray.expanded').click()
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# DB 센터 클릭
secline=driver.find_elements(By.CLASS_NAME, "secline")
DB_senter=secline[7]
DB_senter.click()
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# 컴퓨터가 보고있는 화면의 길이를 최대로 늘린다.
# 초기 위치 설정 
position = 0
while True:
    # 스크롤 다운
    driver.execute_script(f"window.scrollTo(0, {position});")
    
    # 페이지 로딩 대기 및 위치 증가
    position += 800
    time.sleep(2)

    # 새로운 높이 가져오고 비교하기 
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if position >= new_height:
        break
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# 프레임 변경
frame=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(frame)
# -----------------------------------------------------------------------------------------
# 특정 태그 선택 (예:class가 'menu-title'인 요소)
element = driver.find_element(By.CSS_SELECTOR, '#page-main > div > div > div > div > div.left-box > div:nth-child(7) > div')
# -----------------------------------------------------------------------------------------
# 선택한 태그 위치로 스크롤하기
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
# 현재 위치에서 50픽셀 아래로 스크롤하기
driver.execute_script("window.scrollBy(0, 50);")
time.sleep(1.5)
# -----------------------------------------------------------------------------------------
for item in steelList:
    # 항목 선택
    num=steeldict[item]
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
    # -----------------------------------------------------------------------------------------
    # 마지막 페이지 확인
    pageList=driver.find_elements(By.CLASS_NAME,'paging')[0].find_elements(By.TAG_NAME,'a')
    lastPage=int(pageList[-1].get_attribute("onclick").split('=')[1].split(';')[0])
    for i in tqdm(range(1, lastPage+1)):
        if i == 1:
            click_page(i)
            table = make_table()
        else:
            table_ = make_table()
            table = pd.concat([table, table_],ignore_index=True)
            click_page(i)
    print(table)
    table.to_csv(f'./data/{item}_price.csv', index=None)
    # ----------------------------------------------------------------------------------------- 
