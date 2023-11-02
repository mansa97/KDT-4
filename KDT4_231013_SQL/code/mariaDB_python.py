# --------------------------------------------------------------------------------------------------------------------
# MariaDB & Python 연동
# --------------------------------------------------------------------------------------------------------------------
# 모듈 로딩
import mariadb as mdb
import sys
import pandas as pd
import numpy as np


# mariaDB 접속값
conn_params={'host':'localhost',
            'port':3306,
            'user':'root',
            'password':'root',
            'autocommit':True,
            'db':'place'}

df=pd.read_csv(r'edu\12.sql\teamproject_1011\data\db_entertain.csv')
df2=pd.read_csv(r'edu\12.sql\teamproject_1011\data\db_restaurant.csv')
df3=pd.read_csv(r'edu\12.sql\teamproject_1011\data\db_cafe.csv')
df4=pd.read_csv(r'edu\12.sql\teamproject_1011\data\블로그감성분석.csv')
try:
    # mariaDB 연결
    conn=mdb.connect(**conn_params)

    # DB에 접근할 수 있는 Cursor객체 가져오기
    cursor = conn.cursor()

    # entertain 데이터 입력
    for i in range(0,len(df)):
        e_name=df.iloc[i][0]
        e_address=df.iloc[i][1]
        e_latitude=df.iloc[i][2]
        e_longitude=df.iloc[i][3]
        # print(e_name,e_address,e_latitude,e_longitude)

        cursor.execute('insert into entertain(e_name,e_address,e_latitude,e_longitude) values(?,?,?,?);',[e_name,e_address,e_latitude,e_longitude])

    # restaurant 데이터 입력
    for i in range(0,len(df2)):
        r_name=df2.iloc[i][0]
        r_star=df2.iloc[i][1]
        r_address=df2.iloc[i][2]
        r_latitude=df2.iloc[i][3]
        r_longitude=df2.iloc[i][4]
        print(r_name,r_star,r_address,r_latitude,r_longitude)

        cursor.execute('insert into restaurant(r_name,r_star,r_address,r_latitude,r_longitude) values(?,?,?,?,?);',[r_name,r_star,r_address,r_latitude,r_longitude])


    # cafe 데이터 입력
    for i in range(0,len(df3)):
        c_name=df3.iloc[i][0]
        c_star=df3.iloc[i][1]
        c_address=df3.iloc[i][2]
        c_latitude=df3.iloc[i][3]
        c_longitude=df3.iloc[i][4]
        # print(e_name,e_address,e_latitude,e_longitude)

        cursor.execute('insert into cafe(c_name,c_star,c_address,c_latitude,c_longitude) values(?,?,?,?,?);',[c_name,c_star,c_address,c_latitude,c_longitude])

    # emotion 데이터 입력
    for i in range(0,len(df4)):
        em_name=df4.iloc[i][3]
        blog_content=df4.iloc[i][1]
        hash_content=df4.iloc[i][2]
        href=df4.iloc[i][0]
        # print(e_name,e_address,e_latitude,e_longitude)

        cursor.execute('insert into emotion(em_name,blog_content,hash_content,href) values(?,?,?,?);',[em_name,blog_content,hash_content,href])
    
    # mariaDB 종료
    conn.close()


except mdb.Error as e:
    print(f'Error connecting to MariaDB Platform : {e}')
    sys.exit(1)
# --------------------------------------------------------------------------------------------------------------------
# DB 생성 쿼리문
'''
CREATE DATABASE place;

USE place;

CREATE TABLE `cafe` (
	`c_name` VARCHAR(50) PRIMARY KEY,
	`c_star` FLOAT,
	`c_address` TEXT,
	`c_latitude` FLOAT,
	`c_longitude` FLOAT
)
;

CREATE TABLE `entertain` (
	`e_name` VARCHAR(50) PRIMARY KEY,
	`e_address` TEXT,
	`e_latitude` FLOAT,
	`e_longitude` FLOAT,
	`positive` FLOAT,
	`negative` FLOAT,
)
;

CREATE TABLE `emotion` (
	`em_name` VARCHAR(50) PRIMARY KEY,
	`blog_content` TEXT,
	`hash_content` TEXT,
	`href` TEXT
)
;

CREATE TABLE `restaurant` (
	`r_name` VARCHAR(50) PRIMARY KEY,
	`r_star` FLOAT,
	`r_address` TEXT,
	`r_latitude` FLOAT,
	`r_longitude` FLOAT 
)
;
'''
# --------------------------------------------------------------------------------------------------------------------
# DB select 쿼리문
'''
#-----------------------------------------------------------------------------------------------------------------
# 키워드 받아서 평점이 가장 높고/ 거리가 가장 가까운 순으로 카페 5곳 추천
SELECT c.c_name,c.c_star,c.c_latitude, c.c_longitude, e.e_latitude, e.e_longitude,
ROUND((6371 * acos(cos(radians(e.e_latitude)) * cos(radians(c.c_latitude)) *
 cos(radians(c.c_longitude) - radians(e.e_longitude))
 + sin(radians(e.e_latitude)) * sin(RADIANS(c.c_latitude)))),0) AS distance
FROM cafe AS c, 
(SELECT e_latitude, e_longitude from entertain WHERE e_name='강정보디아크광장') AS e
ORDER BY DISTANCE ASC, c.c_star DESC LIMIT 5;
#-----------------------------------------------------------------------------------------------------------------
# 키워드 받아서 평점이 가장 높고/ 거리가 가장 가까운 순으로 음식점 5곳 추천
SELECT r.r_name,r.r_star,r.r_latitude, r.r_longitude, e.e_latitude, e.e_longitude,
round((6371 * acos(cos(radians(e.e_latitude)) * cos(radians(r.r_latitude)) *
 cos(radians(r.r_longitude) - radians(e.e_longitude))
 + sin(radians(e.e_latitude)) * sin(RADIANS(r.r_latitude)))),0) AS distance
FROM restaurant AS r, 
(SELECT e_latitude, e_longitude from entertain WHERE e_name='강정보디아크광장') AS e
ORDER BY DISTANCE ASC, r.r_star DESC LIMIT 5;
#-----------------------------------------------------------------------------------------------------------------
# 키워드 받아서 연관성이 높고/ 감성분석 점수가 높고/ 거리가 가장 가까운 순으로 놀곳 5곳 추천
SELECT n.e_name,n.positive,n.e_latitude, n.e_longitude, e.e_latitude, e.e_longitude,
ROUND((6371 * acos(cos(radians(e.e_latitude)) * cos(radians(n.e_latitude)) *
 cos(radians(n.e_longitude) - radians(e.e_longitude))
 + sin(radians(e.e_latitude)) * sin(RADIANS(n.e_latitude)))),0) AS distance
FROM entertain AS n, 
(SELECT e_latitude, e_longitude from entertain WHERE e_name='강정보디아크광장') AS e
ORDER BY n.positive DESC, DISTANCE;
#-----------------------------------------------------------------------------------------------------------------
'''