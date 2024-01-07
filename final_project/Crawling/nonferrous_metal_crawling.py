import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from tqdm import tqdm

code_dict={'CDY':'copper', 'PDY':'plumbum', 'ZDY':'zinc', 'NDY':'nickel', 'AAY':'aluminum_alloy', 'SDY':'stannum'}
# for code,col in code.items():
#     print(code,col)

# result_df=pd.DataFrame(columns=['date','dollar','yen','euro','yuan'])
all_values=[]
for code,col in code_dict.items():
    values = []
    dates = []
    cnt=1
    print(cnt)
    last_page=-3
    while True:
        try:
            time.sleep(1+random.random())
            url = f'https://finance.naver.com/marketindex/worldDailyQuote.naver?fdtc=2&marketindexCd=CMDT_{code}&page={cnt}'

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            date_ = soup.find_all('td', class_='date')
            # print(date_)
            for d in date_:
                dates.append(d.get_text(strip=True))

            value = []
            value_ = soup.find_all('td', class_='num')
            for v in value_:
                value.append(v.get_text(strip=True))

            for a in range(0,len(value),3):
                values.append(float(value[a].replace(',','')))
            values

            if '다음' not in str(soup.select('body > div > div')[0]):
                last_page+=1
                if last_page==0:
                    break

            cnt+=1
            print(cnt)        

        except:
            break

        df = pd.DataFrame({'date':dates,col:values})
        df.to_csv(f'./data/{col}_price.csv',index=False)

    # all_values.append(values)
# df = pd.DataFrame({'date':dates,'dollar':all_values[0],'yen':all_values[1],'euro':all_values[2],'yuan':all_values[3]})
# df['date']=pd.to_datetime(df['date'])
# df.to_csv('./data/exchange_rate.csv',index=False)