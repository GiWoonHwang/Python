# 숫자 자료형 
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(2*8)
# print(3*(3+1))

# 문자 자료형
# print('풍선')
# print("나비")
# print("z"*9)

# boolan 자료형 참 / 거짓
# print(5 < 10)
# print(5 > 10) 
# print(not( 5>10))

# 변수
# 애완동물을 소개해 주세요
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age>=3
# print(" 우리집 "+str(animal)+ "의 이름은 연탄이에요") 정수형 같은 경우 +를 포함한 print문에 쓰이기 위해서는 str을 넣어준다. 
# print(" 연탄이는 4살이며, 산책을 아주 좋아해요")
# print(" 연탄이는 어른일까요? true")

# 변수를 이용하여 다음 문장을 출력해보자.

# a = '사당'
# b = '신도림'
# c = '인천공항'
# print(a + "행 열차가 들어오고 있습니다")

# 연산자 
# print(2**3) 제곱이다
# print(5%3) 5 나누기 3의 나머지
# print(5//3) 5 나누기 3의 몫
# print(3 == 3) 3은 3과 같다.
# print(1 != 3) 1은 3과 같지 않다.

# 간단한 수식
# print(2+3*4)
# print((2+3) + 4 )
# number = 2 + 3 * 4
# print(number)
# number = number +2 
# print(number)
# number +=2  변수에 2를 더한다
# number *=2 변수에 2를 곱한다
# number /=2 변수에 2를 나눈다
# nubmer %= 2 변수를 2로 나눈 나머지

# 숫자 처리 함수
# print(abs(-5)) 절댓값 함수
# print(pow(4,2)) 4의 2제곱
# print(max(5,12)) 입력받은 값의 최댓값
# print(min(5,12)) 입력받은 값의 최솟값
# print(round(3.114)) 반올림

# 랜덤함수
# from random import *
# print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() *10)+1)
# print(int(random() * 45) +1)
# print(int(random() * 45) +1)
# print(int(random() * 45) +1)
# print(int(random() * 45) +1)
# print(int(random() * 45) +1)
# print(int(random() * 45) +1)
# print(int(random() * 45) +1)

# print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1,45)) 1 ~ 45 이하의 임의의 값 생성 

# from random import randint


# 조건에 맞는 날짜를 정해주는 프로그램을 정하시오
# 조건1: 랜덤으로 날짜를 뽑아야함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# a = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월" + str(a)+ "로 선정되었습니다.")

# 문자열 
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) 
# print("월" + jumin[2:4])
# print("뒤 7자리" + jumin[7:14])
# print("뒤에서부터 7자리" + jumin[-7:])

# 문자열 처리 함수 
# python = 'Python is Amazing'
# print(python.lower()) # 문자열을 소문자로 출력
# print(python.upper()) # 문자열을 대문자로 출력
# print(python[0].isupper()) # 첫번째 문자가 대문자인지 출력
# print(len(python)) # 문자열 길이 출력
# print(python.replace("Python", "Java")) # 문자 바꿔서 출력

# index = python.index("n")
# print(index)
# index=python.index("n", index + 1 )
# print(index)

# 문자열 포맷
# print("나는 %d살입니다" % 20 ) # %뒤에 있는 값을 넣는다 d는 정수 의미
# print("나는 %s을 좋아해요" % "파이썬" ) # s는 문자열 
# print("나는 %c을 좋아해요" % "A" ) # c는 한 글자 
# print("나는 {}살 입니다".format(20))
# age = 20 
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출문
# print("백문이 불어일견 \n백견이 불여일타") # 문장 내 줄바꿈
# print('저는 "황기운"입니다.' )
# print("저는 \"황기운\"입니다")

# \\은 하나의 \로 취급한다

# 리스트: 순서를 가지는 객체의 집합
# 지하철 칸별로 10명,20명,30명
# subway = [10,20,30]
# print(subway)
# print(subway.index(10))
# subway.append("하하")
# print(subway)
# subway.insert(1,"정형돈")
# print(subway)
# print(subway.pop())

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()

# num_list= [5,4,3,2,1,]
# mix_lsit = [1,2,3,4,5]
# num_list.extend(mix_lsit)
# print(num_list)

# 사전
# cabinet = {3 : "유재석", 100 : "김태호"}
# print(cabinet[3])
# print(cabinet.get(3))
# print(cabinet.get(5, "사용가능"))
# print(cabinet)
# print(cabinet)
# print(cabinet.items())
# print(cabinet.keys())
# print(cabinet.values())

# 튜플 : 내용 변경이나 추가를 할 수 없지만 속도가 리스트 보다 빠르다
# menu = ("돈까스", "치즈까스")
# print(menu[0])

# name= "김종국"
# age = 20
# hobby = "코딩"

# name, age, hobby = ("김종국",20,"코딩")

# 집합(set) : 중복이 안되고 순서가 없음
# my_set = {1,2,3,3,3}
# print(my_set) = {1,2,3,} 만 출력

# java = {"유재석","김태호","양세형"}
# python = {"유재석","박명수"}

# # 교집합 구하기
# print(java & python)
# # 합집합 구하기
# print(java | python)

# 자료구조 변경
# menu = {"커피","우유","주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))

# weather = input("오늘 날씨는 어떄요? : ")
# # if 조건: 
# #     실행 명령문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없다")

# temp = input(int("기온은 어떄요? : "))
# if 30 < temp:
#     print("너무 더워요 나가지 마세요")
# elif 10 < temp and temp <30:
#     print("괜찮은 날씨에요")

# 반복문 for 
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# for waiting_num in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_num))
# for waiting_num in range(5):
#     print(waiting_num)

# hero = ["서현식","한동근","한동훈"]
# for i in hero:
#     print(i)

# 반복문 while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("커피가 준비 되었습니다.")
#     index -= 1
#     if index ==0:
#         print("커피 안준다")

# cumstomer = "토르"
# person = "Unknown"

# while person != cumstomer :
#     print("커피가 준비 되었씁니다")
#     person = input("이름이 : ")

# continue 와 break 
# absent = [2,5] # 결석
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     # print(str(student) + " 책을 읽어봐")
#     elif student in no_book:
#         print("수업 끝")

# 한줄 for 
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# 학생이름을 대문자로 변환
# student = ["iron man", "torr", "i am groot"]
# student = [i.upper() for i in student]
# print(student)

# 함수 : 어떠한 역할을 하는 박스이다 

# def open_account():
#     print("새로운 계좌가 생성되었습니다")

# open_account()

# 전달값과 반환값
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다")
#         return balance - money
#     else:
#         print('출금이 완료되지 않았습니다.')

# def wighdraw_night(balance,money):
#     commission = 100
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance,1000)
# # balance = withdraw(balance, 20000)
# commisiion, balance = wighdraw_night(balance,500)

# 함수의 기본값
# def profile(name, age, main_lang):
#     print("이름{0}\t나이{1}\t주사용언어:{2}".format(name,age,main_lang))

# profile("유재셕",20,"파이썬")

# 같은학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="python"):
#     print("이름{0}\t나이{1}\t주사용언어:{2}".format(name,age,main_lang))

# profile("유재석")


# 키워드값
# def profile(name,age,main_lang):
#     print(name,age,main_lang)

# profile(name="유재석",main_lang="파이썬",age=20)

# 가변인자
# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름:{0}나이{1}".format(name,age))

# def profile(name, age, *languague):
#     print("이름:{0}나이{1}".format(name,age))

# 지역변수 전역변수 : 함수내에서만 사용하는 변수, 프로그램 모든 곳에서 사용하는 변수
# gun = 10

# def checkpoint(soldiers):
#     global gun 
#     gun = gun - soldiers
#     print("[함수 내] 나믐총 : {}".format(gun))

# def check_return(gun, soldiers):
#     gun = gun - soldiers
#     print("남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# 표준 입출력
# print("Pyrgon", "Java", "Javascript", sep="", end="?")
# print("무엇이 더 재미있을까요?")

# scores = ["수학":0, "영어":50, "코딩":100]
# for subject, score in scores.items():
#     print(subject,score)

# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file= score_file)
# score_file.close()

# score_file = open("score.txt", "r", encoding='utf8')
# print(score_file.read())
# score_file.close()

# pickle : 프로그램상에서 사용하는 데이터를 파일형으로 저장한다
# import pickle


# profile_file = open("profile.pickle","wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구","곮프"]}
# print(profile)
# pickle.dump(profile, profile_file)

# 클래스
# 마린 : 공격유닛, 군인, 총을쏜다

# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력{1}".format(hp, damage))

# # 탱크 : 공격 유닛 ,포를 쏠 수 있는데 일반모드/ 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력{1}".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}".format(name,location,damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# from multiprocessing import set_forkserver_preload
# from operator import truediv


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self,location):
#         print("{0} : {1} 방향으로 이동합니다".format(self.name,location,self.speed))


# marine = Unit("마린", 40, 5) 
# tank = Unit("탱크",150,35) 

# __init__ : 파이썬에서 쓰이는 생성자이다

# 멤버변수 
# 레이스 : 공중유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스",80,5)
# print("유닛이름 {0}, 공격력 {1}".format(wraith1.name,wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만든다 
# wraith2 = Unit("레이스",80,5)
# wraith2.clocking = True

# if wraith2.clocking ==   True:
#     print("{0}는 현재 클로킹중입니다".format(wraith2.name))

# class attackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage
    
#     def attack(self,location):
#         print("{0} : {1} 방향으로 적군을 공격합니다 [공격력 {2}".format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0}이 {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다".format(self.name))

# # 파이어뱃 : 공격유닛, 화염방사기
# firebat1 = attackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp

# class flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

# class flyableattckunit(attackUnit,flyable):
#     def __init__(self, name,hp,damage,flying_speed):
#         attackUnit.__init__(self,name,hp,0,damage)
#         flyable.__init__(self,flying_speed)
#     def  move (self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 발키리 : 공중공격유닛, 한번에 14번 미사일 발사
# vlakyrie = flyableattckunit("발키리",200,6,5)
# vlakyrie.fly(vlakyrie.name, "3시")

# 메소드 오버라이딩 : 자식클래스에서 정의한 메소드를 쓰고싶을 떄 클래스를 새롭게 정의해서 사용 가능

# vulture = attackUnit("벌쳐",80,20,10)
# battlecruiser = flyableattckunit("배틀크루쳐",500,25,3)

# vulture.move("!1시")
# battlecruiser.move(battlecruiser.name, "9시")

# 건물
# class buildingunit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# supply_depot = buildingunit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     pass

# game_start()
# game_over()

# 예외처리 
# try:

#     print(" 나누기 전용 계산기 입니다. ")
#     nums = []
#     nums.append(  int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append( int(input("두 번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0]/nums[1]))

#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError :
#     print(" 에러! 잘못된 값을 입력하였습니다. ")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알 수 없는 에러가 발생하였습니다")

# 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요"))
#     num2 = int(input(" 두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0}/{1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘 못된 값을 입력했습니다. 한 자리 숫자만 입력하세요")
    

# 사용자 정의 에러처리


# class bignumbererror(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요"))
#     num2 = int(input(" 두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise bignumbererror("입력 값 : {0},{1}".format(num1,num2))
#     print("{0}/{1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘 못된 값을 입력했습니다. 한 자리 숫자만 입력하세요")
# except bignumbererror as err:
#     print("에러가 발생하였습니다. 한 자리의 숫자만 입력하세요.")
#     print(err)

# finally
# class bignumbererror(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요"))
#     num2 = int(input(" 두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise bignumbererror("입력 값 : {0},{1}".format(num1,num2))
#     print("{0}/{1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("잘 못된 값을 입력했습니다. 한 자리 숫자만 입력하세요")
# except bignumbererror as err:
#     print("에러가 발생하였습니다. 한 자리의 숫자만 입력하세요.")
#     print(err)
# finally :
#     print("계산기를 이용해 주셔서 감사합니다")

# 모듈 
# import module
# module.price(3) # 3명이서영화
# module.price_morning(4)
# module.price_soldier(5)

# import module as mv
# mv.price_soldier(3)
# mv.price_morning(4)

# from module import *
# price(3)
# price_morning(4)

# from module import price,price_morning
# price(5)
# price_morning(6)

# 패키지  : 모듈들을 모아놓은 집합
# import travel.thailand
# trip_to = travel.thailand.thailandpackage()
# trip_to.detail()

# from travel.thailand import thailandpackage
# trip_to = thailandpackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.vietnampackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.vietnampackage()
# trip_to.detail()

# 패키지 모듈 위치

import inspect
import random
print(inspect.getabsfile(random))
print(inspect.getabsfile(thailand))