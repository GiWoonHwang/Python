# 1부터 100까지 임의의 수를 생성하고 생성된 임의의 수를 맞추는 게임 프로그램으로 숫자를 하나 입력하면 임의로 생성된 수보다 높은지 낮은지 정답인지를 알려줍니다.
# 정답을 맞춘 경우 정답을 몇번 맞추었는지 그 결과로 게임의 승부를 알 수 있습니다.
# ---------------------------------------------------------------------------------------------------------

# 숫자 맞추는 게임 코드 만들기

# import random

# random_number = random.randint(1,100)

# game_count = 1

# while True:
#     my_number = int(input('1 ~ 100 사이 숫자를 입력하세요'))
    
#     if my_number > random_number:
#         print('다운')
#     elif my_number < random_number:
#         print('업')
#     elif my_number == random_number:
#         print(f'축하합니다 {game_count}회 만에 맞추셨습니다.')
#         break

#     game_count = game_count + 1
# ---------------------------------------------------------------------------------------------------------
 # 숫자 맞추는 게임 트러블 슛팅(예외처리)
import random
    

random_number = random.randint(1,100)
game_count = 1

while True:
    try:
        my_number = int(input('1 ~ 100 사이 숫자를 입력하세요'))

        if my_number > random_number:
            print('다운')
        elif my_number < random_number:
            print('업')
        elif my_number == random_number:
            print(f'축하합니다 {game_count}회 만에 맞추셨습니다.')
            break
    except:
        print('숫자를 입력하세요')
    
