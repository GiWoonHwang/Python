# 영문 내용의 파일을 읽어 한글로 번역하고 새로운 파일로 저장하는 프로그램을 만들어본다
# pip install googletrans==4.0.0-rc1

# import googletrans

# translator = googletrans.Translator()

# str1 = '서현식'
# result1 = translator.translate(str1, dest='en', src='auto') # dest에 번역될 문자를 입력 src에는 번역할 문자의 언어로 auto가 기본값
# print(f'행복하세요 => {result1.text}')

# str2 = 'I am dongken'
# result2 = translator.translate(str2, dest='ko', src='en')
# print(f'I am dongken => {result2.text}' )

# ----------------------------------------------------------------------------------------------------------

# 영어로된 문서를 한글로 자동번역2

# import googletrans

# lang = googletrans.LANGUAGES # 사용가능한 언어목록 출력
# print(lang) 
# ----------------------------------------------------------------------------------------------------------

# 영어 문서를 한글로 번역하는 코드 만들기

# from os import linesep
# import googletrans

# translator = googletrans.Translator()

# read_text_path = r'.\영어파일.txt'

# with open(read_text_path, 'r') as f:
#     readLines = f.readlines() # 파일을 줄별로 읽어 변수에 리스트 형태로 저장

# for lines in readLines: # 저장된 리스트를 한줄씩 읽어 출력
#     result1 = translator.translate(lines, dest='latin')
#     print(result1.text)
# ----------------------------------------------------------------------------------------------------------

# 번역 내용을 새 파일로 저장하는 코드

from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r'./영어파일.txt'
write_file_path = r'./라틴파일.txt'

with open(read_file_path, 'r') as f:
    readLines = f.readlines()
    
for lines in readLines:
    result1 = translator.translate(lines, dest='latin')
    print(result1.text)
    
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')