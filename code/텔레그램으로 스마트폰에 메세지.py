# 텔레그램을 이용하여 파이썬 코드로 메세지를 보나보자. 또한 텔레그램 봇을 생성하여 자동으로 답변을 해주는 기능도 만들어 본다
# pip install python-telegram-bot
#------------------------------------------------------------------------------------------------------------------------------------

# 텔레 아이디 추출 코드
from click import echo
import telegram

token = ''

bot = telegram.Bot(token=token)
updates = bot.getUpdates()

for u in updates:
    print(u.message)
# -------------------------------------------------------------------------------------------------------------

# 텔레로 메세지 보내기
import telegram

token = ''
id = ''
bot = telegram.Bot(token)
bot.sendMessage(chat_id = id, text="받아랏")
# -------------------------------------------------------------------------------------------------------------

# 텔레그램 bot 기능을 활용하여 메시지의 자동응답 보내는 코드 만들어보기

import telegram
from telegram.ext import Udater
from telegram.ext import MessageHandler, Filters

token = ''
id = ''

bot = telegram.Bot(token)
bot.senMessage(chat_id = id, text = '자동응답 테스트입니다. 안녕, 뭐해를 입력해보세요' )

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == '안녕':
        bot.send_message(chat_id=id, text='반갑다')
    elif user_text == '뭐해':
        bot.send_message(chat_id=id, text ='서현식')

echo_handler = MessageHandler(Filters.text, handler)
dispathcher.add_handler(echo_handler)