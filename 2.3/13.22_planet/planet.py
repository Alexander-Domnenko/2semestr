import pygame
import math
WIDTH = 768
HEIGHT = 768
x0=384-20
y0=384-19
class Planet(pygame.sprite.Sprite):
    def __init__(self,name,filename,x,y,r):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.r=r
        self.a=0
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect(center=(x,y))
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        self.rect.x =abs(self.r*math.cos(self.a)+x0)
        self.rect.y=abs(self.r*math.sin(self.a)+y0)
        if self.a>=6.26:
            self.a=0
Sun=Planet('Sun','img/Sun.png',WIDTH/2-15,HEIGHT/2-15,None)
Mercury=Planet('Mercury','img/Mercury.png',WIDTH/2-5,HEIGHT/2-35,20)
Venus=Planet('Venus','img/Venus.png',WIDTH/2-8,HEIGHT/2-55,40)
Earth=Planet('Earth','img/Earth.png',WIDTH/2-10,HEIGHT/2-85,65)
Mars=Planet('Mars','img/Mars.png',WIDTH/2-9,HEIGHT/2-110,100)
Jupiter=Planet('Jupiter','img/Jupiter.png',WIDTH/2-33.5,HEIGHT/2-190,180)
Saturn=Planet('Saturn','img/Saturn.png',WIDTH/2-27,HEIGHT/2-260,250)
Uranus=Planet('Uranus','img/Uranus.png',WIDTH/2-19,HEIGHT/2-310,310)
Neptune=Planet('Neptune','img/Neptune.png',WIDTH/2-15.5,HEIGHT/2-360,360)
List_planet=[Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune]
FPS = 30
BLACK = (0, 0, 0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
while running:  
    screen.fill(BLACK)
    clock.tick(FPS)
    Sun.draw(screen)
    for i in List_planet:
        i.draw(screen)
        i.update()
        i.a+=1/i.r
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()