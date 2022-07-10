# 이미지에서 글자를 인식하여 추출하는 코드 만들기
# pip install pytesseract
# https://github.com/UB-Mannheim/tesseract/wiki pc에서 이미지 인식을 위한 OCR 프로그램
# ---------------------------------------------------------------------------------------

# 이미지에서 한글을 찾아 추출하는 프로그램

from encodings import utf_8
from PIL import Image
import pytesseract

image_path = r'\한글이미지.png'

pytesseract.pytesseract.tesseract_cmd = r'파일이 설치된 경로'
text = pytesseract.image_to_string(Image.open(image_path), lang='kor') # 이미지에서 한글을 찾아 문자로 추출

print(text)
# ---------------------------------------------------------------------------------------

# 사용 가능한 언어 확인하는 코드 작성

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'설치경로'
laguages = pytesseract.get_languages(config='')
print(laguages)
# ---------------------------------------------------------------------------------------

# 위에 저장한 이미지에서 한글 추출하기

from PIL import Image
import pytesseract

image_path = r'\한글이미지.png'


pytesseract.pytesseract.tesseract_cmd = r'설치경로'
text = pytesseract.image_to_string(Image.open(image_path), lang='kor')

print(text)

with open(r'\한글변환.txt', 'w', encoding='utf8') as f:
    f.write(text)
