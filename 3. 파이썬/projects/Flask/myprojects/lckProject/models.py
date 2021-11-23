# 데이터베이스를 처리하는 models.py 파일
# 파이보 프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다.
# SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다.
# 지금은 모델 기반으로 데이터베이스를 처리한다는 말이 이해되지 않겠지만,
# 이후 프로젝트를 진행하면 잘 알 수 있을 것이다. 아무튼 지금 여러분이 알아야 할 내용은 파이보 프로젝트에는
# "모델 클래스들을 정의할 models.py 파일이 필요하다"는 것이다.

from lckProject import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # relationship : 모델 참조
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)