개발과정 첨부
[flask.docx](https://github.com/JangDeukchun/Python/files/8646946/flask.docx)

1. forms.py에서 wtforms.fileds.html5 에서 EmailField를 import할 수 없다는 에러가 발생해서 아래처럼 수정했습니다.

(수정 전)
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField

(수정 후)
from wtforms import StringField, TextAreaField, PasswordField, EmailField

2. 웹 페이지 실행 후 페이지 이동할때 URL에 /?page=1 같은 예시로 해야한다

3. 코드에 jquery 버전 유의할것 (현재 나는 3.6버전으로 코딩)

4. 웹페이지 ![화면 캡처 2022-05-08 211501](https://user-images.githubusercontent.com/85157729/167295709-5b9d36e9-fd06-4b3f-82dd-ec3ba486a2fa.png)
![화면 캡처 2022-05-08 211550](https://user-images.githubusercontent.com/85157729/167295710-61b7d90c-ccdf-4b7f-a611-6c63e2740f6e.png)
