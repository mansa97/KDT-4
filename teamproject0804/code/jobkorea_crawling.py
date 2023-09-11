#---------------------------------------------------------------------------------------------------------------------------------------
# 모듈 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
#---------------------------------------------------------------------------------------------------------------------------------------
# 잡코리아 크롤링(기업 요구 직무 종류)
work=[]
page_count=0
for i in range(1,138):
    # 크롤링시 차단되지 않도록 time.sleep 사용
    time.sleep(2 + random.randint(1,3))
    jobkorea_url='https://www.jobkorea.co.kr/Search/?stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&tabType=recruit&Page_No={}'.format(i)
    page_count+=1
    html=urlopen(jobkorea_url)
    soup=BeautifulSoup(html, 'html.parser')
    bs2=soup.select('p.etc')
    for j in bs2:
        print(j.text)
        workList=j.text.split(',')
        workList
        for k in workList:
            work.append(k.strip().replace('BigData','빅데이터'))
    print(f'현재{page_count}페이지를 크롤링 중 입니다.')
print(work)
#---------------------------------------------------------------------------------------------------------------------------------------
# 각 단어별 개수 딕셔너리로 생성
import collections
print(sorted(list(collections.Counter(work).items()),key=lambda x: x[1],reverse=True))
all_List=sorted(list(collections.Counter(work).items()),key=lambda x: x[1],reverse=True)
all_List
#---------------------------------------------------------------------------------------------------------------------------------------
# 상위 20위만 추출
top20=sorted(list(collections.Counter(work).items()),key=lambda x: x[1],reverse=True)[0:20]
print(top20)
#---------------------------------------------------------------------------------------------------------------------------------------
# 워드 클라우드 생성
import stylecloud
stylecloud.gen_stylecloud(text=dict(all_List),background_color='white', icon_name="fab fa-python", palette='colorbrewer.diverging.Spectral_11', font_path="malgun.ttf")
#---------------------------------------------------------------------------------------------------------------------------------------
# barplot 그리기(상위 20개 키워드)
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
top20=sorted(list(collections.Counter(work).items()),key=lambda x: x[1],reverse=True)[0:20]
df=pd.DataFrame(columns=['work','count'])
df
cnt=0
for i in list(top20):
    df.loc[cnt]=i
    cnt+=1
df
fig=plt.figure(figsize=(10,8))
ax1=fig.add_subplot(1,1,1)
sns.barplot(data=df,x='work',y='count',palette='crest')
plt.xticks(rotation=45)
plt.show()
#---------------------------------------------------------------------------------------------------------------------------------------
# barplot 그리기(프로그램 언어)
list_dict=dict(all_List)
language_List=['Python','C','C++','Java','C#','JavaScript','SQL']

df2=pd.DataFrame(columns=['p_language', 'count'])
cnt=0
for i in language_List:
    df2.loc[cnt]=[i,list_dict[i]]
    cnt+=1
df2
fig=plt.figure(figsize=(10,8))
ax1=fig.add_subplot(1,1,1)
sns.barplot(data=df2,x='p_language',y='count',palette='mako')
plt.xticks(rotation=45,)
plt.xlabel('프로그램언어')
plt.ylabel('개수')
ax1.set_yticks([0,2,4,6,8,10,12,14,16,18,20,22,24])
plt.show()