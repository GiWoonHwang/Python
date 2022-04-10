from flask import Flask
from flask import request

app = Flask(__name__)

#get 방식 페이지에 뛰우는것
@app.route('/')
def user_juso():
    return "Page Open"

#서버에서 POST형식으로 보내게되면 BC에서 POST로 받음
@app.route('/create', methods=['POST'])
def create():
    #회원정보가 정상적으로 들어오면
    if request.is_json :
        params = request.get_json() #서버에서 보내준 회원의정보
        # print(params['user_id']) #user_id는 json의 key값 
        return params

app.run(host = '127.0.0.1', port=8090)