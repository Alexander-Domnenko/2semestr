import datetime as dt
import pygame
import time

pou7 = pygame.image.load("7C.png")
pou6 = pygame.image.load("6C.png")
pou5 = pygame.image.load("5C.png")
pou4 = pygame.image.load("4C.png")
pou3 = pygame.image.load("3C.png")
pou2 = pygame.image.load("2C.png")
pou1 = pygame.image.load("1C.png")
print(pou1==pou2)
WIDTH = 500
HEIGHT = 500
FPS = 30
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
pygame.mixer.init()
font = pygame.font.Font(None, 25)
background_image = pygame.image.load('background.jpg')
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True



class Condition:
    def __init__(self,p1,p2,p3,p4,p5,p6,p7,x,y):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.p5=p5
        self.p6=p6
        self.p7=p7
        self.x=x
        self.y=y
    def a(self):
        self.firstC=screen.blit(self.p1,(self.x,self.y))
    def b(self):
        self.secondC=screen.blit(self.p2,(self.x,self.y))
    def c(self):
        self.thirdC=screen.blit(self.p3,(self.x,self.y))
    def d(self):
        self.fourthC=screen.blit(self.p4,(self.x,self.y))
    def e(self):
        self.fifthC=screen.blit(self.p5,(self.x,self.y))
    def f(self):
        self.sixthС=screen.blit(self.p6,(self.x,self.y))
    def g(self):
        self.seventhC=screen.blit(self.p7,(self.x,self.y))


condition=Condition(pou1,pou2,pou3,pou4,pou5,pou6,pou7,160,260)

class Animal:
    
    def __init__(self,name,hunger,health=75):
        self.name=name
        self.health=health
        self.hunger=hunger
        self.time=dt.datetime.now()
    def upHealth(self,needForFood=5):
        self.neefForFood=needForFood
        self.health+=needForFood

    def downHealth(self,needForFood=5):
        self.neefForFood=needForFood
        self.health-=needForFood
    

                
    def printCondition(self):
        if self.health >=80 and self.health <= 100:
           condition.c()
        if self.health<80 and self.health>=60:
           condition.d()
        if self.health<60 and self.health>=40:
           condition.e()
        if self.health<40 and self.health>=20:
           condition.b()
        if self.health<20 and self.health>=1:
           condition.a()
        if self.health>100 and self.health<130:
            condition.f()
        if self.health<=0 or self.health>=130:
            condition.g()
    def play(self):
        condition.y-=20
    def play2(self):
        condition.y+=20
animal=Animal('Panda',10)

while running:
    screen.blit(background_image, (0, 0))
    text = font.render("Score: "+str(animal.health),True,BLACK)
    text2 = font.render("feed: button K_UP",True,BLACK)
    text3 = font.render("play with hero: K_DOWN",True,BLACK)
    screen.blit(text, [10,10])
    screen.blit(text2, [330,10])
    screen.blit(text3, [290,30])
    
    animal.printCondition()
    
    pygame.display.update()
    a=dt.datetime.now()
    if (a-animal.time).seconds>=10:
        animal.downHealth()
        animal.time=dt.datetime.now()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if animal.health>=130 or animal.health<=0:
            animal.health=0
            time.sleep(3)
            running=False
            #pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                animal.upHealth()
            # if event.key==pygame.K_LEFT:
            #     print('текущее здоровье = ',animal.health)
            if event.key==pygame.K_DOWN:
                animal.upHealth(10)
                animal.play()
        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                animal.play2()            
             #   print('текущее состояние = ',end='')
             #   animal.printCondition()
            
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()
