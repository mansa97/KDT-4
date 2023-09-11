#---------------------------------------------------------------------------------------------------------------------------------------
# 모듈 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
#---------------------------------------------------------------------------------------------------------------------------------------
# 사람인 크롤링(기업 요구 직무 종류)
work2=[]
page_count=0
for i in range(1,29):
    saramin_url='https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={0}&cat_kewd=116&isAjaxRequest=0&page_count=50&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=1&tab=job-category#searchTitle'.format(i)
    page_count+=1
    html=urlopen(saramin_url)
    soup=BeautifulSoup(html, 'html.parser')
    bs2=soup.select('.job_meta > span')
    
    for j in bs2:
        cnt=0
        for k in j:
            cnt+=1
            if 1<cnt<len(j):
                print(k.text)
                work2.append(k.text)
    print(f'현재{page_count}페이지를 크롤링 중 입니다.')        
print(work2)
#---------------------------------------------------------------------------------------------------------------------------------------
# 각 단어별 개수 딕셔너리로 생성
import collections
print(sorted(list(collections.Counter(work2).items()),key=lambda x: x[1],reverse=True))
all_List=sorted(list(collections.Counter(work2).items()),key=lambda x: x[1],reverse=True)
top20=sorted(list(collections.Counter(work2).items()),key=lambda x: x[1],reverse=True)[0:20]
print(top20)
#---------------------------------------------------------------------------------------------------------------------------------------
# 워드 클라우드 생성
import stylecloud
stylecloud.gen_stylecloud(text=dict(all_List),background_color='black', icon_name="fab fa-python", palette='colorbrewer.diverging.Spectral_11', font_path="malgun.ttf")
#---------------------------------------------------------------------------------------------------------------------------------------
# barplot 그리기(상위 20개 키워드)
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
top20=sorted(list(collections.Counter(work2).items()),key=lambda x: x[1],reverse=True)[0:20]
df=pd.DataFrame(columns=['work','count'])
cnt=0
for i in list(top20):
    df.loc[cnt]=i
    cnt+=1
fig=plt.figure(figsize=(10,8))
ax1=fig.add_subplot(1,1,1)
sns.barplot(data=df,x='work',y='count',palette='rocket')
plt.xticks(rotation=45)
plt.show()