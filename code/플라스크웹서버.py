# 구글 사이트에서 이미지를 검색하고 검색한 이미지를 저장하는 프로그램을 만들어봅시다.
# pip install flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/1')
def test1page():
    return '1page ok'

@app.route('/2')
def test2page():
    return '2page ok'

@app.route('/map')
def map():
    return render_template('uni_map.html')


def main():
    app.run(debug=True, port=80) # 플라스크 웹서버 실행

if __name__ == '__main__':
    main()
