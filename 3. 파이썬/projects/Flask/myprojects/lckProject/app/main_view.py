from flask import Blueprint

bluePrint = Blueprint('main', __name__, url_prefix='/')

# Blueprint 생성 객체
@bluePrint.route('/')
def index():
    return 'sg-moomin python web project!!'

@bluePrint.route('/hello')
def solution():
    return 'hello sg-moomins'
