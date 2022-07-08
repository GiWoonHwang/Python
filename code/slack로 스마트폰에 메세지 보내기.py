import requests
import json

slack_web_url = 'www.naver.com'

def sendSlackWebhook(strText):
    headers = {
        'Content-type' : 'application/json'
    }
    
    data = {
        'text' : strText
    }
    
    res = requests.post(slack_web_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return 'ok'
    else:
        return 'error'
    
print(sendSlackWebhook('안녕'))