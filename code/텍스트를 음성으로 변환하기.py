# 텍스트를 한글 음성으로 변환하고 변환된 파일을 재생하여 출력하는 프로그램을 만들어본다.
# pip install gtts
# pip install playsound
# --------------------------------------------------------------------------------------------------------------

# 텍스트를 음성으로 변환
# from playsound import playsound
# from gtts import gTTS
# import os # 경로를 이동하기 위한 os라이브러리

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# text = '안녕하세요 황기운 입니다'

# tts = gTTS(text=text, lang='ko')
# tts.save(r"예제\hi.mp3")
# playsound('hi.mp3')
# --------------------------------------------------------------------------------------------------------------

# 파일에서 문자를 읽어 음성으로 출력하는 코드

from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동

file_path = '나의텍스트' # 텍스트 파일을 변수에 담는다
with open(file_path, 'rt', encoding= 'UTF8') as f: # 파일을 f의 이름으로 오픈한다. 한글로 작성된 파일을 열기 때문에 rf, utf8 형식으로 열어 글자가 깨지지 않게 함
    read_file = f.read() # 파일의 전체 내용을 읽어 read_file 변수에 바인딩한다. with는 파일을 열고 종료되면 자동으로 파일을 닫는다. 파일을 열 때 with를 사용하면 코드가 간결해짐

tts = gTTS(text=read_file, lang='ko')

tts.save('myText.mp3')