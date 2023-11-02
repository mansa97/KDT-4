# ---------------------------------------------
# Application 구동에 필요한 설정들
# 예) DB URI, Table...
# 적용 => Flask.config 인스턴스에 저장됨
# ---------------------------------------------

# 디버그 모드 여부 설정값
FLASK_DEBUG = True

# DB관련 설정값
import os
BASE_DIR = os.path.dirname(__file__)
DB_NAME = 'myapp.db'
DB_SQLITE_URI = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME)}'

# MSQL, MARIA RDEMS => 존재하는 데이터 베이스명 지정
DB_MYSQL_URI = "mysql+pymysql://root:root@localhost:3306/testdb"
DB_MARIA_URI = 'mariadb+mariadbconnector://root:root!@127.0.0.1:3306/db_ai'

# 사용할 DBMS 설정
# ORM SQLALCHEMY에 연동할 RDBMS 설정
SQLALCHEMY_DATABASE_URI = DB_SQLITE_URI # DB_SQLITE_URI DB_MARIA_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "hello"
