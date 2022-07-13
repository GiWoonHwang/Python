# pip install pygame

# import pygame
# import sys

# FPS = 60
# MAX_WIDTH = 600
# MAX_HEIGHT = 400

# pygame.init() # 게임 초기화
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT)) # 스크린 설정

# def main():
#     while True:
#         for event in pygame.event.get(): # 파이게임이벤트 가져옴
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN: # 키다운중 스페이 눌리면 스페이스 출력
#                 if event.key == pygame.K_SPACE:
#                     print('space')
        
#         clock.tick(FPS) # 프레임 설정, 1초에 60프레임이다.
#         screen.fill((255,255,255)) # 화면을 흰색으로 채움 rgb
        
#         pygame.display.update()
        
# if __name__ == '__main__':
#     main()
# -------------------------------------------------------------------------------------

# 게임 플레이어 만드는 코드. 클래스를 사용하여 만들었다 클래스를 사용하면 조금 더 직관적이니까

import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

# 클래스로 플레이어 생성
class Player():
    def __init__(self, x, y): # 초기 객체 초기화
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    def draw(self): # 파란색 네모를 x,y 좌표에 40x40 사이즈로 그림
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

player = Player(50, MAX_HEIGHT - 40)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True # 스페이스를 누르면 점프를 참으로 설정
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        
        player_rect = player.draw()
        player.jump() # 점프를 구현함 스페이스바를 눌렀을때, 즉 점프가 참 일때 동작
        
        print(player_rect)
        
        pygame.display.update()

if __name__ == '__main__':
    main()
# -------------------------------------------------------------------------------------
 
# 적과 닿으면 종료하는 코드 만들기 위에 코드에 덧붙인다

import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

class Enemy(): # 적 클래스
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self):
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 40))
    
    def move(self,speed): # 화면 오른쪽 끝에서부터 왼쪽으로 이동함
        self.x = self.x - speed
        if self.x <= 0:
            self.x = MAX_WIDTH

player = Player(50, MAX_HEIGHT - 40)
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40)

def main():
    
    speed = 7
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        
        player_rect = player.draw() # 적을 그린다.
        player.jump()
        
        enemy_rect = enemy.draw()
        enemy.move(speed)
        speed = speed + 0.01 # 속도가 조금씩 빨라짐
        
        if player_rect.colliderect(enemy_rect): # 충돌하면 종료
            print("충돌")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()

if __name__ == '__main__':
    main()