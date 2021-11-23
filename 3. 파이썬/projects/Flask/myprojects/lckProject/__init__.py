# flask app 생성 -> __name__ md에 담기
# app = Flask(__name__)
# flask 내장 함수 - 다른 함수명이면 정상작동하지 않음

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    # 모델 호출
    from . import models

    #BluePrint
    from .app import main_view
    app.register_blueprint(main_view.bluePrint)

    return app