import pygame
import os
import random
import tkinter as tk
from pygame.locals import (
K_w,
K_s,
K_a,
K_d,
K_SPACE,
K_ESCAPE,
KEYDOWN,
QUIT,
RLEACCEL
)
speed=4
pygame.init()
win= pygame.display.set_mode((700,660))
pygame.display.set_caption("gaaaaaaaaaaaaaaaaaaaaaaame")
run=True
bg_color=pygame.image.load('fon.jpg')
def stolknovenie():
    global run
    if pygame.sprite.spritecollideany(player,enemies):
        run=False
        win = tk.Tk()
        win.geometry(f"900x700+200+200")
        win.title('')
        Label_1=tk.Label(win,text='Вы проиграли',
                         fg='red',
                         font=('Arial',18),
                         pady=200,
                         )
        Label_1.pack()
        win.mainloop()
player=pygame.sprite.Sprite()
vrag=pygame.sprite.Sprite()
vrag2=pygame.sprite.Sprite()
vrag3=pygame.sprite.Sprite()
vrag4=pygame.sprite.Sprite()

def vrag2Init():
    global vrag2
    vrag2.image=pygame.image.load('pixil-frame-2.png').convert()
    vrag2.image.set_colorkey((0,0,0),RLEACCEL)
    vrag2.rect=vrag2.image.get_rect(center=(random.randint(20,650),random.randint(-40,-10)))
def vrag2Update():
    global vrag2
    global speed
    if vrag2.rect.top<700:
        vrag2.rect.move_ip(0, speed)
    if vrag2.rect.top>600:
        vrag2.rect=vrag2.image.get_rect(center=(random.randint(20,650),random.randint(-540,-500)))

def vrag3Init():
    global vrag3
    vrag3.image=pygame.image.load('demon.png').convert()
    vrag3.image.set_colorkey((0,0,0),RLEACCEL)
    vrag3.rect=vrag3.image.get_rect(center=(random.randint(20,650),random.randint(-100,-10)))
def vrag3Update():
    global vrag3
    global speed
    if vrag3.rect.top<700:
        vrag3.rect.move_ip(0, speed)
    if vrag3.rect.top>600:
        vrag3.rect=vrag3.image.get_rect(center=(random.randint(20,650),random.randint(-540,-500)))

def vragInit():
    global vrag
    vrag.image=pygame.image.load('demon.png').convert()
    vrag.image.set_colorkey((0,0,0),RLEACCEL)
    vrag.rect=vrag.image.get_rect(center=(random.randint(20,650),random.randint(-40,-10)))
def vragUpdate():
    global vrag
    global speed
    if vrag.rect.top<700:
        vrag.rect.move_ip(0, 5)
    if vrag.rect.top>600:
        vrag.rect=vrag.image.get_rect(center=(random.randint(20,650),random.randint(-40,-10)))



def vrag4Init():
    global vrag4
    vrag4.image=pygame.image.load('pixil-frame-3.png').convert()
    vrag4.image.set_colorkey((0,0,0),RLEACCEL)
    vrag4.rect=vrag.image.get_rect(center=(random.randint(0,700),random.randint(-80,-40)))
def vrag4Update():
    global vrag4
    global speed
    if vrag4.rect.top<700:
        vrag4.rect.move_ip(0, 7)
    if vrag4.rect.top>600:
        vrag4.rect=vrag4.image.get_rect(center=(random.randint(20,650),random.randint(-40,-10)))




def playerInit():
    global player
    player.image=pygame.image.load('pixil-frame-00.png').convert()
    player.image.set_colorkey((0,0,0),RLEACCEL)
    player.rect=player.image.get_rect(center=(350,600))
def playerUpdate(pressed_keys):
    global player
    
    if pressed_keys[K_w]and player.rect.top>430:
        player.rect.move_ip(0, -4)
    if pressed_keys[K_s] and player.rect.bottom<650:
        player.rect.move_ip(0, 4)
    if pressed_keys[K_a]and player.rect.left>0:
        player.rect.move_ip(-4, 0)
    if pressed_keys[K_d] and player.rect.right<700:
        player.rect.move_ip(4, 0)
playerInit()
vragInit()
vrag2Init()
vrag3Init()
vrag4Init()
enemies=pygame.sprite.Group([vrag,vrag2,vrag4,vrag3])
en=pygame.sprite.Group()
en.add(player)
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    pygame.time.delay(10)
    pressed_keys = pygame.key.get_pressed()
    playerUpdate(pressed_keys)
    stolknovenie()
    win.blit(bg_color,(0,0))
    vragUpdate()
    vrag2Update()
    vrag3Update()
    vrag4Update()
    win.blit(player.image, player.rect)
    win.blit(vrag.image, vrag.rect)
    win.blit(vrag2.image, vrag2.rect)
    win.blit(vrag3.image, vrag3.rect)
    win.blit(vrag4.image, vrag4.rect)
    pygame.display.flip()
pygame.quit()
