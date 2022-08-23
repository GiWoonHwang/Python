
from asyncio.windows_events import NULL
import pprint
from types import NoneType
import mysql.connector
from pymongo import MongoClient
import time
import datetime

# 기본 정보만 넣기
# client = MongoClient('localhost', 27017)
# db = client.test
# users = db['balances']
# user = users.find()
# temp = [x['userid'] for x in user]

# newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )

# for i in temp:
#     try:
#         usereth = users.find(
#         {'userid':i,},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
        
#         cursor = newDb.cursor(prepared=True)
#         sql = "INSERT ignore INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0)

#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         cursor.close()
#         # newDb.close()
#     except Exception as error:
#         print(error) 
#--------------------------------------------------------------------------------------------

# 게임 연동 여부 넣기 LoginStatus --> game 으로 컬럼값 변경
# client = MongoClient('localhost', 27017)
# db = client.ledger
# users = db['users']
# user = users.find()
# temp = [x['userid'] for x in user]

# newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )

# for i in temp:
#     try:
#         usergame = users.find_one(
#         {'userid':i,}
#         )
        
#         cursor = newDb.cursor(prepared=True)
#         # sql = "INSERT INTO blog_SignUp LoginStatus VALUES (%s) WHERE username = %s ; "
#         sql = "UPDATE blog_SignUp set LoginStatus= %s WHERE username = %s ; "
#         val = (str(usergame["game"]),str(i))

#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         cursor.execute(sql,val)
#         newDb.commit()
#         cursor.close()
#         # newDb.close()
#     except Exception as error:
#         print(error)
#--------------------------------------------------------------------------------------------

# 코인 지갑, 잔액 업데이트하기
# client = MongoClient('localhost', 27017)
# db = client.test
# users = db['balances']
# user = users.find()
# temp = [x['userid'] for x in user]

# newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
# )
# for i in temp:
#     try:
         
#         usereth = users.find_one(
#         {'userid':i,"coin":"ETH"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
#         )

#         print(usereth)
#         userbtc = users.find_one(
#         {'userid':i,"coin":"BTC"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
#         )
#         # print(userbtc["public_addr"])
#         usermPando = users.find_one(
#         {'userid':i,"coin":"MPANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
#         )
#         userpando = users.find_one(
#         {'userid':i,"coin":"PANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
#         )
        

#         cursor = newDb.cursor(prepared=True)
#         sql = "UPDATE blog_SignUp set BtcValue=%s, BtcWallet=%s, BtcPrive=%s, EthValue=%s, EthPandoWallet=%s, EthPandoPriv=%s, PandoValue=%s, PandoPriv=%s, mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
#         val = (str(userbtc["wa_balance"]), str(userbtc["public_addr"]), str(userbtc["private_key"]), str(usereth["wa_balance"]),str(userpando["public_addr"]),str(usereth["private_key"]), str(userpando["wa_balance"]),str(userpando["private_key"]), str(usermPando["public_addr"]),str(usermPando["wa_balance"]),str(i))
#         cursor.execute(sql,val)
#         newDb.commit()
#         cursor.close()
#         # newDb.close()
#         # result = cursor.fetchall()
#         # print(result)
#         # print("="*100)
#     except Exception as error:
#         error
#         # print(error)
# --------------------------------------------------------------------------------------------


client = MongoClient('localhost', 27017)
db = client.test
users = db['balances']
user = users.find()
temp = [x['userid'] for x in user]

newDb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="0000",
          database="blog",
          charset='utf8'
)

for i in temp:
    try:
         
        usereth = users.find_one(
        {'userid':i,"coin":"ETH"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
        )

        # print(usereth)
        userbtc = users.find_one(
        {'userid':i,"coin":"BTC"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
        )
        # print(userbtc["public_addr"])
        usermPando = users.find_one(
        {'userid':i,"coin":"MPANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
        )
        userpando = users.find_one(
        {'userid':i,"coin":"PANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False,"public_key":False,"createdAt":False}
        )
        

        # if usereth == None:
        #     cursor = newDb.cursor(prepared=True)
        #     sql = "UPDATE blog_SignUp set EthValue=%s WHERE username = %s ; "
        #     val = (None,str(i))
        #     cursor.execute(sql,val)
        #     newDb.commit()
        #     cursor.close()
        if usereth != None:
            cursor = newDb.cursor(prepared=True)
            # sql = "UPDATE blog_SignUp set BtcValue=%s, BtcWallet=%s, BtcPrive=%s, EthValue=%s, EthPandoWallet=%s, EthPandoPriv=%s, PandoValue=%s, PandoPriv=%s, mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
            sql = "UPDATE blog_SignUp set EthValue=%s,EthPandoWallet=%s,EthPandoPriv=%s WHERE username = %s ; "
            val = (str(usereth["wa_balance"]),str(usereth["public_addr"]),str(usereth["private_key"]),str(i))
            cursor.execute(sql,val)
            newDb.commit()
            cursor.close()
        
        elif userbtc != None:
            cursor = newDb.cursor(prepared=True)
            # sql = "UPDATE blog_SignUp set BtcValue=%s, BtcWallet=%s, BtcPrive=%s, EthValue=%s, EthPandoWallet=%s, EthPandoPriv=%s, PandoValue=%s, PandoPriv=%s, mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
            sql = "UPDATE blog_SignUp set btcValue=%s, BtcWallet=%s, BtcPrive=%s WHERE username = %s ; "
            val = (str(userbtc["wa_balance"]),str(userbtc["public_addr"]),str(userbtc["private_key"]),str(i))
            cursor.execute(sql,val)
            newDb.commit()
            cursor.close()
        
        elif usermPando != None:
            cursor = newDb.cursor(prepared=True)
            # sql = "UPDATE blog_SignUp set BtcValue=%s, BtcWallet=%s, BtcPrive=%s, EthValue=%s, EthPandoWallet=%s, EthPandoPriv=%s, PandoValue=%s, PandoPriv=%s, mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
            sql = "UPDATE blog_SignUp set mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
            val = (str(usermPando["public_addr"]),str(usermPando["wa_balance"]),str(i))
            cursor.execute(sql,val)
            newDb.commit()
            cursor.close()
        
        elif userpando != None:
            cursor = newDb.cursor(prepared=True)
            # sql = "UPDATE blog_SignUp set BtcValue=%s, BtcWallet=%s, BtcPrive=%s, EthValue=%s, EthPandoWallet=%s, EthPandoPriv=%s, PandoValue=%s, PandoPriv=%s, mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
            sql = "UPDATE blog_SignUp set PandoValue=%s, PandoPriv=%s WHERE username = %s ; "
            val = (str(userpando["wa_balance"]),str(userpando["private_key"]),str(i))
            cursor.execute(sql,val)
            newDb.commit()
            cursor.close()
    except Exception as error:
        print(error)



























