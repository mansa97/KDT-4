from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import random



html=urlopen(r'https://www.jobkorea.co.kr/Recruit/GI_Read/42498862?Oem_Code=C1&logpath=1&stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&listno=1')
soup=BeautifulSoup(html, 'html.parser')
bs=soup.select('div.tbRow.clear > div:nth-child(1) > dl > dd:nth-child(6)')
for i in bs:  
    print(i.text)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen(r'https://www.jobkorea.co.kr/Search/?stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&cotype=1%2C2%2C4%2C5%2C15%2C7%2C8&jobtype=1%2C2%2C4%2C6')
soup=BeautifulSoup(html, 'html.parser')
bs=soup.select_one('.dev_tot')
last_page=int(bs.text.replace(',',''))

certificate=[]

# for i in range(1,last_page+1):
certificate=[]

from urllib.request import urlopen
from bs4 import BeautifulSoup

time.sleep(3 + random.randint(1,4))
html=urlopen(r'https://www.jobkorea.co.kr/Search/?stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&cotype=1%2C2%2C4%2C5%2C15%2C7%2C8&jobtype=1%2C2%2C4%2C6')
soup=BeautifulSoup(html, 'html.parser')
bs=soup.select_one('.dev_tot')
last_page=int(bs.text.replace(',',''))

from urllib.request import urlopen
from bs4 import BeautifulSoup

for i in range(1,5):
    time.sleep(3 + random.randint(1,4))
    html=urlopen('https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={i}&cat_kewd=116&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle')
    html
    soup=BeautifulSoup(html, 'html.parser')
    soup
    bs2=soup.select('.job_sector')
    for j in bs2:
        print(j)
        certificate.append(j.text.strip().split(','))

for i in certificate:
    print(i)

bs.text.strip().split(',')
print(i.text.strip().split(','))

certificate

from urllib.request import urlopen
from bs4 import BeautifulSoup
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
p=1
html=urlopen('https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={p}&cat_kewd=116&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle')
soup=BeautifulSoup(html, 'html.parser')

bs2=soup.select('.job_meta > span')

for i in bs2:
    cnt=0
    for j in i:
        cnt+=1
        if cnt<len(i):
            print(j.text)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    
    for j in bs2:
        cnt=0
        test=[]
        for k in j:
            cnt+=1
            if 1<cnt<len(j):
                print(k.text)
                test.append(k.text)
        work.append(test)

for i in work:
    print(i)


work_DF=pd.DataFrame(columns=[1,2,3,4,5])
work_DF
cnt=0
for i in work:
    work_DF.loc[cnt]=i
    cnt+=1

work_DF=pd.DataFrame(work,columns=[1,2,3,4,5])
work_DF

for i in work:
    work_DF=i

import collections
print(collections.Counter(work))

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
    
    for j in bs2:
        cnt=0
        for k in j:
            cnt+=1
            if 1<cnt<len(j):
                print(k.text)
                work.append(k.text)

import collections
print(sorted(dict(collections.Counter(work).items()),key=lambda x: x[0][1]))
collections.Counter(work).items()
list(collections.Counter(work).items())[0][1]

print(sorted(list(collections.Counter(work).items()),key=lambda x: x[1],reverse=True))

top20=sorted(list(collections.Counter(work).items()),key=lambda x: x[1],reverse=True)[0:20]
print(top20)