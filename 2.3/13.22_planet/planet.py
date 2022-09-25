import pygame
import math
width = 768
height = 768
x0=384-20
y0=384-19
class Planet(pygame.sprite.Sprite):
    def __init__(self,name,filename,x,y,r):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.r=r
        self.a=4.7124
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect(center=(x,y))
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        self.rect.x =abs(self.r*math.cos(self.a)+x0)
        self.rect.y=abs(self.r*math.sin(self.a)+y0)
Sun=Planet('Sun','img/Sun.png',width/2-15,height/2-15,None)
Mercury=Planet('Mercury','img/Mercury.png',width/2-5,height/2-35,20)
Venus=Planet('Venus','img/Venus.png',width/2-8,height/2-55,40)
Earth=Planet('Earth','img/Earth.png',width/2-10,height/2-85,65)
Mars=Planet('Mars','img/Mars.png',width/2-9,height/2-110,100)
Jupiter=Planet('Jupiter','img/Jupiter.png',width/2-33.5,height/2-190,180)
Saturn=Planet('Saturn','img/Saturn.png',width/2-27,height/2-260,250)
Uranus=Planet('Uranus','img/Uranus.png',width/2-19,height/2-310,310)
Neptune=Planet('Neptune','img/Neptune.png',width/2-15.5,height/2-360,360)
List_planet=[Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune]
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
while running:  
    screen.fill((0,0,0))
    clock.tick(30)
    Sun.draw(screen)
    for i in List_planet:
        i.draw(screen)
        i.update()
        Mercury.a+=0.02
        Venus.a+=0.01464
        Earth.a+=0.01244
        Mars.a+=0.01
        Jupiter.a+=0.00546
        Saturn.a+=0.00404
        Uranus.a+=0.00284
        Neptune.a+=0.00266
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
