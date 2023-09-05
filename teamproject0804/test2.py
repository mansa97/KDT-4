#---------------------------------------------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
work=[]

for i in range(1,28):
    saramin_url='https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={0}&cat_kewd=116&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle'.format(i)
    html=urlopen(saramin_url)
    soup=BeautifulSoup(html, 'html.parser')
    bs2=soup.select('.job_meta > span')
    bs2
saramin_url='https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=45737108&recommend_ids=eJxNj7kRAzEMA6txzhcgYxfi%2FruwTvYdFe5gCQwDwg7Gp7RffAeUEiILdaMY1fGgJe1C%2B8nGhMWkdIffaTYE0JVio2mo8xlaVcmRiy3pd1UWKrf8b4ZrD2qCcuDqYo9sa7bOW6eNrOuHQfHQOmSToI5MI68UX10aQDM%3D&view_type=list&gz=1&t_ref_content=general&t_ref=jobcategory_recruit&immediately_apply_layer_open=n#seq=0'
html=urlopen(saramin_url)
soup=BeautifulSoup(html, 'html.parser')
bs2=soup.select('#content > div.wrap_jview > section.jview.jview-0-45737108 > div.wrap_jv_cont > div.jv_cont.jv_statics > div > div > div > div.box_chart.narrow.count.sub > dl > dd')
bs2
for i in bs2:
    print(i)


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver = webdriver.Chrome('C:\\workspace\\chromedriver')
driver.get(r'https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=45737108&recommend_ids=eJxNj7kRAzEMA6txzhcgYxfi%2FruwTvYdFe5gCQwDwg7Gp7RffAeUEiILdaMY1fGgJe1C%2B8nGhMWkdIffaTYE0JVio2mo8xlaVcmRiy3pd1UWKrf8b4ZrD2qCcuDqYo9sa7bOW6eNrOuHQfHQOmSToI5MI68UX10aQDM%3D&view_type=list&gz=1&t_ref_content=general&t_ref=jobcategory_recruit&immediately_apply_layer_open=n#seq=0')
driver.implicitly_wait(5)
# find_element_by_class_name('클래스이름'): 하나의 클래스 이름 검색
# name = driver.find_element_by_class_name('green')
name = driver.find_element(By.CLASS_NAME, "total")
print(name.text)
count=name.text.replace('지원자수\n','').replace(',','').replace("명",'')
print(count)


def peo_count(html):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome('C:\\workspace\\chromedriver')
    driver.get(html)
    driver.implicitly_wait(5)
    # find_element_by_class_name('클래스이름'): 하나의 클래스 이름 검색
    # name = driver.find_element_by_class_name('green')
    name = driver.find_element(By.CLASS_NAME, "total")
    print(name.text.replace('지원자수\n','').replace(',','').replace("명",''))
    count=name.text.replace('지원자수\n','').replace(',','').replace("명",'')
    return count