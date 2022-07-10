# 압축파일의 암호를 푸는 프로그램을 만들어 본다. 번호를 생성하고 암호화된 압축파일에 대입해서 암호를 푸는 방식

# import itertools
# from pprint import pprint

# passwd_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # 모든숫자와 영문자를 변수에 집어넣음

# for len in range(1,4): # 반복
#     to_attempt = itertools.product(passwd_string, repeat=len) # 변수의 담긴 모든 문자열을 repeat=길이 로 정렬하여 반환
#     print(to_attempt)
#     for attempt in to_attempt: # 정렬하여 반환된 문자의 수만큼 반복
#         passwd = ''.join(attempt) # 리스트로 반환된 값을 문자열로 변환
#         print(passwd)
# --------------------------------------------------------------------------------------------------------------

# 이 코드는 정상작동하지 않는다 비밀번호를 찾고 출력했지만 너무 빨리 다음 단계로 넘어가 출력값을 확인하기 어렵다. break문을 써서 for문은 종료했지만 for문이 두개있어 모든 for문을 종료하지 않고 아래쪽 하나의 for문만 종료함

# import itertools
# import zipfile

# passwd_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # 모든숫자와 영문자를 변수에 집어넣음

# zFile = zipfile.ZipFile(r'암호1234.zip')

# for len in range(1,6):
#     to_attempt = itertools.product(passwd_string, repeat=len)
#     for attempt in to_attempt:
#         passwd = ''.join(attempt)
#         print(passwd)
#         try:
#             zFile.extractall(pwd=passwd.encode())
#             print(f'비밀번호는 {passwd} 입니다')
#         except:
#             pass
# --------------------------------------------------------------------------------------------------------------

# 비밀번호를  찾으면 프로그램이 종료되는 코드를 만들고 실행

import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len +1):
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd= passwd.encode())
                print(f'비밀번호는 {passwd} 입니다')
                return 1
            except:
                pass

passwd_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
zFile = zipfile.ZipFile(r'암호1234.zip')

min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1:
    print('암호찾기 성공')
else:
    print('암호찾기 실패')

