# 각국의 통화 이니셜 ? 받아옴 
from importlib.resources import contents
from urllib import response
from currency_converter import CurrencyConverter
import requests
from bs4 import BeautifulSoup

cc = CurrencyConverter()
print(cc.currencies)

# 현재 환율 불러옴 (1달러 기준)
dd = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(dd.convert(1,'USD','KRW'))

# 실시간 환율 크롤링
def get_exchange_rate(target1, target2):
    headers = { # 헤더를 추가한다. 헤더가 있어야 일반적인 브라우저를 이용하여 접속한것처럼 보임
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    
    response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1,target2), headers=headers) # 사이트 접속하여 가져옴
    contents = BeautifulSoup(response.content, 'html.parser') # 모듈을 이용하여 html로 보기 값을 좋게 함
    containers = contents.find('span', {'data-test': 'instrument-price-last'}) # 마지막 환율 정보를 찾음
    print(containers.text) # 아시죠 ?
    
get_exchange_rate('usd','krw') # 함수를 이용하여 1달러에 맞는 실시간 환율 출력
