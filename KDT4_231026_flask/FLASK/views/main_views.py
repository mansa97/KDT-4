from flask import Blueprint, url_for
from werkzeug.utils import redirect
# from FLSK_PJT.models import Question


# 블루프린트 객체 생성
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_flask():
    return 'hello, FLASK!!(Blueprint)'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# @bp.route('/')
# def index():
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html',
#                            question_list = question_list)

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get(question_id)
#     return render_template('question/question_detail.html',
#                            question = question)