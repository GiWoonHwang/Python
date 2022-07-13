# 게임 틀 만들기
import pygame
import sys

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space")
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        
        pygame.display.update()

if __name__ == '__main__':
    main()
# ---------------------------------------------------------------------------------------------------

# 플레이어 클래스 생성

import pygame, sys
from pygame.locals import *
import random

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))


class Player(): # 플레이어
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self): # 그려줌
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def move(self): # 키보드 왼쪽오른쪽키를 입력받아 이동
        if pressed_keys[K_RIGHT]:
            if self.x < MAX_WIDTH-40:
                self.x += 5
        if pressed_keys[K_LEFT]:
            if self.x > 0:
                self.x -= 5


player = Player(MAX_WIDTH/2, MAX_HEIGHT - 40) # 플레이어 객체 생성

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        global pressed_keys
        pressed_keys = pygame.key.get_pressed() # 키 값을 입력받음 이건 전역변수로 써야함
        player_rect = player.draw()
        player.move() # 움직임
        
        pygame.display.update()

if __name__ == '__main__':
    main()
# ---------------------------------------------------------------------------------------------------

# 적과 닿으면 게임 종료

import pygame, sys
from pygame.locals import *
import random

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def move(self):
        if pressed_keys[K_RIGHT]:
            if self.x < MAX_WIDTH-40:
                self.x += 5
        if pressed_keys[K_LEFT]:
            if self.x > 0:
                self.x -= 5

class Enemy(): # 적
    def __init__(self):
        self.x = random.randrange(0, MAX_WIDTH-40) # 초기값은 랜덤
        self.y = 50
        self.speed = random.randrange(10, 20) # 속도도 랜덤
        
    def draw(self): # 적 만들어주는거고
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 20))
    
    def move(self): # 아래로 떨어면서 이동
        self.y = self.y + self.speed
        if self.y >= MAX_HEIGHT:
            self.y = 50
            self.x = random.randrange(0, MAX_WIDTH-40)
            self.speed = random.randrange(7, 15)


player = Player(MAX_WIDTH/2, MAX_HEIGHT - 40)
enemy = Enemy() # 적 객체 생성

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        global pressed_keys
        pressed_keys = pygame.key.get_pressed()
        player_rect = player.draw()
        player.move()
        
        enemy_rect = enemy.draw()
        enemy.move()
        
        if player_rect.colliderect(enemy_rect): # 닿으면 종료
            print("충돌")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()

if __name__ == '__main__':
    main()
# ---------------------------------------------------------------------------------------------------

# 위 코드에 똥사진을 추가해서 게임을 완성해보자.

import pygame, sys
from pygame.locals import *
import random

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def move(self):
        if pressed_keys[K_RIGHT]:
            if self.x < MAX_WIDTH-40:
                self.x += 5
        if pressed_keys[K_LEFT]:
            if self.x > 0:
                self.x -= 5

class Enemy():
    def __init__(self):
        self.x = random.randrange(0, MAX_WIDTH-40)
        self.y = 50
        self.speed = random.randrange(10, 20)
        self.enemy = pygame.image.load(r'.\똥.png') # 불러옴
        self.enemy = pygame.transform.scale(self.enemy,(40,40))
        
    def draw(self):
        return screen.blit(self.enemy, (self.x, self.y)) # bilt로 이미지 위치 지정
    
    def move(self):
        self.y = self.y + self.speed
        if self.y >= MAX_HEIGHT:
            self.y = 50
            self.x = random.randrange(0, MAX_WIDTH-40)
            self.speed = random.randrange(7, 15)


player = Player(MAX_WIDTH/2, MAX_HEIGHT - 40)
enemy = Enemy()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        global pressed_keys
        pressed_keys = pygame.key.get_pressed()
        player_rect = player.draw()
        player.move()
        
        enemy_rect = enemy.draw()
        enemy.move()
        
        if player_rect.colliderect(enemy_rect):
            print("충돌")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()

if __name__ == '__main__':
    main()