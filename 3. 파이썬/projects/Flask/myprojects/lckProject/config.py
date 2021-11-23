import os

BASE_DIR = os.path.dirname(__file__)
# DB 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'lck.db'))
# SQLAlchemy event
SQLALCHEMY_TRACK_MODIFICATIONS = False
