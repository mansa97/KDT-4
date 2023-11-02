from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention={
    "ix" : "ix_%(column_0_label)s",
    "uq" : "uq_%(table_name)s_%(column_0_label)s",
    "ck" : "ck_%(table_name)s_%(column_0_label)s",
    "fk" : "fk_%(table_name)s_%(column_0_label)s_%(referred_table_name)s",
    "pk" : "pk_%(table_name)s"

}

def format_datetime(value, format=None):
  if format is None:
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    wd = weekdays[value.weekday()]
    format = "%Y년 %m월 %d일 ({}) %H:%M:%S".format(wd)
    formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
  else:
    formatted = value.strftime(format.encode('unicode-escape').decode()).encode().decode('unicode-escape')
  return formatted

db=SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate=Migrate()

from flask_wtf.csrf import CSRFProtect

from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

app.config['expiration_time'] = datetime.now() + timedelta(minutes=10)

remaining_time = app.config['expiration_time'] - datetime.now()

@app.route('/timer/')
def home():
    return render_template('timer/home.html')

def get_remaining_time_in_seconds():
    remaining_time = app.config['expiration_time'] - datetime.now()
    remaining_time_in_seconds = remaining_time.total_seconds()
    return remaining_time_in_seconds

@app.route('/timer/remaining_time')
def remaining_time():
    remaining_time_in_seconds = get_remaining_time_in_seconds()
    return jsonify({'remaining_time_in_seconds': remaining_time_in_seconds})

@app.route('/timer/reset', methods=['POST'])
def reset():
    if request.method == 'POST':
        app.config['expiration_time'] = datetime.now() + timedelta(minutes=10)
        return render_template('timer/home.html')


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app._static_folder = r'D:\EXAM_PANDAS\01_YOLO\basicflask\FLASK\static'
    app.jinja_env.filters['datetime'] = format_datetime

    # csrf = CSRFProtect()
    # csrf.init_app(app)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    
    # Blueprint
    from views import main_views, question_views, answer_views, game_views, yolo_views, auth_views, yolo_stream_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(game_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(yolo_views.bp)
    app.register_blueprint(yolo_stream_views.bp)

    return app