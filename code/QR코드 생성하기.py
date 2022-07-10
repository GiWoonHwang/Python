# QR코드를 자동으로 생성하는 프로그램을 만들어본다.
# pip install qrcode 
# --------------------------------------------------------------------------------------------------------------

# import qrcode

# qr_data = 'www.naver.com' 
# qr_img = qrcode.make(qr_data) # 변수에 담긴 값을 기반으로 qr이미지를 만든다

# save_path = '예제\\'+ qr_data + '.png' # 이미지를 경로에 저장
# qr_img.save(save_path) # 이미지를 저장
# --------------------------------------------------------------------------------------------------------------

# 여러개의 qr코드를 한번에 생성하는 코드를 만들고 실행, 읽어온 주소로 qr코드를 생성하고 저장

import qrcode

file_path = r'예제\qr코드모음'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines() # f.readlines() 파일을 읽어 줄 별로 리스트 값의 형태로 내어준다.  read_lines에는 줄별로 읽힌 값이 리스트 형태로 바인딩됨

    for line in read_lines: # 여러개의 값을 읽기 위하여 for문 씀
        line = line.strip() # line.strip()은 줄 마지막에 줄바꿈 문자를 삭제함
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = '예제\\' + qr_data + '.png'
        qr_img.save(save_path)
