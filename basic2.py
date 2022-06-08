# print("강아지" + "고양이")
# print("반가워요" * 20)
# print("100" + "200")
# print(100 + 200)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.forward(100)
# t.left(90)
# t.forward(50)
# t.right(90)
# t.forward(100)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# print("안녕 한동근")
# print("프로그래밍 공부를 즐기셨으면 합니다")
# print("안녕" *3 )

# import turtle

# colors = ["red", "purple", "blue", "green" "yellow", "orange"]
# t = turtle.Turtle()

# turtle.bgcolor("black")
# t.speed(0)
# t.width(3)
# length = 10

# while length < 500:
#     t.forward(length)
    
#     44번째줄 오류 이유 모르겠음t.pencolor(colors[length%6])
#     t.right (89)
#     length += 5

# x = 100
# x = 200
# y = 300 
# sum = x + y
# print(sum)

# name = "홍길동"
# address = "서울시 종로구 1번지"

# print(name)
# print(address)
 
# x = 100
# y = 200
# sum = x + y

# print( x, "과", y, "의 합은", sum, "입니다" )

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# radius = 100
# t.circle(radius)
# t.fd(30)
# t.circle(radius)
# t.fd(30)
# t.circle(radius)
# t.fd(30)

# x = int(input("첫 번째 정수를 입력하시오: "))

# print(x)30

# x = int(input("첫 번째 정수를 입력하세요:"))
# y = int(input("두 번째 정수를 입력하세요:"))
# sum = x + y
# print(x, "와", y, "의 합은", sum, "입니다")

# name = input("이름을 입력하세요 : ")
# print(name)






# 거북이로 집 그리기

# 터틀 그래픽을 사용하여야 하므로 다음과 같은 코드를 소스 파일에 입력한다
# import turtle
# from typing import Sized
# t = turtle.Turtle()
# t.shape("turtle")

# # 사용자로부터 집의 크기를 받아서 size라는 변수에 저장한다
# # 집의 크기는 정수이므로 input()이 반환하는 문자열을 int()를 통하여 정수로 변환한다
# size = int(input("집의 크기는 어마로 할까요?: "))

# # 집을 그릴 차례이다. 사각형을 다음과 같은 코드로 그린다. 이때 변수 Size를 사용하자
# t.forward(size) # 사이즈만큼 거북이를 전진시킨다
# t.right(90) # 거북이를 오른쪽으로 90도 회전시킨다
# t.forward(size)
# t.right(90)
# t.forward(size)
# t.right(90)
# t.forward(size)

# # 이제 지붕을 그릴 차례이다. 현재 거북이는 위를 보고 있기 때문에 
# # 거부그이를 오른쪽으로 90도 회전시켜서 오른쪽을 보도록 한다.
# t.right(90)

# # 지붕을 그리면 된다. 지붕은 간단히 삼격형으로 그렸다.
# t.forward(size)
# t.left(120)
# t.forward(size)
# t.left(120)
# t.forward(size)
# t.left(120)

# 로봇 기자 만들기
# stadium = input("경기장은 어디입니까? : ")
# winner = input(" 승리팀은 어디입니가? : ")
# loser = input(" 패배팀은 어디입니까? : ")
# mvp = input( " 우수 선수는 누구입니까? :")
# score = input("스코어는 무엇입니까? : ")

# 변수와 문자열을 연결하여 기사를 작성한다
# print("")
# print("=======================")
# print("오늘", stadium, "에서 경기가 열렸습니다")
# print(winner, "와", loser, "는 치열한 경기를 평쳤습니다")
# print(mvp, "가 맹활약을 펼쳤습니다")
# print(winner, "가", loser, "를", score, "로 이겼습니다")
# print("=========================")

# print(7/4)
# print(7//4)

# p = int(input("분자를 입력하세요"))
# q = int(input("분모를 입력하세요"))

# print ( p // q )
# print ( p % q)

# sec = 100
# min = 1000 // 60
# remainder = 1000 % 60
# print(min, remainder)

# 거북이를 이용해서 다각형 그리기

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# n = int(input( "몇각형을 그리시겠어요? :" ))

# for i in range(n) :
#     t.forward(100)
#     t.left(360//n)

# 자동 판매기 프로그램

# money = int(input("투입한 돈: "))
# price = int(input("물건 값: "))

# change = money - price
# print("거스름돈 :", change)
# coin500 = change // 500
# change = change % 500
# coin100 = change // 100

# print("500원 동전 개수 :",  coin500)
# print("100원 동전 개수 :", coin100)

# 지수 연산자는 다른 연산자보다 우선순위이다
# 원리금 합계를 복리로 계산하는 식을 만들어 보자

# 원금
# a = 

# 이자율
# r = 

# n년 후에 원리금 합계 
# b = a(1+r)^n

# a = 1000
# r = 0.05
# n = 10

# print(a*(1+r)**n)

#대입 연산자
# x = 100 + 200
# x = y = 100

#복합연산자

# num = num + 2

# num += 2

# x +=y = x = x + y

# x -=y = x = x - y   

# x *=y = x = x * y

# x /=y = x = x / y

# x %=y = x = x % y



# 숫자를 문자로 변환하기 

# print('나는 현재' + str(21) + '살이다' ) 

# price = 10000

# print("상품의 가격은 %s원 입니다" % price)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "이름을 입력하시오: ")
# t.write("안녕하세요" + s + "씨 인사 드립니다")

# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

# s = "monty python"
# print(s[6:10])

# message = 'doesn\'t'
# print(message)

# 2050 년에는 몇살이 될까 ?

# import time

# now = time.time()

# thisyear = int(1970 + now //(365*24*3600))

# age = int(input("몇살이세용:"))
# print(thisyear)

# print(age + (2050 - thisyear))

# 리스트 : 여러 개의 자료들을 모아서 하나의 묶음으로 저장 할 수 있다.

# slist = ['영어', '수학', '사회', '과학']

# list1 = [1,2,3,4,5,6]

# list2 = ['a','b','c','d']

# print(slist)

# list.append 함수 = 빈 리스트 안에 값을 추가하는 함수입니다.

# list = []
# list.append(1)
# list.append(3)
# list.append(4)
# list.append(5)
# list.append(6)
# list.append(7)

# print(list)

# 리스트 값 출력하기
# slist = ['서현식', '황기운', '한동훈', '한동근', '강기모']
# print(slist[0])

# 예제 친구들의 리스트 생성하기
# friend_list = []

# friend = input('친구의 이름을 입력하시오: ')
# friend_list.append(friend)
# print(friend_list)

# 리스트에 저장 된 색상으로 거북이 원 그리기

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# # 리스트를 사용하여 문자열을 저장한다

# color_list = [ "yellow", "red", "blue", "green"]

# t.fillcolor(color_list[0]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(50)
# t.fillcolor(color_list[1]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(50)
# t.fillcolor(color_list[2]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.forward(50)
# t.fillcolor(color_list[3]) # 채우기 색상
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# 우리가 프로그램을 작성 할 때 사용 할 수 있는 3가지의 기본 제어 구조가 있다

# 순차구조 - 명령들을 순차적으로 실행하는 구조
# 선택구조 - 둘 중의 하나의 명령을 선택하여 실행되는 구조이다.
# 반복구조 - 동일한 명령이 반복되면서 실행되는 구조이다

# 1. 선택구조 
# 선택주ㅗ는 질문 한 후에 결정을 내리는 것이다
# (ex) 게임에서 이긴 철수  점수 1 증가
#      파일이 디스크에 없으면 오류 출력 등


# score = int(input("성적을 입력하세요: "))
# if score >= 60:
#     print("합격입니다")
#     print("서현식입니다")
# else:
#     print("불합격입니다")
    
# num = int(input("정수를 입력하세요:"))

# if num % 2 == 0 :
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# 정수 부호에 따라 거북이를 움직이자

# import turtle
# t= turtle.Turtle()
# t.shape("turtle")

# t.penup() # 펜을 올려 그림이 그려지지 않게 한다
# t.goto(100 ,100)
# t.write("거북이가 여기로 오면 양수 입니다")

# t.goto(100 ,0)
# t.write("거북이가 여기로 오면 0 입니다")

# t.goto(100 ,-100)
# t.write("거북이가 여기로 오면 음수 입니다")

# t.goto(0,0) # 이 좌표로 거북이를 이동시킨다
# t.pendown() # 펜을 내려서 그림이 그려지게 한다
# s  = turtle.textinput("", "숫자를 입력하시오 :")

# n =int(s)

# if( n>0):
#     t.goto(100,100)
# if (n == 0):
#     t.goto(100,0)
# else:
#     t.goto(100,-100)

# 거북이  제어하기
# l 입력하면 왼쪽으로 100픽셀 이동 r 누르면 오른쪽으로 100픽셀 이동한다
# 반복문을 이용한다

# import turtle
# t =turtle.Turtle()
# t.width(3) 
# t.shape("turtle")  # 커서 모양을 거북이로 한다
# t.shapesize(3,3)

# while True:
#     a = input("명령어를 입력하시오: ")
#     if a == "l":
#         t.left(90)
#         t.forward(100)
#     if a == "r":
#         t.right(90)
#         t.forward(100)

# 윤년만들기 
# year = int(input("년도를 입력하세요:"))

# if ((year % 4 ==  0 and year % 100 != 0) or year % 400 == 0):
#     print(year, "년은 윤년입니다.")

# else :
#     print(year, "년은 윤년인 아닙니다.")

# 동전 던지기 게임

# import random
# coin = random.randrange(2)
# if coin == 0:
#     print("앞면입니다")
# else:
#     print("뒷면입니다")
# print("게임이 종료되었습니다.")


# num = int(input("정수를 입력하시오: "))

# if num > 0 :
#     print("양수입니다")
# elif num == 0 :
#     print("0입니다")
# else:
#     print("음수입니다")


# 종달새가 노래할까 ?

# import random
# time = random.randint(1, 24)
# sunny = random.choice([True,False])
# if sunny:
#     print("날씨 좋음")
# else:
#     print("날씨 안좋음")

# if time >=6 and time <9 and sunny:
#     print("종달새가 노래합니다")
# else:
#     print("종달새가 노래하지 않습니다")


# 팁 : random.randint 는 a가 최소 b가 최대의 범위가 된다
#     random.randrange는 a가 최소 b-1가 최대의 범위가 된다

# 중첩 if문
# num = int(input("정수를 입력하세요 "))
# if num >= 0:
#     if num == 0:
#         print("0입니다")
#     else:
#         print("양수입니다")
# else:
#     print("음수입니다")

# 아이디 확인
# id = rldns3457
# s = input("아이디를 입력하세요")
# if id == s:
#     print("환영합니다")
# else:
#     print("아이디를 찾을 수 없습니다")

# 패널티킥
# import random

# option = ["왼쪽", "가운데", "오른쪽"]
# computechoice = random.choice(option)

# userchoice = input("어디를 수비하시겠어요 ?")

# if computechoice == userchoice:
#     print("수비성공")
# else:
#     print("성공")


# 도형 그리기
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("","도형을 입력하세요 :")
# if s == "사각형":
#     s = turtle.textinput("", "가로:")
#     w = int(s)
#     s = turtle.textinput("", "세로")
#     h = int(s)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
#     t.left(90)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
    
    # 반복문 
    # 횟수 제어 반복 : 정해진 횟수만큼 반복
    # 조건 제어 반복 : 조건이 만족해지면 계속 반복

# for i in [1,2,3,4,5]:
#     print("나는 서현식")

# for i in [1,2,3,4,5]:
#     print("i=", i)

# for i in[1,2,3,4,5]:
#     print("9*", i, "=", 9*i)

# 반복해야 하는 횟수가 큰 경우 range를 이용하자

# for i in range(5):
#     print(i)

# range() 함수는 숫자들을 생산하는 공장으로 생각하면 된다.

# range(start,stop,step)
# ex) 
# for i in range(10,0,-1):
#     print(i)

# 6개의 원 그리기
# 터틀을 60도만틈 회전시키면서 화면에 6개의 원을 그려보자
# (1) 반복 사용 x
# import turtle
# t =turtle.Turtle()
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)

# (2) 반복문 사용
# import turtle
# t = turtle.Turtle()
# for count in range(6):
#     t.circle(100)
#     t.left(360/6)

# 반복을 사용하여 도형을 그려보자 !

# import turtle
# t= turtle.Turtle()
# t.shape("turtle")

# # 정삼각형
# for i in range(3):
#     t.forward(100)
#     t.left(360/3)

# t.penup()
# t.goto(200,0)
# t.pendown()

# for i in range(4):
#     t.forward(100)
#     t.left(360/4)

# n각형 그리기 정수 n을 받아서 n각형을 그려보자

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("","몇각형?")
# n = int(s)

# for i   in range(n):
#     t.forward(100)
#     t.left(360/n)

# 거북이를 랜덤하게 움직이게 하자
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# import random

# for i in range(30):

#     number = random.randint(1,100)
#     t.forward(number)
#     angle = random.randint(-180, 180)
#     t.right(angle)

# 팩토리얼 계산하기

# n = int(input("정수입력해"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(n, "!은", fact, "이다")

# 조건 제어 반복 : 조건이 참이면 계속 반복된다.

# a = "" 
# while a != "ok":
#          a = input("엄마 다 됐어? :")
# print("먹자")


# password = ""
# while password != "rldns":
#     password = input("암호를 입력하시오: ")
# print("로그인 성공")

# count = 1
# sum = 0
# while count <= 10:
#     sum = sum + count
#     count = count + 1
# print("합은" , sum)

# 사각형 그리기

# import turtle
# t = turtle.Turtle()


# i = 0
# while i < 4:
#     t.forward(100)
#     t.right(90)
#     i = i +1

# 구구단 출력
# from typing import IO


# dan = int(input("원하는 단은 ? : "))
# i = 1

# while i <= 9:
#     print("%s*%s=%s" %(dan, i, dan * i))
#     i = i + 1



# 별을 그려보자 !
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# i = 0

# while i < 5:
#     t.forward(50)
#     t.right(144)    
#     i= i+1

# 스파이럴을 그려보자 ! 
# import turtle
# 색상을 리스트에 저장한 후 하나씩 꺼내서 변경해보자
# color = ["red", "purple", "blue", "green", "yellow", "orange"]
# t = turtle.Turtle()

#배경색을 변경해보자 !
# turtle.bgcolor("black")
# 거북이의 속도를 바꾸어 보자 !
# t.speed(0)

# 거북이 선의 두께를 설정해 보자 !
# t.width(3)

#선의 길이를 설정해보자 !
# length = 10
# while length < 500: 
    # t.forward(length)
    # t.pencolor(color[length%6])
    # t.right (89)
    # length += 5

# 사용자가 입력하는 숫자의 합 계산하기

# total = 0 
# answer = "yes"
# while answer == "yes":
#     number = int(input("숫자를 입력하세요:"))
#     total = total + number
#     answer = input("계속?(yes/no): ")
# print("합계는 :", total)

# 숫자 맞추기 게임을 해보자 !

# import random
# tries = 0 
# guess = 0
# answer = random.randint(1, 100)

# print("1부터 100 사이의 숫자를 맞추시오")

# while guess != answer:
#     guess = int(input("숫자를 입력하시오:"))
#     tries = tries + 1
#     if guess < answer:
#         print("낮음")
#     elif guess > answer:
#         print("높음")
    
# if guess == answer:
#     print("축하합니다 시도횟수", tries)
# else:
#     print("정답은", answer)

# 초등생을 위한 산수문제 발생기를 해보자 !

# import random

# while True:
#     x = random.randint(1,100)
#     y = random.randint(1, 100)
#     print(x, "+", y, "=", end = "")
#     answer=int(input()) 
#     if answer == x + y:
#         print("잘했어요")
#     else:
#         print("다음엔 더 잘하자")

# 모든 샌드위치 종류를 출력해보자 !
# breads = ["호밀빵", "위트", "화이트"]
# meats = ["미트볼", "소시지", "닭가슴살"]
# vegis = ["양상추", "토마토", "오이"]
# sauces = ["마요네즈", "머스타드", "케찹"]

# for b in breads:
#     for m in meats:
#         for v in vegis:
#             for s in sauces:
#                 print(b+m+v+s)

# 무한루프와 break!
# while True:
#     light = input(int("색상을 입력하세요"))
#     if light == "blue":
#         break
# print("앞으로 가세요 ")

# 터틀 그래픽을 이용하여  시계 그리기 ! 
# import turtle
# t = turtle.Turtle()
# t.color("black")
# ///지정 위치에 거북이를 찍을 수 있다
# t.stamp()    
# move = 30

# for i in range(12):
    # t.penup()
    # t.forward(50)
    # t.pendown()
    # t.penup()
    # t.forward(25)
    # t.pendown()
    # t.penup()
    # t.forward(15)
    # t.pendown()
    # t.stamp()
    # t.home()
    # t.right(move)
    # move = move + 30

    # 점치는 게임을 만들어보자 !
    
# import sys
# import random

# while True:
#     name = input("이름 : (종료하려면 엔터키)")
#     if name == "":
#         sys.exit()
# question = input("알고싶은게 무엇이냐:")
# print(name + "님", question, "에 대해 질문하셨군요")
# print("주사위를 굴려보자")

# answer = random.randint(1, 3)

# if answer == 1:
#     print("네")
# elif answer == 2:
#     print("굿")
# else:
#     print("그건 별로임")


# 함수란 ? 
# 프로그램은 점점 복잡하고 커지기 때문에 이해하기 쉽고 관이하기 쉽도록 
# 작은 조각으로 나누어서 조직화할 필요가 있다
# 쪼개는 3가지의 방법
# 함수 = 반복적인 코드를 묶음
# 객체 = 코드중에서 독립적인 단위로 분리 가능
# 모듈 = 프로그램의 일부를 가지고 있다, 함수를 묶음

# def print_address():
#     print("서현식")
#     print("슈퍼서현식")
#     print("왕돼지서현식")

# 함수호출하기 :
# print_address()

# 함수에 값을 전달할 수 있다. 이것을 인수라고한다
# def a(name):
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#     print(name)

# a("서현식")

# 값 반환하기  함수로부터 되돌아 오는 값
# def calculate_area(radius):
#     area = 3.14 * radius **2
#     return area

# c_area = calculate_area(5.0)
# print(c_area)

# 함수에 여러 개의 입력 전달하기
# 함수로 여러 개의 값을 전달하는 방법을 살펴보자. 두개의 정수 start와 end를 받아서 stat

# def get_sum(start,end):
#     sum = 0
#     for i in range(start, end+1):
#         sum = sum + i
#     return sum

# print(get_sum(1,10))

# 사각형을 그리는 함수를 작성해보자!
# import turtle

# # 함수를 정의하자!
# t = turtle.Turtle()
# t.shape("turtle")

# def square(length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)

# t.up()
# t.goto(-200,0)
# t.down()
# square(100)

# t.up()
# t.goto(0,0)
# t.down()
# square(100)

# t.up()
# t.goto(200,0)
# t.down()
# square(100)

# n각형을 그리는 함수를 작성해보자 !

# import turtle
# t = turtle.Turtle()

# def a(n,length):
#     for i in range(n):
#         t.forward(length)
#         t.left(360//n)

# for i in range(10):
#     t.left(20)
#     a(6,100)

# 지역변수 : 함수 안에서 생성되는 함수
# 전역변수 : 잘 아시죠잉

# 함수 안에서 전역변수를 사용해보자 !

# def calculate_area(radius):
#     result = 3.14 * radius **2
#     return result

# r = float(input("원의반지름 : "))
# area = calculate_area(r)
# print()

# def cacculate_area(radious):
#     area = 3.14 * radious **2 
#     return

# area = 0 
# r = float(input("원의 반지름:"))
# cacculate_area(r)
# print(area)

# def calculate_area(radius):
#     global area
#     area = 3.14 * radius **2
#     return

# area = 0
# r = float(input("원의 반지름:"))
# calculate_area(r)
# print(area)

# 디폴트 인수 = 매개변수가 가지는 기본 값

# def greet(name, msg="별일없죠?"):
#     print("안녕", name + msg)
    
# greet("영희")

# 키워드 인수 : 인수 앞에 키워드를 두어서 인수들을 구분한다 키워드 인수는
#               인수의 이름을 ㅁ여시적으로 지정해서 전달하는 방법이다

# def calc(x,y,z):
#     return x+y+z

# calc(10,20,30)
# print(calc)
# calc(y=20,x=30,z=50)
# print(calc)

# 클릭하는곳에 사각형을 그려보자 ! (콜백함수 이용 )

# import turtle
# t = turtle.Turtle()

# def square(length):
#     for i in range(4):
#         t.forward(length)
#         t.left(90)

# # 마우스가 클릭 된 곳에 사각형을 그리는 함수을 정의한다.
# def drawit(x,y):
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.begin_fill()
#     t.color("green")
#     square(50)
#     t.end_fill()

# s = turtle.Screen()
# s.onscreenclick(drawit)

# 마우스로 그림을 그려보자 !
# import turtle
# t = turtle.Turtle()

# def draw(x,y):
#     t.turtle.goto(x,y)

# t.shape("turtle")
# t.pensize(10)
# s = turtle.Screen()
# s.onscreenclick(draw)

# s.onkey(t.penup(), "up")
# s.onkey(t.pendown(), "down")
# s.listen() #키보드 이벤트를 기다린다

# 나무를 그려보자 !
# 함수는 내부에서 자기자신을 다시 호출 할 수 있는데 이것을 순환호출 이라 한다 !
# import random
# import turtle



# def tree(length):
#     if length > 5:
#         t.forward(length)
#         t.right(20)
#         tree(length-15)
#         t.left(40)
#         tree(length-15)
#         t.right(20)
#         t.backward(length)

# t = turtle.Turtle()
# t.left(90)

# t.color("green")
# tree(90)
# t.speed(1)

# 막대 그래프를 그려보자! 

# import turtle # 왜 안되는지 모르겟음 ..


# def drawBar(height):
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write(str(height)), font = ('Times New Roman', 16, 'bold')
#     t.right(90)

#     t.forward(90)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()

# data = [120,56,309,156,23,98]

# t = turtle.Turtle()
# t.color("blue")
# t.fillcolor("red")

# t.pensize(3)

# for d in data:
#     drawBar(d)

# 이것도 왜 안되는지 모르겠음
# import random
# import turtle

# t = turtle.Turtle()
# screen = turtle.Screen()
# screen.onkey(turn_right,"right")
# screen.onkey(turn_left,"left")
# t.shape("turtle")
# t.speed(0)

# x,y 위치에 미로를 그리는 함수
# def draw_maze(x,y):
#     for i in range(2):
#         t.penup()
#     if i ==1:
#         t.goto(x+100,y+100)
#     else:
#         t.goto(x,y)
#     t.pendown()
#     t.forward(300)
#     t.right(90)
#     t.forward(300)
#     t.left(90)
#     t.forward(300)

# def turn_left():
#     t.left(10)
#     t.forward(10)

# def turn_right():
#     t.right(10)
#     t.forward(10)

# t.penup()
# t.goto(-300,-250)
# t.speed(1)
# t.pendown
# screen.listen
# screen.mainloop

# 지금까지 배운것을 이용해서 프로그램을 만들어 보자

# 난수 발생하기 : 난수는 게임과 시뮬레이션에 필수적이다. 모듈을 통하여 발생시켜보자

# import random
# 가장 기본이 되는 함수는 random() 이다. random 모듈 안에 있는 random() 함수를 호출하려면
# random.random()으로 적어야 한다
# random.random() # 0.0 부터 1.0보다 작은 실수 난수
# 정수 구간의 난수가 필요하다면 random.randint(a,b) 사용한다
# random.randint(1,100)

# 문자열이나 리스트 안에서 랜덤하게 하나의 항목을 선택하려면 random.choice(seq) 함수 사용
# random.choice(aadasdas)
# items = [1,23,4,6]
# random.shuffle(items) # 항목들을 섞는 기능을 한다
# items
# print(items)

# 거북이 경주 게임을 만들어 보자 !
# import turtle
# t1 = turtle.Turtle() 
# t2 = turtle.Turtle()

# t1.color("pink")
# t1.shape("turtle")
# t1.shapesize(5)
# t1.pensize(5)

# t2.color("blue")
# t2.shape("turtle")
# t2.shapesize(5)
# t2.pensize(5)

# t1.penup()
# t1.goto(-300,0)

# t2.penup()
# t2.goto(-300, 100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(2)

# for i in range(100):
#     d1 = random.randint(1,60)
#     t1.forward(d1)
#     d2 = random.randint(1,60)
#     t2.forward(d2)

# 애니메이션을 만들어 보자 !
# 터틀 그래픽을 이용하여 태극무늬를 만들어보자

# import turtle


# def draw_shape(radius, color1):
#     t.left(270)
#     t.width(3)
#     t.color("black", color1)
#     t.begin_fill()
#     # t.circle(20,-180)
#     t.circle(radius/2.0, -180)
#     t.circle(radius, 180)
#     t.left(180)
#     # t.circle(-radius/2.0, -180)
#     t.end_fill()

# t = turtle.Turtle()
# t.reset()
# draw_shape(200,"red")
# t.setheading(180)
# draw_shape(200,"blue")

# 왜 안되는지 모르겠음 
# import turtle
# import random
# import math

# player = turtle.Turtle()
# player.color("blue")
# player.shape("turtle")
# player.penup()
# player.speed(0)
# screen = player.getscreen()

# al = turtle.Turtle()
# al.color("red")
# al.shape("circle")
# al.penup()
# al.penup()
# al.speed(0)
# al.goto(random.randint(-300, 300), random.randint(-300, 300))

# a2 =turtle.Turtle()
# a2.color("red")
# a2.penup()
# a2.pendown()
# a2.speed(0)
# a2.goto(random.randint(-300,300),random.randint(-300,300))

# def turnleft():
#     player.left(30)

# def turnright():
#     player.right(30)

# screen.onkeypress(turnleft, "Left")
# screen.onkeypress(turnright, "Right")
# screen.listen()

# def play():
#     player.forward(2)
#     al.forward(2)
#     a2.forward(2)
#     screen.ontimer(play,10)
# screen.ontimer(play,10)

# 앵그리 터틀 게임 해보기 !
# 이것도 왜 안되는지 모르겠음 ..

# import turtle
# import math

# player = turtle.Turtle()
# player.shape("turtle")
# screen = player.getscreen()

# def turnleft():
#     player.left(5)

# def turnright():
#     player.right(5)

# def fire():
#     x = 0
#     y = 0
#     velocity = 50 # 초기속도
#     angle = player.heading()
#     vx = velocity * math.cos(angle * 3.14 / 180.0)
#     vy = velocity * math.sin(angle * 3.14 /180.0)
#     while player.ycor() >= 0 : #y 좌표가 음수가 될 때 까지
#         vx = vy
#         vy = vy -10
#         x = x + vx
#         y = y + vy
#         player.goto(x,y)

# screen.onkeypress(turnleft, "Left")
# screen.onkeypress(turnright, "Right")
# screen.listen()

# 암호화 , 복호화

# text = "did vp " #평문

# encrypted_text =""
# for c in text:
#     x = ord(c) # 글자의 코드 값 구함
#     x= x+1
#     cc = chr(x) #증가된 코드값에 해당하는 문자 계산
#     encrypted_text = encrypted_text + cc
# print(encrypted_text) # 암호화된 값은 eje!wq!

# encrypted_text = "eje!wq!"
# text = ""
# for c in encrypted_text:
#     x=ord(c)
#     x = x-1
#     cc =chr(x)
#     text = text +cc
# print(text) 

# import qrcode


# a = qrcode.make("eje!wq!")
# a.save("C:\Users\User\python")
# print(type(img))
# print(img.size)

# 리스트와 딕셔너리

# numbers = [1,2.3,4,5]
# heros = []
# heros.append("아이언맨")
# heros.append("닥터스트레인지")

# 파이썬에서 모든 것은 객체 이다. 객체란 관련된 변수와 함수를 묶은 것이다.
# 리스트도 객체이다. 객체안에 무엇인가를 사용할 때는 객체의 이름 을 쓰고 점을 붙
# 인후 함수의 이름을 찍는다

# 리스트는 혼성 리스트도 가능하다!
# 리스트에 접근해보자!
# letters= ['a','b','c','d']
# # 리스트에서 하나의 항목에 접근할 때는 인덱스를 사용한다. 인덱스란 리스트에서 항목
# # 위치번호 이다.
# print(letters[0])

# 슬라이싱 : 리스트에서 여러가지의 항목을 추출한다 !
# letters= ['a','b','c','d']
# print(letters[0:3])
# print(letters[:3])
# print(letters[3:])
# print(letters[:])

# 리스트에 저장된 항목을 변경해보자 !
# heros = ['아이언맨','토르','헐크','서현식']
# heros[1] = '닥터 스트레인지'
# print(heros)
# heros.append("스파이더맨")
# heros.insert(1,"배트맨")
# print(heros)

# 리스트의 항목을 삭제해보자 !
# heros = ['아이언맨','토르','헐크','서현식']
# heros.remove("서현식")
# print(heros)

# del heros[0] # del은 인덱스를 이용하여 삭제한다
# print(heros)

# a = heros.pop() # 리스트 마지막 항목을 지우고 반환함
# print(heros)
# print(a)

# 리스트를 탐색해보자 !
# heros = ['아이언맨','토르','헐크','서현식']
# print(heros.index("헐크"))
# if "헐크" in heros:
#     print(heros.index("헐크"))
# for hero in heros:
#     print(hero)

# 리스트를 정렬해보자!
# heros = ['아이언맨','토르','헐크','서현식']
# heros.sort()
# print(heros)
# number = [9,8,7,6,5]
# number.sort()
# print(number)
# a = sorted(number,reverse=True)
# print(a)

# 오늘의 속담을 만들어보자 ! 
# import random
# quotes = []


# quotes.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다")
# quotes.append("분노는 바보들의 가슴속에만 살아간다")
# quotes.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다")
# quotes.append("사람은 사랑할 때 누구나 시인이 된다")
# quotes.append("시작이 반이다")

# dailiyQUOTE = random.choice(quotes)
# print(dailiyQUOTE)

# 오륜기를 그려보자 ! 왜 안되는지 모르겠음
# import turtle
# t = turtle.Turtle()

# def draw_olympic_symbol():
#     position = [[0,0,"blue"],[-120,0,"purlple"],[60,60,"red"],[-60,60,"yellow"],[-180,60,"green"]]
#     for x,y,c in position:
#         t.penup()
#         t.goto(x,y)
#         t.pendown()
#         t.color(c,c)
#         t.begin_fill()
#         t.circle(30)
#         t.end_fill()

# t = turtle.Turtle
# draw_olympic_symbol()

# 에스터 로드 게임을 업그레이드 해보자 !
# import turtle
# import random
# import math

# player = turtle.Turtle()
# player.color("blue")
# player.shape("turtle")
# player.penup()
# player.speed(0)
# screen = player.getscreen()

# asteroid = []
# for i in range(10):
#     a1 = turtle.Turtle()
#     a1.color("red")
#     a1.shape("circle")
#     a1.penup()
#     a1.speed(0)
#     a1.goto(random.randint(-300,300),random.randint(-300,300))
#     asteroid.append(a1)

# def turnleft():
#     player.left(30)

# def turnright():
#     player.right(30)

# screen.onkeypress(turnright,"Right")
# screen.onkeypress(turnleft,"Left")
# screen.listen()

# def play():
#     player.forward(2)
#     for a in asteroid: #리스트에 저장된 모든 터틀에 대하여
#         a.right(random.randint(-180,180))
#         a.forward(2)

#     screen.ontimer(play,10)
# screen.ontimer(play,10)

# 딕셔너리를 만들어 보자
# 딕셔너리는 리스트와 같이 값을 저장하는 방법이다 .하지만 딕셔너리에는 값(VALUE)에 관련된 key가 있다. 
# 주소록에서는 사람의 이름이 키가 되고 전화번호가 값이 된다
# phone_book = { }
# phone_book["홍길동"] = "010-1234-56789"
# phone_book["강감찬"] = "010-123-489"
# phone_book["서현식"] = "010-89-165"

# print(phone_book)
# print(phone_book["강감찬"])
# print(phone_book.keys())
# print(phone_book.values())

# dict = {'name':'홍길동', "age":'7'}
# print(dict['name'])
# 딕셔너리[key] = 키값에 해당하는 밸류값 불러옴
# 딕셔너리의 모든 항목을 반복하면서 출력해보자 for문을 이용해라
# phone_book = { }
# phone_book["홍길동"] = "010-1234-56789"
# phone_book["강감찬"] = "010-123-489"
# phone_book["서현식"] = "010-89-165"
# for key in sorted(phone_book.keys()):
#     print(key,phone_book[key])

# del phone_book["홍길동"]
# phone_book.clear()

# 딕셔너리를 이용해 편의점 재고 관리를 해보자 ! 
# items = {"커피음료" : 7, "펜":3, "종이컵" : 6}
# item = input("물건의 이름은 ?")
# print(items[item])

# 영한사전을 만들어보자 !
# english = dict()
# english['one'] = '하나'
# english['two'] = '둘'
# word = input("단어를 입력하세요")
# print(english[word])

# 이메일을 보내보자 ! 
# import smtplib
# from email.mime.text import MIMEText

# me = "rlaejrqo465@naver.com"
# you = "rare813@gmail.com"
# contents = "지건"

# msg = MIMEText(contents, _charset="euc_kr")
# msg['subjedt'] = "동창회 모임"
# msg["from"] = me
# msg['to'] = you

# server = smtplib.SMTP('rlaejrqo465@gmail.com', 587) #이부분 오류나는데 원인 모름
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login('아이디','패스워드')
# server.send_message(me,you,msg.as_string())
# server.quit

# 윈도우 버튼을 생성해보자 !
# from tkinter import * #tkinter 안에 있는 모든 함수를 포함시켜라
# window = Tk() # 하나의 창 생성
# button = Button(window, text="클릭하세요") #첫번쨰는 최상위 매개변수 window가 전달
# button.grid() # 버튼을 최대한 압축하여 윈도웅 ㅔ표시
# window.mainloop() # 윈도우에서 발생하는 여러가지 이벤트 처리

# 엔트리와 레이블 위젯을 사용해보자 ! 
# from hashlib import blake2b
# from tkinter import *

# window = Tk()

# l1 = Label(window, text="서현식")
# l2 = Label(window, text="한동근")
# l1.grid()
# l2.grid()

# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid()
# e2.grid()

# b1 = Button(window, text="서현식->한동근")
# b2 = Button(window, text="한동근->서현식")
# b1.grid()
# b2.grid()

# window.mainloop()

# text = "did vp " #평문

# encrypted_text =""
# for c in text:
#     x = ord(c) # 글자의 코드 값 구함
#     x= x+1
#     cc = chr(x) #증가된 코드값에 해당하는 문자 계산
#     encrypted_text = encrypted_text + cc
# print(encrypted_text) # 암호화된 값은 eje!wq!

# 격자 배치 관리자를 이용해보자 !
# from hashlib import blake2b
# from tkinter import *

# window = Tk()

# l1 = Label(window, text="서현식")
# l2 = Label(window, text="한동근")
# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)

# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# b1 = Button(window, text="서현식->한동근")
# b2 = Button(window, text="한동근->서현식")
# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# window.mainloop()

# 버튼 이벤트를 처리해보자 !
# from tkinter import * 
# def process():
#     print("나는 서현식!")

# window = Tk()
# button = Button(window, text="안녕하세요", command=process)
# button.pack()
# window.mainloop()

# 버튼 이벤트를 처리해보자 ! 2
# from tkinter import *

# def process():
#     e2.insert(0, "100")

# window = Tk()

# l1 = Label(window, text="화씨")
# l2 = Label(window, text="섭씨")
# l1.grid(row=0, column=0)
# l1.grid(row=0, column=0)

# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# b1 = Button(window, text="화씨->섭씨", command=process)
# b2 = Button(window, text="섭씨->화씨")
# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# window.mainloop()

# 버튼 이벤트를 처리해보자 ! 3
# from tkinter import *

# def process():
#     temperture = float(e1.get())
#     mytemp = (temperture-32)*5/9
#     e2.insert(0, str(mytemp))

# window = Tk()

# l1 = Label(window, text="화씨")
# l2 = Label(window, text="섭씨")
# l1.grid(row=0, column=0)
# l2.grid(row=1, column=0)

# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# b1 = Button(window, text="화씨->섭씨", command=process)
# b2 = Button(window, text="섭씨->화씨")
# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# window.mainloop()

# 위젯의 색상과 폰트를 변경해보자 ! 
# from tkinter import *

# def process():
#     temperture = float(e1.get())
#     mytemp = (temperture-32)*5/9
#     e2.insert(0, str(mytemp))

# window = Tk()

# l1 = Label(window, text="화씨", font='helvetica 16 italic')
# l2 = Label(window, text="섭씨", font='helvetica 16 italic')
# l1.grid(row=0, column=0)
# l2.grid(row=1, column=0)

# e1 = Entry(window, bg="yellow", fg="white")
# e2 = Entry(window, bg="yellow", fg="white")
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# b1 = Button(window, text="화씨->섭씨", command=process)
# b2 = Button(window, text="섭씨->화씨")
# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# window.mainloop()

# 절대위치 배치 관리자 : 절대위치를 사용하여 위젯을 배치한다 x와 y매개변수 이용
# from tkinter import *
# import tkinter
# window = ()
# w = Label(window, text="서현식", bg="red", fg="blue")
# w.place(x=0,y=0)
# w = Label(window, text="한동근", bg="red", fg="blue")
# w.place(x=20,y=20)
# w = Label(window, text="한동훈", bg="red", fg="blue")
# w.place(x=40, y=40)
# window.mainloop()

# 이미지 표시 프로그램 : 레이블의 속성 image를 이용하여 레이블 안에 이미지를 표시해보자!
# from tkinter import * # 왜 안되는지 모르겠음

# def change_img():
#     path = inputBox.get()
#     img = PhotoImage(file= path)
#     imageLabe1.configure(image = img)
#     imageLabe1.image = img

# window = Tk()

# phote = PhotoImage(file="wl.gif")
# imageLabe1 = Label(window, image=phote)
# imageLabe1.pack

# inputBox = Entry(window)
# inputBox.pack()

# button = Button(window, text="서현식", command=change_img)
# button.pack()

# window.mainloop()

# MyPaint 프로그램 윈도우의 그림판과 비슷한 프로그램 
# from os import path #왜 안되는지 모르겠음 ...
# from tkinter import *
# mycolor = "blue"
# def paint(event):
#     x1, y1 = (event.x-1),(event.y-1)
#     x2, y2 = (event.x-1),(event.y-1)
#     Canvas.create_oval(x1,y1,x2,y2, fill=mycolor)

# def chnage_color():
#     global mycolor
#     mycolor="red"

# window = Tk()
# Canvas = Canvas(window)
# Canvas.pack()
# Canvas.bind("<B1-motion>", paint)
# button = Button(window, text="빨간색", command=chnage_color)
# button.pack()
# window.mainloop()

# 계산기를 만들어 보자 !
# 1 . 엔트리 위젯
# button_list = ['7','8','9','/','c',
#                 '4','5','6','*',' ',
#                 '1','2','3','-',' ',
#                 '0','.','=','+',' ']

# from tkinter import *
# window = Tk()
# window.title("서현식")
# display = Entry(window, width=33,bg="yellow")
# display.grid(row=0,column=0,columnspan=5)

# 버튼을 생성하고 버튼을 격자 모양으로 배치해보자 이것은 반복을 사용한다
# row_index = 1
# col_index = 0
# for button_text in button_list:
#     Button(window, text=button_text, width=5, command= click(button_text)).grid(row=row_index, column=col_index)
#     col_index +=1
#     if col_index > 4:
#         row_index +=1
#         col_index = 0

# window.mainloop()

# 버튼 입력을 처리해보자
# def click(key):
#     display.insert(END,key)

# button_list = ['7','8','9','/','c',
#                 '4','5','6','*',' ',
#                 '1','2','3','-',' ',
#                 '0','.','=','+',' ']

# from tkinter import *
# window = Tk()
# window.title("서현식")
# display = Entry(window, width=33,bg="yellow")
# display.grid(row=0,column=0,columnspan=5)

# row_index = 1
# col_index = 0
# for button_text in button_list:
#     Button(window, text=button_text, width=5, command= click(button_text)).grid(row=row_index, column=col_index)
#     col_index +=1
#     if col_index > 4:
#         row_index +=1
#         col_index = 0

# window.mainloop()

# 버튼을 눌렀을 떄만 함수를 호출한다, 이럴때는 반복문에서 하나의 함수를 정의하고 버튼에 등록을 사용함 !
# for button_text in button_list:
#     def process(t=button_text):
#         click(t)
#     Button(window, text=button_text, width=5, command= click(button_text)).grid(row=row_index, column=col_index)
#     col_index +=1
#     if col_index > 4:
#         row_index +=1
#         col_index = 0

# 전체 소스를 적어보자 !

# from tkinter import *
# window = Tk()
# window.title("서현식")
# display = Entry(window, width=33, bg="yellow")
# display.grid(row=0,column=0,columnspan=5)

# button_list = ['7','8','9','/','c',
#                 '4','5','6','*',' ',
#                 '1','2','3','-',' ',
#                 '0','.','=','+',' ']

# def click(key):
#     if key == '=':
#         result = eval(display.get()) #여기 오류나는데 이유 모르겠음
#         s = str(result)
#         display.insert(END, "=" + s)
#     else:
#         display.insert(END,key)
    
#     display.insert(END,key)



# row_index = 1
# col_index = 0
# for button_text in button_list:
#     def process(t=button_text):
#         click(t)
#     Button(window, text=button_text, width=5, command= click(button_text)).grid(row=row_index, column=col_index)
#     col_index +=1
#     if col_index > 4:
#         row_index +=1
#         col_index = 0
# window.mainloop()

# 파일 사용해보자 !  한번에 읽기
# infile = open("C:\\Users\\User\\Desktop\\phones.txt", "r")
# lines = infile.readlines() #infile.read() 로 바꾸면 가로로 출력됨. 이건 세로얌
# print(lines)
# infile.close()

# 파일 한줄 씩 읽기!
# infile = open("C:\\Users\\User\\Desktop\\phones.txt", "r")
# for line in infile:
#     line = line.rsplit()
#     print(line)
# infile.close()

# 파일에 데이터를 써보자!
# outfile = open("C:\\Users\\User\\Desktop\\phones.txt", "w")
# outfile.write("서현식 1212312\n")
# outfile.close()

# 파일에 데이터를 추가해보자 ! ( 데이터 쓰기랑 비슷한듯 ?)
# outfile = open("C:\\Users\\User\\Desktop\\phones.txt", "a")
# outfile.write("tjgustldd,l;a,das \n")
# outfile.close()

# 파일에서 단어를 읽어보자 ! 
# infile = open("C:\\Users\\User\\Desktop\\phones.txt", "r")
# for line in infile :
#     line = line.rsplit()
#     word_list = line.split()
#     for word in word_list:
#         print(word)
# infile.close()

# 파일을 복사해보자 !
# import shutil
# shutil.copy("d:\\phones.txt", "d:\\temp.txt")
# infilename = input("d:\\phones.txt")
# outfilename = input("d:\\temp.txt")

# infile = open(infilename, "r")
# outfile = open(outfilename, "r")

# s = infile.read() #전체 파일을 읽는다
# outfile.write(s) # 전체 파일을 쓴다

# infile.close()
# outfile.close()

# 행맨 게임을 만들어보자 !
# import random
# guesses = ""
# turns = 10

# infile = open("행맨파일")
# lines = infile.readlines()
# word = random.choice(lines)

# while turns > 0:
#     failed = 0
#     for char in word:
#         if char in guesses:
#             print(char, end="")
#         else:
#             print("-", end="")
#             failed += 1
#     if failed == 0:
#         print("사용자승리")
#         break
#     print("")
#     guess = input("단어 추측하세요")
#     guesses += guess
#     if guess not in word:
#         turns -= 1
#         print("틀림")
#         print(str(turns)+ '기회남음')
#         if turns == 0:
#             print("사용자 패배 정답"+ word)

# infile.close()

# 객체 출력 , 딕셔너리를 저장해보자 ! pickle 모듈 사용, dump로 압축
# gameoption = {"sound": 8, "videoquiality" : "hight", "money" : 100000, "weponlist" : ["gun", "missile", "knife"]}
# import pickle
# file = open("위치경로","w")
# pickle.dump(gameoption,file)
# file.close()

# 다시한번 정리해보자
# pickle 모듈 포함시킨다 , 딕셔너리 생성, wb모드로 파일 연다 dump 함수를 호출하여 딕셔너리 전달, 파일 닫는다
# import pickle
# gameoption = {"sound": 8, "videoquiality" : "hight", "money" : 100000, "weponlist" : ["gun", "missile", "knife"]}
# file = open("위치경로","wb")
# pickle.dump(gameoption,file)
# file.close()

#이진 파을에 저장된 딕셔너리를 읽어보자 !
# import pickle
# file = open("경로", "rb")
# #피클 파일에 딕셔너리 로딩
# obj = pickle.load(file)
# print(obj)

# 팁 from os import open  os 모듈에 있는 open 이란 함수를 import

# 파일 대화상자 ! 
# from tkinter import *
# from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfile

# readfile = askopenfilename()
# if(readfile !=None):
#     infile = open(readfile, "r")

# for line in infile.readlines():
#     line=line.strip()
#     print(line)
# infile.close()
# 메모장을 만들어 보자 !

# from tkinter import *
# import tkinter
# from tkinter import filedialog
# from tkinter.filedialog import askopenfilename
# window = Tk()
# text = Text(window, height=30, width=80) # 메모장 기능을 수행하는 애플리케이션 작성
# text.pack()

# def open():
#     file =  filedialog.askopenfilename(parent=window, mode = 'r')
#     if file != None:
#         lines = file.read()
#         text.insert('1,0', lines)
#         file.close()


# def save():
#     file = filedialog.asksaveasfile(parent=window, mode = 'w')
#     if file != NONE:
#         lines = text.get(1.0, END+'-1C') #파일 이름을 받는다, 위젯에 입력된 내용 파일에 저장, 1.0은 1행 0번째 글자부터 맨 끝에서 한문자만 제거
#         file.write(lines)
#         file.close()
    
# def exit():
#     if Message.askokcancel("QUIT", "종료하시겠습니까"):
#         window.destroy()

# def about():
#     label = Message.showinfo("about", '메모장 프로그램')


# menu = Menu(window)
# window.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label="파일", menu=filemenu)   
# filemenu.add_command(label="열기",command=open)
# filemenu.add_command(label="저장하기",command=save)
# filemenu.add_command(label="종료",command=exit)
# helpmenu = Menu(menu)
# menu.add_cascade(label="도움말", menu=helpmenu)
# helpmenu.add_command(label="프로그램 정보", command=about)

# window.mainloop()

# 다양한 라이브러리를 만들어보자 !
# requests: 가장 유명한 http 라이브러리다
# scrapy : 웹에서 자료를 모을 때 사용하는 라이브러리이다.
# pillow : 파이썬에서 영상 처리 라이브러리이다.
# pygame : 파이썬으로 게임을 제작하기 위한 프레임 워크
# numpy : 계산과 수학 작업에 많이 사용되는 라이브러리다.
# SciPy: 과학-수학 기능을 지원한다.

# 필로우를 통한 영상표시를 해보자 !

# from PIL import ImageTk, Image # pil모듈에서 몇개의 클래스를 포함시킨다

# import tkinter as tk #라이브러리를 tk로 축약해서 사용한다  tkinter 모듈을 포함시킨다

# #윈도우를 생성하고 우니도우 안에 캔버스를 생성한다

# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# img = Image.open("경로")

# # tk형식으로 영상을 변환한다
# tk_img = ImageTk.PhotoImage(img)

# # tkinter의 캔버스에 영상을 표시한다
# canvas.create_image(250, 250 image=tk_img)

# window.mainloop()

# 영상을 회전시켜 보자 !
# from PIL import Image, ImageTk
# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# #영상 파일을 연다
# im = Image.open("경로")

# #영상을 45도 회전한다
# out = im.rotate(45)

# #영상을 tkinter 형식으로 변환한다
# tk_img = ImageTk.PhotoImage(out)
# # 영상을 tkineter에서 화면에 표시한다
# canvas.create_image(250, 250, image=tk_img)
# window.mainloop()

# 영상을 흐리게 해보자 !

# from PIL import Image, ImageTk, ImageFilter
# import tkinter as tk

# window= tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# #영상 파일을 연다
# im = Image.open("경로")
# #영상을 흐리게 한다
# out = im.filter(ImageFilter.BLUR)
# #영상을 tkinter 형식으로 변환한다.
# tk_img = ImageTk.PhotoImage(out)
# #영상을 tkinter에서 화면에 표시한다.
# canvas.create_image(250,250, image=tk_img)
# window.mainloop()

# # 메뉴를 만들어 보자 !
# import tkinter as tk
# # 파일 메뉴에서 '열기'를 선택했을 때 호출되는 함수
# def open():
#     pass
# # 파일 메뉴에서 "종료"를 눌렀을 때 호출되는 함수
# def quit():
#     window.quit()
# #윈도우를 생성한다
# window = tk.Tk()
# # Menu()를 사용하여 윈도우 안에 메뉴를 생성한다
# menubar = tk.Menu(window)
# #메뉴바 안에 "파일" 메뉴를 생성한다
# filemenu = tk.Menu(menubar)
# # "파일" 메뉴 안에 "열기" 메뉴항목을 추가한다.
# filemenu.add_command(label="열기", command=open)
# filemenu.add_command(label="종료", command=quit)
# # "파일" 메뉴를 누르면 아래로 다른 메뉴가 확장된다.
# menubar.add_cascade(label="파일", menu=filemenu)
# # 윈도우 창의 메뉴로 menebar를 지정한다
# window.config(menu=menubar)
# window.mainloop()

# # 영상 처리 기능을 메뉴로 연결한다 !
# from tkinter.constants import OUTSIDE
# from PIL import Image, ImageTk, ImageFilter
# import tkinter as tk
# from tkinter import Canvas, filedialog as fd

# im = None
# tk_img = None

# # 파일 메뉴에서 "열기를" 선택하였을때 호출되는 함수
# def open():
#     global im, tk_img
#     fname = fd.askopenfilename()
#     im = Image.open(fname)
#     tk_img = ImageTk.PhotoImage(im)
#     canvas.create_image(250,250, image=tk_img)
#     window.update()

# # 파일 메뉴에서 "종료"를 선택했을 때 호출되는 함수
# def quit():
#     window.quit()  

# # 영상처리 메뉴에서 "영상회전"을 선택했을 때 호출되는 함수  
# def image_rotate():
#     global im, tk_img
#     out = im.rotate(45)
#     tk_img =ImageTk.PhotoImage(out)
#     canvas.create_image(250,250, image=tk_img)

# # 영상처리 메뉴에서 "영상흐리기"를 선택하였을 때 호출되는 함수
# def image_blur():
#     global im, tk_img
#     out = im.filter(ImageFilter.BLUR)
#     tk_img = ImageTk.PhotoImage(out)
#     canvas.create_image(250,250, image=tk_img)
#     window.update()

# #윈도우를 생성한다
# window = tk.Tk()
# canvas = tk.Canvas(window,width=500,height=500)
# canvas.pack()

# #메뉴를 생성한다
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar)
# ipmenu = tk.Menu(menubar)
# filemenu.add_command(label="열기", command=open)
# filemenu.add_command(label="종료", command=quit)
# ipmenu.add_command(label="영상회전", command=image_rotate)
# ipmenu.add_command(label="영상흐리기", command=image_blur)
# menubar.add_command(label="파일", menu=filemenu)
# menubar.add_command(label="영상처리", menu=ipmenu)

# window.config(menu=menubar)
# window.mainloop()

# 파일 메뉴에서 "열기"를 선택하였을 때 호출되는 함수
# from PIL import Image, ImageTk


# def open():
#     global im, tk_img
#     fname = fd.askopenfilename()
#     im = Image.open(fname)
#     tk_img = ImageTk.PhotoImage(im)
#     canvas.create_image(250,250, image=tk_img)
#     window.uqdate()

# 객체란 무엇일까요 ?? 함수와 변수를 하나의 단위로 묶을 수 있는 방법이다.
# 자동차로 예를 들어보자 메이커 모델,색상같은 속성을 가지고 있고, 주행하고나 주차하는 동작이있다
# 객체의 속성은 객체의 변수에 저장된다 ex) object.seppd, 객체의 동작을 메소드라하는데 객체안에 정의된 함수이다
# ex) objetc.drive()이렇게 표시한다 객체 = 변수 + 메소드

# # 우리는 이미 객체를 사용해 보았다 !
# from turtle import *
# import turtle
# # turtle 모듈에서 모든 것을 불러올것.
# tim = turtle() # 거북이 객체를 사용한다
# tim.forward(100) # foward는 turtle의 메소드이다

# 객체를 생성해보자 !
# 1. 설계도를 작성하자 속성은 변수로 동작은 메소드로 이것을 클래스라 한다. 자동차 클래스를 만들작성해보자
# class car:
#     def drive(self):
#         self.speed = 10
# car 클래스는 하나의 속성과 하나의 메소드만을 가지고 있다. seppd는 car 클래스의 속성, drive는 메소드이다.
# 메소드의 첫 번째 매개변수는 항상 self로서 현재 객체를 가르킴

# 클래스로부터 객체 만들기
# mycar = car()
# # 객체에 속성을 추가해보자
# mycar.color = "blue"
# mycar.model = "e-class"
# mycar.drive()
# print(mycar.speed)

# 코드정리
# class car:
#     def drive(self):
#         self.speed = 10

# mycar = car()
# mycar.speed = 100

# mycar.drive()
# print(mycar.speed)

# 객체를 생성하면서 초기화 해보자 !
# class car():
#     def __init__(self,speed,color,model): # 속도,색상,모델을 받아서 변수에 저장
#         self.speed = speed
#         self.color = color
#         self.modle = model

#     def drive(self):
#         self.speed = 60

# mycar = car(0,"blue","e-class")
# print(mycar)

#  하나의 클래스로 객체는 많이 만들 수 있다 ! 
# class car():
#     def __init__(self,speed,color,model): # 속도,색상,모델을 받아서 변수에 저장
#         self.speed = speed
#         self.color = color
#         self.modle = model

#     def drive(self):
#         self.speed = 60

# mycar=car(0,"blue","eclass")
# yourcar=car(20,"red","aclass")

#  __str__ 메소드 : 객체를 출력하였을 때 객체안의 정보들을 출력하게 해주는 함수이다

# class car():
#     def __init__(self,speed,color,model): # 속도,색상,모델을 받아서 변수에 저장
#         self.speed = speed
#         self.color = color
#         self.modle = model

#     def __str__(self):
#         msg =   str(self.speed) + self.color + self.modle
#         return msg

# mycar=car(0,"blue","eclass")
# yourcar=car(20,"red","aclass")

# print(mycar)

# self란 무엇일까 어떤 객체가 메소드를 호출했는지 알려준다. 객체이름이 self로 전달된다

# 터틀 그래픽을 다시 그려보자 !

# from turtle import *
# import turtle # 터틀 모듈에서 모든것을 불러온다

# t1 = turtle #객체 생성
# t1.shape("circle")

# t2 = turtle
# t2.shape("turtle")

# t3 = turtle
# t3.shape("square")

# t1.penup()
# t2.penup()
# t1.goto(0, 100)
# t2.goto(0, 50)
# t1.pendown()
# t2.pendown()

# while True:
#     t1.circle(100)
#     t2.circle(150)
#     t3.circle(200)

# car 클래스 터틀 클래스 합치기
# from turtle import *
# import turtle
# class car():
#     def __init__(self,speed,color,model):
#         self.speed = speed
#         self.color = color
#         self.model = model
#         self.turtle = turtle # 클래스 안에 거북이 객체를 생성 후 저장
#         self.turtle.shape("car.gif")

#     def drive(self):
#         self.turtle.forward(self.speed)

#     def left_turn(self):
#         self.turtle.left(90)

# register_shape("car.gif")

# mycar = car(200,"red","eclass")
# for i in range(100):
#     mycar.drive()
#     mycar.left_turn

# ball 클래스를 만들어 보자 !
# from turtle import *
# import turtle
# class ball():
#     def __init__(self,color,size,speed):
#         # 공의위치
#         self.x = 0
#         self.y = 0
#         #공의 속도벡터
#         self.speed = speed
#         self.speed = speed
#         #공의 크기
#         self.size = size
#         #공의 색상
#         self.color = color

#         self.turtle = Turtle()
#         self.turtle.shape("circle")
#         self.turtle.color(color,color)
#         self.turtle.resizemode("user")
#         self.turtle.shapesize(size,size,10)

#         #메소드 정의 메소드 정의가 안되는데 왤까 ?
#         def move(self):
#             self.x += self.speed
#             self.y += self.speed
#             self.turtle.goto(self.x,self.y)

# balll = ball("red",2,3)
# for i in range(100):
#     ball.move()

# # 상속이란 뭘까?
# # 부모클래스의 매소드와 변수들을 자식이 사용하는것

# from turtle import *
# import turtle
# class myturtle(turtle):
#     def glow(self,x,y):
#         self.fillcolor("red")
    
# turtle = myturtle()
# turtle.shape("turtle")
# turtle.onclick(turtle.glow)

# 지금까지 배운것을 토대로 프로젝트를 진행해보자!
# 객체 = 속성 + 메소드()
# class Ball:
#     def __init__(self): #생성자
#         self.color = "red"
#         self.size = 30
#         self.x = 0
#         self.y = 0
#         self.xspeed = 0
#         self.yspeed = 0
#     def move(self):
#         pass #아직 구현되지 않았음을 나타냄

# # 객체생성
# ballA = Ball("red",30,0,0,0,0)
# ballB = Ball("blue",30,0,0,0,0)

# # tkinter 를 사용하여 윈도우 생성
# from tkinter import *
# width = 800
# height = 400
# window = Tk()
# canvas = Canvas(window,width=width,height=height)
# canvas.pack()

# canvas.create_oval(100,100,60,60,fill="red") #원을 하나 그린다

# ball 클래스에서 원 그리기
# from tkinter import *
# class Ball:
#     def __init__(self, canvas, color, size, x, y, xseppd, yspeed):
#         self.canvas = canvas #컨버스 객체
#         self.color = color
#         self.size = size
#         self.x = x
#         self.y = y
#         self.xspeed = xseppd
#         self.yspeed = yspeed
#         self.id = canvas.create_oval(x,y,x+size,y+size, fill=color)

#         def move(self):
#             pass

# width = 800
# height = 400

# window = Tk()
# canvas = Canvas(window, width=width, height=height)
# canvas.pack()

# ballA = Ball(canvas,"red",30,0,0,0,0)

# 공을 움직여 보자 !
# from _typeshed import Self
# from tkinter import *
# class Ball:
#     def __init__(self, canvas, color, size, x, y, xseppd, yspeed):
#         self.canvas = canvas #컨버스 객체
#         self.color = color
#         self.size = size
#         self.x = x
#         self.y = y
#         self.xspeed = xseppd
#         self.yspeed = yspeed
#         self.id = canvas.create_oval(x,y,x+size,y+size, fill=color)

#         def move(self):
#             self.canvas.move(self.id,self.xspeed,self.yspeed)

# width = 800
# height = 400

# window = Tk()
# canvas = Canvas(window, width=width, height=height)
# canvas.pack()

# ballA = Ball(canvas,"red",30,0,0,0,0)

# while True:
#     ballA.move()
#     window.update()
#     time.slepp(0.03)

# # 공을 화면에서 반사시키는 함수를 작성해보자 
# (x1,y1,x2,y2) = self.canvas.coords(slef.id)

# def move(self):
#             self.canvas.move(self.id,self.xspeed,self.yspeed)
#             (x1,y1,x2,y2) = self.canvas.coords(slef.id)
#             (self.x, Self.y) = (x1,y1)
#             if x1 <=0 or x2 >= width: # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
#                 self.xspeed = - self.xspeed # 속도의 부호를 반전시킨다


# 움직이는 볼을 여러개 만들어 보자 !

# color_list = ["red","blue","yellow"]
# # 공들이 저장되는 리스트를 만든다
# balls_list = []
# #10번 반복하면서 ball클래스의 객체를 생성하여 리스트에 저장한다
# for i in range(10):
#     color = random.choice(color_list)
#     size = random.randrange(10,100)
#     xspeed = random.randrange(1,10)
#     yspeed = random.randrange(1,10)
#     balls_list.append(canvas,color,size,0,0,xspeed,yspeed)
# #리스트에 저장된 공들을 이동시킨다
# while True:
#     for ball in balls_list:
#         ball.move()
#     window.update()
#     time.sleep(0.03)

# 전체 소스코드 작성 !
# import builtins
# from tkinter import *
# import time
# import random

# width = 800
# height = 400

# class Ball:
#     def __init__(self, canvas, color, size, x, y, xseppd, yspeed):
#         self.canvas = canvas #컨버스 객체
#         self.color = color
#         self.size = size
#         self.x = x
#         self.y = y
#         self.xspeed = xseppd
#         self.yspeed = yspeed
#         self.id = canvas.create_oval(x,y,x+size,y+size, fill=color)

#     def move(self):
#             self.canvas.move(self.id,self.xspeed,self.yspeed)
#             (x1,y1,x2,y2) = self.canvas.coords(self.id)
#             (self.x, self.y) = (x1,y1)
#             if x1 <=0 or x2 >= width: # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
#                 self.xspeed = - self.xspeed # 속도의 부호를 반전시킨다
#             if y1 <=0 or y2 >= height:
#                 self.yspeed = - self.yspeed

# # 생성된 포탄을 저장하는 리스트 
# bullets = []

# #이벤트를 처리하는 함수
# def fire(event):
#     bullets.append(Ball(Canvas,"red",10,150,250,10,0))

# # 윈도우를 생성한다
# window =Tk()
# canvas = Canvas(window,width=width,height=height)
# canvas.pack()
# canvas.bind("<Button-1>", fire) #마우스 버튼 클릭 이벤트에 함수를 연결한다

# # 우리 우주선과 외계 우주선을 생성한다
# spaceship = Ball(canvas, "green", 100 ,100 ,200 ,0 ,0)
# enemy = Ball(canvas, "red", 100 ,100 ,200 ,0 ,0)

# # 리스트에 저장된 각각의 객체들을 이동시킨다
# while True:
#     for bullet in bullets:
#         bullet.move()
#         #포탄이 화면에 벗어나면 삭제한다
#         if(bullet.x+bullet.size) >= width:
#             canvas.delete(bullet.id)
#             bullet.remove(bullet)

#     enemy.move()
#     window.update()
#     time.sleep(0.03)