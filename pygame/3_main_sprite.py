import pygame

pygame.init() # 초기화 작업

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("황기운 게임") # 게임 이름 설정

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\rlaej\\Desktop\\python\\pygame\\background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\rlaej\\Desktop\\python\\pygame\\charcter.png")
character_size = character.get_rect().size # 캐릭터의 가로세로 크기 가져옴
character_width = character_size[0] # 가로크기
character_height = character_size[1] # 세로크기
character_x_pos = screen_width /2 - character_width/2 # 가로 크기 절반에 위치함
character_y_pos = screen_height - character_height # 화면 세로 크기에 해당하는 곳에 위치

# 이벤트 루프 실행(이게 있어야 창이 꺼지지 않음)
running = True # 게임이 진행중인가 ?
while running:
    for event in pygame.event.get(): # 프로그램이 종료되지 않도록 대기하며 동작을 체크함
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아니다

    screen.blit(background, (0, 0)) # 배경화면이 나올 좌표 설정

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 화면을 그려준다 

# pygame 종료
pygame.quit()