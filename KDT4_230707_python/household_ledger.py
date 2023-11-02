# ------------------------------------------------------------------------------
# [필수]
# - 클래스 기반
# - 데이터 저장 => File
# 속성/ 기능 나누기
# ppt
# ------------------------------------------------------------------------------
# 클래스명 : AccountBook
# 속성필드 : balance(월초잔액)
# 기능역할 : deposit 수입 / withdraw 지출 / breakdown 내역 / balancePrint 잔액조회
# ------------------------------------------------------------------------------
# 파일 입력 형태
# 
# =============================================================
# 이전달 잔액         1,000,000 |
# |          입금(항목) 500,000 | 
# |                            | 출금(항목) -600,000
# =============================================================
# |합계                1500000 |합계                   -600000 
# |총액                                               900,000원
# =============================================================
# ------------------------------------------------------------------------------
# 식비 / 교통 / 주거 / 문화 / 경조사 / 운동 / 교육 / 쇼핑 / 기타
# 월급 / 용동 / 이자수익 / 중고물품거래
# ------------------------------------------------------------------------------
class AccountBook:
    breakdown={}
    filename=r"C:\Users\KDP-040\Desktop\새 폴더\EXAM_4PYTHON\accountBooktest.txt"
    
    def __init__(self, balance):
        self.balance=balance
        self.firstbalance=balance

    def deposit(self, money, category):
        fp=open(self.filename, mode="a", encoding='utf-8')
        print("="*30)
        fp.writelines(["="*30,"\n"])
        print()
        fp.write("\n")
        print(f"(수익) {category} : {format(money,',')}")
        fp.writelines([f"(수익) {category} : {format(money,',')}","\n"])
        print()
        fp.write("\n")
        print("="*30)
        fp.writelines(["="*30,"\n"])
        self.balance+=money
        if category in self.breakdown:
            for i in self.breakdown.items():
                if category == i[0]:            
                    self.breakdown[category]=i[1]+money 
        elif category not in self.breakdown:               
            self.breakdown[category]=money
        fp.close()

    def withdraw(self, money, category):
        fp=open(self.filename, mode="a", encoding='utf-8')
        print("="*30)
        fp.writelines(["="*30,"\n"])
        print()
        fp.write("\n")
        print(f"(지출) {category} : {format(money,',')} ")
        fp.writelines([f"(지출) {category} : {format(money,',')} ","\n"])
        print()
        fp.write("\n")
        print("="*30)
        fp.writelines(["="*30,"\n"])
        self.balance-=money
        if category in self.breakdown:
            for i in self.breakdown.items():
                if category == i[0]:            
                    self.breakdown[category]=i[1]-money 
        elif category not in self.breakdown:               
            self.breakdown[category]=-money
        fp.close()

    def accountBookPrint(self,depositSum=0,withdrawSum=0):
        fp=open(self.filename, mode="a", encoding='utf-8')
        print("="*91)
        fp.writelines(["="*91,"\n"])
        print(f'|{"수익":^40}|{"지출":^44}|')
        fp.writelines([f'|{"수익":^40}|{"지출":^44}|',"\n"])
        print("="*91)
        fp.writelines(["="*91,"\n"])

        if self.firstbalance>=0:
            print(f"|{'전월잔액':ㅡ<11}|  {format(self.firstbalance,','):>17}|{'ㅡ'*23}|")
            fp.writelines([f"|{'전월잔액':ㅡ<11}|  {format(self.firstbalance,','):>17}|{'ㅡ'*23}|","\n"])
        elif self.firstbalance<0:
            print(f"|{'ㅡ'*21}|{'전월잔액':ㅡ<11}|  {format(self.firstbalance,','):>21}|")
            fp.writelines([f"|{'ㅡ'*21}|{'전월잔액':ㅡ<11}|  {format(self.firstbalance,','):>21}|","\n"])

        for i in self.breakdown.items():
            if i[1]>0:
                print(f"|{i[0]:ㅡ<11}|  {format(i[1],','):>17}|{'ㅡ'*23}|")
                fp.writelines([f"|{i[0]:ㅡ<11}|  {format(i[1],','):>17}|{'ㅡ'*23}|","\n"])
                depositSum+=i[1]
            elif i[1]<0:
                print(f"|{'ㅡ'*21}|{i[0]:ㅡ<11}|  {format(i[1],','):>21}|")
                fp.writelines([f"|{'ㅡ'*21}|{i[0]:ㅡ<11}|  {format(i[1],','):>21}|","\n"])
                withdrawSum+=i[1]

        print("="*91)
        fp.writelines(["="*91,"\n"])

        if self.firstbalance>=0:
            print(f"|{'합계':ㅡ<11}| {format(depositSum+self.firstbalance,','):>17} |{'합계':ㅡ<11}| {format(withdrawSum,','):>22}|")
            fp.writelines([f"|{'합계':ㅡ<11}| {format(depositSum,','):>17} |{'합계':ㅡ<11}| {format(withdrawSum,','):>22}|","\n"])
              
        elif self.firstbalance<0:
            print(f"|{'합계':ㅡ<11}| {format(depositSum,','):>17} |{'합계':ㅡ<11}| {format(withdrawSum+self.firstbalance,','):>22}|")
            fp.writelines([f"|{'합계':ㅡ<11}| {format(depositSum,','):>17} |{'합계':ㅡ<11}| {format(withdrawSum,','):>22}|","\n"])

        print("="*91)
        fp.writelines(["="*91,"\n"])
        print(f"|총액{'ㅡ'*18}{'ㅡ'*19}{format(self.firstbalance+depositSum+withdrawSum,','):>11}|")
        fp.writelines([f"|총액{'ㅡ'*18}{'ㅡ'*19}{format(self.firstbalance+depositSum+withdrawSum,','):>11}|","\n"])
        print("="*91)
        fp.writelines(["="*91,"\n"])
        fp.close()
    

    def balancePrint(self):
        fp=open(self.filename, mode="a", encoding='utf-8')
        print(f"잔액은 {format(self.balance,',')}입니다.")
        fp.writelines([f"잔액은 {format(self.balance,',')}입니다.","\n"])
        fp.close()


def accountBookInput():
    while True:
        breakdown=input('월초 잔액을 입력하세요.(숫자만입력) : ')
        if breakdown.isnumeric():
            breakdown=int(breakdown)
            break
        elif breakdown.startswith("-") and breakdown[1:].isnumeric():
            breakdown=int(breakdown)
            break
        else:
            print("숫자만 입력해주세요.")
    
    deal=AccountBook(breakdown)
    while True:
        func=input("수익, 지출을 입력하세요. (x를 누르면 종료합니다) : ")
        if func=="수익":
            category=input("카테고리를 입력하세요. (예) 월급 / 용돈 / 이자수익 / 중고물품거래 : ")
            while True:
                if category.isalpha():
                    break
                else:
                    print("잘못된 입력입니다. 다시입력해주세요.")   
            while True:
                money=input("금액을 입력해주세요.(숫자만입력) : ").strip()
                print(money, type(money))

                if money.isnumeric():
                    money=int(money)
                    break
                else:
                    print("잘못된 입력입니다. 다시입력해주세요.")   
            deal.deposit(money,category)
            deal.balancePrint()

        elif func=="지출":
            category=input("카테고리를 입력하세요. (예) 식비 / 교통 / 주거 / 문화 / 경조사 / 운동 / 교육 / 쇼핑 / 기타 : ")
            while True:
                if category.isalpha():
                    break
                else:
                    print("잘못된 입력입니다. 다시입력해주세요.")   
            while True:
                money=input("금액을 입력해주세요.(숫자만입력) : ")
                if money.isnumeric():
                    money=int(money)
                    break
                else:
                    print("잘못된 입력입니다. 다시입력해주세요.")  

            deal.withdraw(money,category)
            deal.balancePrint()
        elif func=="x":
            deal.accountBookPrint()
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

accountBookInput()

# ------------------------------------------------------------------------------
# while 문으로 구현할 코드
# accountBookinput()

# deal = AccountBook(1000000)
# deal1 = AccountBook("1000000")

# deal.deposit(2000000,"월급")
# deal.balancePrint()

# deal.withdraw(1250, "교통")
# deal.balancePrint()

# deal.withdraw(5000, "편의점")
# deal.balancePrint()

# deal.withdraw(10000, "편의점")
# deal.balancePrint()

# deal.withdraw(1250, "교통")
# deal.balancePrint()

# deal.withdraw(100000, "주택청약")
# deal.balancePrint()

# deal.withdraw(700000, "청년도약적금")
# deal.balancePrint()

# deal.accountBookPrint()

# ------------------------------------------------------------------------------
# 입금 기능 구현(값 추가시 덮어쓰지 않게!!)
# mdict={"주거":300000,"교통":1250}
# cate="주거"
# money=20000
# if cate in mdict:
#     for i in mdict.items():
#         print(i)
#         if cate == i[0]:            
#             mdict[cate]=i[1]+money
# mdict
# ------------------------------------------------------------------------------
# 가계부 출력하기(총계 출력)
# mdict={"주거":300000,"교통":1250}
# depositSum=0
# withdrawSum=0
# mdict[0]
# for i in mdict.items():
#     if i[1]>0:
#         print(f"|{i[0]:ㅡ<11}|  {i[1]:>17}|{'ㅡ'*23}|")
#         depositSum+=i[1]
#     elif i[1]<0:
#         print(f"|{'ㅡ'*21}|{i[0]:ㅡ<11}|  {i[1]:>21}|")
#         withdrawSum+=i[1]
# withdrawSum
# depositSum
# ------------------------------------------------------------------------------


