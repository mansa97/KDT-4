dobble_dic={'clown' : '광대',
            'dinosaur' : '공룡',
            'dobble' : '도블',
            'dog' : '개',
            'dolphin' : '돌고래',
            'dragon' : '용',
            'exclmation_mark' : '느낌표',
            'eye' : '눈',
            'flower' : '꽃',
            'ghost' : '유령',
            'hammer' : '망치',
            'heart' : '하트',
            'horse' : '말',
            'ice' : '얼음',
            'igloo' : '이글루',
            'key' : '열쇠',
            'cat' : '고양이',
            'ladybug' : '무당벌레',
            'lightning' : '번개',
            'lip' : '입술',
            'lock' : '자물쇠',
            'maple' : '단풍잎',
            'mark' : '과녁',
            'moon' : '달',
            'paints' : '물감',
            'pencil' : '연필',
            'person' : '사람',
            'question_mark' : '물음표',
            'scissors' : '가위',
            'sign' : '표지판',
            'skeleton' : '해골',
            'snow' : '눈꽃',
            'snowman' : '눈사람',
            'spider' : '거미',
            'sun' : '해',
            'sunglasses' : '선글라스',
            'taeqeuk' : '태극',
            'the_treble_clef' : '높은음자리표',
            'tree' : '나무',
            'turtle' : '거북이',
            'water_drop' : '물방울',
            'web' : '거미줄',
            'zebra' : '얼룩말',
            'bulb' : '전구',
            'clock' : '시계',
            'art' : 'art',
            'stop' : 'stop',
            'taxi' : '자동차',
            'ok' : 'ok',
            'carrot' : '당근',
            'clover' : '네잎클로버',
            'apple' : '사과',
            'baby_bottle' : '젖병',
            'cheese' : '치즈',
            'cactus' : '선인장',
            'bomb':'폭탄',
            'campfire':'모닥불',
            'lib':'입술',
            'candle':'촛불',
            'anchor':'닻',
            'bird':'새',
            '':''

}

from flask import Blueprint, url_for, render_template, request, Response, jsonify, current_app
from werkzeug.utils import redirect
import random
import time
from datetime import datetime, timedelta
# from FLSK_PJT.models import Question

import pymysql as ps
db = ps.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='db_ai',
    charset='utf8'
)


# 블루프린트 객체 생성
bp = Blueprint('game', __name__, url_prefix='/game')

# 전역변수
score=0
count=21
same_picture=''
pathList=[]
cardList=[]

def card_make():
    pathList=[]
    cardList=[]
    numList=list(range(1,17))
    sampleList=random.sample(numList,k=2)
    for i in sampleList:
        cursor=db.cursor()
        cursor.execute(f'select * from dobble where do_id={i}')
        cardList.append(cursor.fetchall())
        pathList.append(f'image/{i}.jpg')
    print(cardList)
    card1=cardList[0][0]
    card2=cardList[1][0]
    print(card1)
    print(card2)
    for i in card1:
        if i in card2:
            same_picture=i
    print(dobble_dic[same_picture])
    
    return pathList, cardList, same_picture



@bp.route('/', methods=['post','get'],endpoint='game')
def game():
    global score, count, same_picture, pathList, cardList

    if request.method == 'GET' :
        pathList=[]
        cardList=[]
        score = 0
        pathList, cardList, same_picture = card_make()
        
        

    if request.method == 'POST' :
        print(type(request.form['answer']),request.form['answer'],request.form['answer']==dobble_dic[same_picture])
        if request.form['answer']==dobble_dic[same_picture]:
            score+=1
            count=16
            pathList=[]
            cardList=[]
            pathList, cardList, same_picture = card_make()
            return render_template('game/game_main.html', image_file=pathList, correct_answer=same_picture, score=score)
    
    return render_template('game/game_main.html', image_file=pathList, correct_answer=same_picture, score=score)

@bp.route('/manual', methods=['post','get'])
def manual():
    return render_template('game/game_manual.html')
        


@bp.record
def record_params(setup_state):
    app = setup_state.app
    app.config['expiration_time'] = 10
    # print(datetime.now() + timedelta(seconds=10))


def get_remaining_time_in_seconds():
    global count
    count-=1
    remaining_time = count
    remaining_time_in_seconds = remaining_time
    print(remaining_time)
    return remaining_time_in_seconds


@bp.route('/remaining_time')
def remaining_time():
    global count
    remaining_time_in_seconds = get_remaining_time_in_seconds()
    
    if int(remaining_time_in_seconds)==0:
        count = 31
    #     print('-----------------------------------')
    #     return jsonify({'remaining_time_in_seconds': remaining_time_in_seconds})
    return jsonify({'remaining_time_in_seconds': remaining_time_in_seconds})

@bp.route('/game_over')
def game_over():
    global score
    return render_template('game/game_over.html', score=score) 

# @bp.route('/reset', methods=['POST'])
# def reset():
#     if request.method == 'POST':
#         current_app.config['expiration_time'] = datetime.now() + timedelta(seconds=10)
#         print(5)
#         return render_template('timer/timer.html')
