
import pprint
import mysql.connector
from pymongo import MongoClient
import time
import datetime


# cursor = newDb.cursor()
# sql = "INSERT INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
# val = (str(datetime.datetime.now()), 0, "None", "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0)
# cursor.execute(sql,val)
# result = cursor.fetchall()
# # print(result)
# newDb.commit()
# cursor.close()
# newDb.close()

# client = MongoClient('localhost', 27017)
# db = client.test
# users = db['balances']
# user = users.find()
# temp = [x['userid'] for x in user]

# print(len(set(temp)))



newDb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0000",
  database="blog",
  charset='utf8'
)

# client = MongoClient('localhost', 27017)
# db = client.test
# users = db['balances']
# user = users.find()
# temp = [x['userid'] for x in user]
# for i in temp:
#     try:
#         usereth = users.find_one(
#         {'userid':i,"coin":"ETH"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         # print("가입날짜",usereth["createdAt"] )
#         # print( "이더 주소",usereth["public_addr"])
#         # print("이더 비밀키",usereth["private_key"])
#         # print("이더 잔액",usereth["wa_balance"])

#         newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )
#         cursor = newDb.cursor(prepared=True)
#         sql = "INSERT IGNORE  INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck,EthValue,EthPandoWallet,EthPandoPriv) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0, str(usereth["wa_balance"]), str(usereth["public_addr"]), str(usereth["private_key"]))
#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         # cursor.close()
#         # newDb.close()
#         print("="*100)

#         userbtc = users.find_one(
#         {'userid':i,"coin":"BTC"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         # print("비트 주소",userbtc["public_addr"])
#         # print("비트 비밀키",userbtc["private_key"])
#         # print("비트 잔액",usereth["wa_balance"])
#         newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )
#         cursor = newDb.cursor(prepared=True)
#         sql = "INSERT IGNORE  INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck,BtcValue,BtcWallet,EthPandoPriv) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0, str(userbtc["wa_balance"]), str(userbtc["public_addr"]), str(userbtc["private_key"]))
#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         # cursor.close()
#         # newDb.close()
#         print("="*100)
# # # --------------------------------------------------------------------------------------------
#         usermPando = users.find_one(
#         {'userid':i,"coin":"MPANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         # print("m판도 주소",usermPando["public_addr"])
#         # print("m판도 비밀키",usermPando["private_key"])
#         # print("m판도 잔액",usereth["wa_balance"])
#         newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )
#         cursor = newDb.cursor(prepared=True)
#         sql = "INSERT IGNORE  INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck,mPandoValue,mPandoWallet,EthPandoPriv) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0, str(usermPando["wa_balance"]), str(usermPando["public_addr"]), str(usermPando["private_key"]))
#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         # cursor.close()
#         # newDb.close()
#         print("="*100)
# # # --------------------------------------------------------------------------------------------
#         userpando = users.find_one(
#         {'userid':i,"coin":"PANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         # print("판도 주소",userpando["public_addr"])
#         # print("판도 비밀키",userpando["private_key"])
#         # print("판도 잔액",usereth["wa_balance"])
#         newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )
#         cursor = newDb.cursor(prepared=True)
#         sql = "INSERT IGNORE  INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck,PandoValue,EthPandoWallet,EthPandoPriv) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0, str(userpando["wa_balance"]), str(userpando["public_addr"]), str(userpando["private_key"]))
#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         # cursor.close()
#         newDb.close()
#         print("="*100)
#     except Exception as error:
#         print(error) 











# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# client = MongoClient('localhost', 27017)
# db = client.test
# users = db['balances']
# user = users.find()
# temp = [x['userid'] for x in user]
# for i in temp:
#     try:
#         usereth = users.find_one(
#         {'userid':i,"coin":"ETH"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         userbtc = users.find_one(
#         {'userid':i,"coin":"BTC"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         usermPando = users.find_one(
#         {'userid':i,"coin":"MPANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         userpando = users.find_one(
#         {'userid':i,"coin":"PANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )
#         newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )
#         cursor = newDb.cursor(prepared=True)
#         sql = "REPLACE  INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck,EthValue,EthPandoWallet,EthPandoPriv,BtcValue,BtcWallet,mPandoValue,mPandoWallet,PandoValue) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0, str(usereth["wa_balance"]), str(usereth["public_addr"]), str(usereth["private_key"]),str(userbtc["wa_balance"]),str(userbtc["public_addr"]),str(usermPando["wa_balance"]),str(usermPando["public_addr"]),str(userpando["wa_balance"]))

#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         # cursor.close()
#         # newDb.close()
#         print("="*100)
#     except Exception as error:
#         print(error) 




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# 기본 정보만 넣기
# client = MongoClient('localhost', 27017)
# db = client.test
# users = db['balances']
# user = users.find()
# temp = [x['userid'] for x in user]
# for i in temp:
#     try:
#         usereth = users.find(
#         {'userid':i,},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
#         )


#         newDb = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="0000",
#           database="blog",
#           charset='utf8'
#         )
#         cursor = newDb.cursor(prepared=True)
#         sql = "INSERT ignore INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
#         val = (str(datetime.datetime.now()), 0, str(i), "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0)

#         cursor.execute(sql,val)
#         # result = cursor.fetchall()
#         # print(result)
#         newDb.commit()
#         # cursor.close()
#         # newDb.close()
#         print("="*100)
#     except Exception as error:
#         print(error) 
#--------------------------------------------------------------------------------------------

client = MongoClient('localhost', 27017)
db = client.test
users = db['balances']
user = users.find()
temp = [x['userid'] for x in user]
for i in temp:
    try:
        usereth = users.find_one(
        {'userid':i,"coin":"ETH"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
        )
        userbtc = users.find_one(
        {'userid':i,"coin":"BTC"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
        )
        usermPando = users.find_one(
        {'userid':i,"coin":"MPANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
        )
        userpando = users.find_one(
        {'userid':i,"coin":"PANDO"},{"_id":False,"public_key":False,"updatedAt":False,"__v":False,"info":False,"wa_status":False,"wa_blocked":False,"wa_info":False,"wa_move":False}
        )
# str(usereth["wa_balance"]), str(usereth["public_addr"]), str(usereth["private_key"]),str(userbtc["wa_balance"]),str(userbtc["public_addr"]),str(usermPando["wa_balance"]),str(usermPando["public_addr"]),str(userpando["wa_balance"])

        newDb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="0000",
          database="blog",
          charset='utf8'
        )
        cursor = newDb.cursor(prepared=True)
        sql = "UPDATE blog_SignUp set BtcValue=%s, BtcWallet=%s, BtcPrive=%s, EthValue=%s, EthPandoWallet=%s, EthPandoPriv=%s, PandoValue=%s, PandoPriv=%s, mPandoWallet=%s, mPandoValue=%s WHERE username = %s ; "
        # sql = "INSERT INTO blog_SignUp (EthValue,EthPandoWallet,EthPandoPriv,BtcValue,BtcWallet,mPandoValue,mPandoWallet,PandoValue) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE username = %s;"
        val = (str(userbtc["wa_balance"]), str(userbtc["public_addr"]), str(userbtc["private_key"]), str(usereth["wa_balance"]),str(userpando["public_addr"]),str(usereth["private_key"]), str(userpando["wa_balance"]),str(userpando["private_key"]), str(usermPando["public_addr"]),str(usermPando["wa_balance"]),str(i))

        # cursor.execute(sql)
        cursor.execute(sql,val)
        
        # result = cursor.fetchall()
        # print(result)
        newDb.commit()
        # cursor.close()
        # newDb.close()
        print("="*100)
    except Exception as error:
        print(error) 
# --------------------------------------------------------------------------------------------






























# newDb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="0000",
#   database="blog",
#   charset='utf8'
# )

# cursor = newDb.cursor()
# sql = "INSERT INTO blog_SignUp (last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, name, password,otpCheck) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
# val = (str(datetime.datetime.now()), 0, "None", "None", "None", 0, 0, str(datetime.datetime.now()), "None", "None", 0)
# cursor.execute(sql,val)
# result = cursor.fetchall()
# # print(result)
# newDb.commit()
# cursor.close()
# newDb.close()
