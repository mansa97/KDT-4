import pandas as pd
import requests
from bs4 import BeautifulSoup

# sqld,sqlp 크롤링해서 csv파일로 저장하기
# 다른 조원이 했기에 자세한 설명 X
url = "https://allaboutwealth.tistory.com/413"
response = requests.get(url)
sql = BeautifulSoup(response.text, 'html.parser')

table_sql = sql.select('table > tbody')
sqlD_table = table_sql[0].select('tr')[1:]
sqlP_table = table_sql[1].select('tr')[1:]

sqlP_list = []
sqlD_list = []
for i in range(len(sqlP_table)):
    p_year_info = sqlP_table[i].select('td > span > span')
    year = p_year_info[0].get_text()
    tesk_taker = int(p_year_info[3].get_text())
    pass_rate = int(p_year_info[4].get_text())

    sqlP_list.append([year,tesk_taker,pass_rate])

    d_year_info = sqlD_table[i].select('td > span > span')
    year = d_year_info[0].get_text()
    tesk_taker = int(d_year_info[3].get_text().replace(",",''))

    sqlD_list.append([year,tesk_taker])

sqlD_DF = pd.DataFrame(sqlD_list, columns=['연도','응시자 수'])
sqlD_DF.sort_values(by='연도',ascending=True,ignore_index=True).to_csv('sqlD.csv')
sqlP_DF = pd.DataFrame(sqlP_list, columns=['연도','응시자 수','합격률'])
sqlP_DF.sort_values(by='연도', ascending=True,ignore_index=True).to_csv('sqlP.csv')

