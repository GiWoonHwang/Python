# 파이썬을 이용하여 안드로이드 스마트폰을 제어하여 자동화 하는 프로그램을 만들어 본다.
# pip install pure-python-adb

#  파이썬으로 스마트폰 제어

from ppad.clinet import Client # 라이브러리 불러옴

client = Client(host='127.0.0.1', port = 5037) # ADB를 사용하기 위한 포트로 접속
find_devices = client.devices()

if len(find_devices) == 0: # 디바이스를 찾지 못했다면 종료
    print('no devices')
    quit()

device = find_devices[0]
print(f'찾은 디바이스: {device}')
# ---------------------------------------------------------------------------------------------------------------------------

# 상단의 코드로 디바이스를 찾은 후 스마트폰의 웹 브라우저를 열어보자

from ppad.clinet import Client # 라이브러리 불러옴
import time

def adb_connect():
    client = Client(hots='127.0.0.1', port = 5037)
    find_devices = Client.devices()

    if len(find_devices) == 0:
        print('장치가 없음')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device,  client

device, client = adb_connect() # adb에 연결

device.shell('input keyevent 64') # 명령어로 웹 브라우저 실행
time.sleep(3.0)
# ---------------------------------------------------------------------------------------------------------------------------

# 브라우저 화면 캠쳐  후 저장하는 코드

from ppadb.client import Client
import time

def adb_connect():
    client = Clinet(host='127.0.0.1', port= 5037 )
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('장치없음')
        quit()
    
    device = find_devices[0]
    print(f'찾은 디바이스 {device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64')
time.sleep(2.0)

xyPosition = '423 136'
device.shell(f'input tat{xyPosition}')
time.sleep(2.0)

url = 'www.naver.com'
device.shell(f'input text {url}')
time.sleep(2.0)

device.shee('input keyevent 66') # 엔터키 입력
time.sleep(2.0)

result = device.screencap()
with open(r'./screen.png', 'wb') as fp:
    fp.write(result)


