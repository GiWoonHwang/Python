# from base64 import decode
# import imaplib
# import email
# from email import policy

# def find_encoding_info(txt): # 문자열을 인코딩한다
#     info = email.header.decode_header(txt)
#     subject, encode = info[0]
#     return subject, encode

# imap = imaplib.IMAP4_SSL('imap.gmail.com') # 구글 메일로 로그인한다
# id = ''
# pw = ''
# imap.login(id,pw)

# imap.select('INBOX') # 받은 메일함에서 메일을 읽는다
# resp, data = imap.uid('search', None, 'All')
# all_email = data[0].split()
# last_email = all_email[-5:] # 최신 5개의 메일만 읽는다. 만약 최신 100개를 읽고싶으면 -100으로

# for mail in reversed(last_email): # 최신의 메일만 출력하여 반복 reverse가 리스트를 뒤집어줌
#     result, data = imap.uid('fetch', mail, '(RFC822)') # 메일을 읽는다 
#     raw_email = data[0][1]
#     email_message = email.message_from_bytes(raw_email,policy=policy.default)
#     print('='*70)
#     print('FROM', email_message['FROM'])  # 32번라인까지 메일의 정보를 출력하는 구문
#     print('SENDER', email_message['Sender'])
#     print('TO', email_message['To'])
#     print('DATE', email_message['Date'])
#     subject, encode = find_encoding_info(email_message['Subject'])
#     print('SUBJECT:', subject)
#     print('='*70)

# imap.close()
# imap.logout()
# -------------------------------------------------------------------------------------

# 이메일의 본문내용을 읽어오자    

# import imaplib
# import email
# from email import policy

# def find_encoding_info(txt):
#     info = email.header.decode_header(txt)
#     subject, encode = info[0]
#     return subject, encode

# imap = imaplib.IMAP4_SSL('imap.gmail.com') # 구글 메일로 로그인한다
# id = ''
# pw = ''
# imap.login(id,pw)

# imap.select('INBOX') # 받은 메일함에서 메일을 읽는다
# resp, data = imap.uid('search', None, 'All')
# all_email = data[0].split()
# last_email = all_email[-5:] # 최신 5개의 메일만 읽는다. 만약 최신 100개를 읽고싶으면 -100으로

# for mail in reversed(last_email): # 최신의 메일만 출력하여 반복 reverse가 리스트를 뒤집어줌
#     result, data = imap.uid('fetch', mail, '(RFC822)') # 메일을 읽는다 
#     raw_email = data[0][1]
#     email_message = email.message_from_bytes(raw_email,policy=policy.default)
#     print('='*70)
#     print('FROM', email_message['FROM'])  # 32번라인까지 메일의 정보를 출력하는 구문
#     print('SENDER', email_message['Sender'])
#     print('TO', email_message['To'])
#     print('DATE', email_message['Date'])
#     subject, encode = find_encoding_info(email_message['Subject'])
#     print('SUBJECT:', subject)
    
#     print('CONTENT')
#     message = ''
#     if email_message.is_multipart():
#         for part in email_message.get_payload():
#             if part.get_content_type() == 'text/plain':
#                 bytes = part.get_payload(decode=True)
#                 encode = part.get_content_charset()
#                 message = message + str(bytes, encode)
#     print(message)
#     print('=' *70)
    
# imap.close()
# imap.logout()
# -------------------------------------------------------------------------------------

# 특정 키워드가 오면 스마트폰으로 알림 보내기

import imaplib
import email
from email import policy 
import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

def find_encoding_info(txt):    
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '아이디'
pw = '비밀번호'
imap.login(id, pw)

imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:] 

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default) 

    email_from = str(email_message['From']) # 문자열로 바인딩
    email_date = str(email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    subject_str = str(subject)
    if subject_str.find("김바쏘") >= 0: # 문자열에서 '김바쏘'를 찾는다. 만약 찾으면 위치를 반환함
        slack_send_message =  email_from + '\n' + email_date + '\n' + subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)

imap.close()
imap.logout()
# -------------------------------------------------------------------------------------

# 반복 실행하여 새로운 이메일의 내용일 있을 때만 slakc으로 메세지를 보내는 코드 만들기

import imaplib
import email
from email import policy
import requests
import json
import time

slack_webhook_url = ''

def sendSlakcWebhook(strText):
    headers = {
        'Content-type' : 'application/json'
    }
    
    data = {
        'text' : strText
    }
    
    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return 'ok'
    else:
        return 'error'
    
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode =info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.gmail.com')
id = ''
pw = ''

send_list = [] # 보내는 데이터를 저장할 리스트 생성

while True: # 반복문을 추가하여 계속 반복함
    try:
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-5:]
        for mail in reversed(last_email):
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email, policy=policy.default) 

            email_from = str(email_message['From']) # 문자열로 바인딩
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)
            if subject_str.find("김바쏘") >= 0: # 문자열에서 '김바쏘'를 찾는다. 만약 찾으면 위치를 반환함
                slack_send_message =  email_from + '\n' + email_date + '\n' + subject_str
                if slack_send_message not in send_list: # 리스트에 보낸 메세지가 없다면 만족합니다. 즉 새로운 메시지가 있으면 조건에 만족
                    sendSlackWebhook(slack_send_message)
                    print(slack_send_message)
                    send_list.append(slack_send_message) # 리스트에 보낸 메세지를 추가함
        time.sleep(30)
    except KeyboardInterrupt:
        break

imap.close()
imap.logout()