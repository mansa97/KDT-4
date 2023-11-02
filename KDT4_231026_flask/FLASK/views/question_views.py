from flask import Blueprint, render_template, url_for, request, g, flash
from datetime import datetime
from werkzeug.utils import redirect
from FLSK_PJT.app import db

from FLSK_PJT.models import Question
from FLSK_PJT.forms import QuestionForm, AnswerForm
from .auth_views import login_required


bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int,default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/question_list.html',
                           question_list = question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form=AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question = question, form=form)

@bp.route('/create/', methods=['post','get'])
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data,content=form.content.data,
                            create_date=datetime.now(), user=g.user)
        print(question)
        db.session.add(question)
        db.session.commit()
        # Post방식 요청이면 data 저장 후 질문목록 페이지로 이동
        return redirect(url_for('main.index'))
    # Get방식 요청이면 질문 목록 페이지 렌더링
    return render_template('question/question_form.html', form=form)

@bp.route('/modify/<int:question_id>/',methods=['GET','POST'])
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('question.detail', question_id=question_id))
    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else:
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html',form=form)

@bp.route('/delete/<int:question_id>/')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('삭제권한이 없습니다.')
        return redirect(url_for('question.detail',question_id=question_id))
    db.session.delete(question)
    db.session.commit()

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