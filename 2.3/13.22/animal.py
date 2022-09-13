import datetime as dt
import pygame

class Condition:
    def __init__(self):
        self.firstC='bad'
        self.secondC='sad'
        self.thirdC='normal'
        self.fourthC='good'
        self.fifthC='happy'
        self.sixthС='gorged'
        self.seventh='died'

condition=Condition()

class Animal:
    needForFood=10
    def __init__(self,name,hunger,health=100):
        self.name=name
        self.health=health
        self.hunger=hunger
        self.time=dt.datetime.now()
    def upHealth(self,kFood):
        self.health+=kFood

    def downHealth(self):
        self.health-=Animal.needForFood

    def printCondition(self):
        if self.health >=80 and self.health <= 100:
            print(condition.fifthC)
        if self.health<80 and self.health>=60:
            print(condition.fourthC)
        if self.health<60 and self.health>=40:
            print(condition.thirdC)
        if self.health<40 and self.health>=20:
            print(condition.secondC)
        if self.health<20 and self.health>=1:
            print(condition.firstC)
        if self.health>100:
            print(condition.sixthС)
        if self.health<=0:
            print(condition.seventh)

animal=Animal('Panda',10)

WIDTH = 500
HEIGHT = 500
FPS = 60
BLACK = (0, 0, 0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True

while running:
    a=dt.datetime.now()
    if (a-animal.time).seconds>=10:
        animal.downHealth()
        animal.time=dt.datetime.now()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                animal.upHealth(int(input('Какое количество еды = ')))
            if event.key==pygame.K_LEFT:
                print('текущее здоровье = ',animal.health)
            if event.key==pygame.K_DOWN:
                print('текущее состояние = ',end='')
                animal.printCondition()
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()
