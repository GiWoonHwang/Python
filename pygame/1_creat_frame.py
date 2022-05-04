import pygame

pygame.init() # 초기화 작업

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("황기운 게임") # 게임 이름 설정

# 이벤트 루프 실행(이게 있어야 창이 꺼지지 않음)
running = True # 게임이 진행중인가 ?
while running:
    for event in pygame.event.get(): # 프로그램이 종료되지 않도록 대기하며 동작을 체크함
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아니다

# pygame 종료
pygame.quit()