from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen(r'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0')
soup=BeautifulSoup(html, 'html.parser')
soup
bs=soup.select('#content > section > div.category_search')
bs
for i in soup:  
    print(i.text)

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver = webdriver.Chrome('C:\\workspace\\chromedriver')
driver.get(r'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0')
driver.implicitly_wait(5)
# find_element_by_class_name('클래스이름'): 하나의 클래스 이름 검색
# name = driver.find_element_by_class_name('green')
name = driver.find_element(By.CLASS_NAME, "search_number")
print(name.text)



print(name.text)
print('-' * 20)
# find_elements_by_class_name('클래스이름'): 해당 클래스 이름을 모두 검색
nameList = driver.find_elements(By.CLASS_NAME,'green')

driver.find_elements(By.CSS_SELECTOR)

for name in nameList:
    print(name.text)
driver.quit()

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen(r'https://www.jobkorea.co.kr/Recruit/GI_Read/42424843?Oem_Code=C1&logpath=1&stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&listno=699')
soup=BeautifulSoup(html, 'html.parser')
soup
bs=soup.select('#content > section > div.category_search')
bs
for i in soup:  
    print(i.text)




# ------------------------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver = webdriver.Chrome('C:\\workspace\\chromedriver')
driver.get(r'https://www.jobkorea.co.kr/Recruit/GI_Read/42498862?Oem_Code=C1&logpath=1&stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&listno=1')
driver.implicitly_wait(5)
# find_element_by_class_name('클래스이름'): 하나의 클래스 이름 검색
# name = driver.find_element_by_class_name('green')
name = driver.find_element(By.XPATH, "/html/body/div[5]/section/section/div[1]/article/div[2]/div[1]/dl/dd[3]/text()")
print(name.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get(r'https://www.jobkorea.co.kr/Recruit/GI_Read/42498862?Oem_Code=C1&logpath=1&stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&listno=1')
driver.implicitly_wait(time_to_wait=5)
element = driver.find_element(By.XPATH,'/html/body/div[5]/section/section/div[1]/article/div[2]/div[1]/dl/dd[3]/text()')
print(element.text)


from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen(r'https://www.jobkorea.co.kr/Recruit/GI_Read/42498862?Oem_Code=C1&logpath=1&stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&listno=1')
soup=BeautifulSoup(html, 'html.parser')
bs=soup.select('div.tbRow.clear > div:nth-child(1) > dl > dd:nth-child(6)')
for i in bs:  
    print(i.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get(r'https://linkareer.com/list/contest?filterType=CATEGORY&orderBy_direction=DESC&orderBy_field=CREATED_AT&page=1')
driver.implicitly_wait(time_to_wait=5)
element = driver.find_elements(By.CLASS_NAME,'MuiTypography-colorTextPrimary')
for i in element:
    print(i.text)

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get(r'https://linkareer.com/list/contest?filterType=CATEGORY&orderBy_direction=DESC&orderBy_field=CREATED_AT&page=1')
driver.implicitly_wait(time_to_wait=5)
element = driver.find_elements(By.TAG_NAME,'img')
element
for i in element:
    print(i.text)