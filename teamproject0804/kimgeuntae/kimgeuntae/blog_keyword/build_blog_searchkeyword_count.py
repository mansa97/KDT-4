from selenium import webdriver
import pandas as pd
# 네이버 블로그에서 키에 해당하는 url 키워드
searchword = {'빅데이터':'%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0',
              '인공지능':'%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5',
              'AI':"AI"
              }
blogcountList = []

# 연도별 빅데이터,ai 키워드 수 리스트로 반환
for key in searchword.keys():
    countList = []
    for year in range(2012,2023):
        url = f"https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=PERIOD&orderBy=sim&startDate={year}-01-01&endDate={year}-12-31&keyword={searchword[key]}"
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome('C:\\workspace\\chromedriver')
        driver.get(url)
        driver.implicitly_wait(5)
        blog_count = driver.find_element_by_class_name("search_number").text
        a = blog_count.replace(',','')
        blog_count = a.replace('건','')
        countList.append(int(blog_count))
        driver.quit()
    blogcountList.append(countList)

# 리스트 DF 변환 후 blog_search_keyword_count.csv 파일로 생성
blogcountDF = pd.DataFrame(blogcountList, columns=[i for i in range(2012,2023)], index=[key for key in searchword.keys()])
blogcountDF = blogcountDF.T
blogcountDF.to_csv('blog_search_keyword_count.csv')