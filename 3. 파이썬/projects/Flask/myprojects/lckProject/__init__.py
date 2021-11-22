from flask import Flask

# flask app 생성 -> __name__ md에 담기
app = Flask(__name__)

@app.route('/')
def solution():
    return 'hello!'