# 쓰레드란 코드를 실행하는 하나의 동작이다. 우리는 파이썬 코드를 이용하여 하나의 동작을 하는 코드를 만들고 있다. 하지만 프로그램이 커지고 
# 할일이 많아진다면 하나의 동작만을 가지고는 부족하여 스레드라는 방식을 이용하여 동작을 늘릴 수 있다

# import threading
# import time

# def thread_1():
#     while True:
#         print('쓰레드1 동작')
#         time.sleep(1.0) # 1초마다 쓰레드 동작함

# t1 = threading.Thread(target=thread_1) # 쓰레드 설정
# t1.start() # 쓰레드 시작

# while True: # 메인코드로 2초마다 출력
#     print('메인동작')
#     time.sleep(2.0)
# ----------------------------------------------------------------------------------------------------------------------

# 메인코드가 동작할 때에만 쓰레드 동작하는 코드 만들기

# import threading
# import time    

# def thread_1():
#     while True:
#         print('쓰레드 1동작')
#         time.sleep(1.0)
        
# t1 = threading.Thread(target=thread_1)
# t1.daemon = True # 쓰레드를 데몬쓰레드로 설정하여 메인코드가 동작할때만 실행되게함
# t1.start()

# while True:
#     print('메인동작')
#     time.sleep(2.0)
# ----------------------------------------------------------------------------------------------------------------------

# 다수의 쓰레드를 동작시키는 코드 만들고 실행

# import threading
# def sum(name,value):
#     for i in range(0, value):
#         print(f'{name} : {i}')
    
# t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))
# t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))

# t1.start()
# t2.start()

# print('Main Thread')
