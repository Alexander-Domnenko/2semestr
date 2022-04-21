import random
import pygame
pygame.mixer.pre_init(44100,-16,1,512)
import sys
pygame.init()
import tkinter as tk
win=pygame.display.set_mode((700,600))

pygame.mixer.music.load('background_fon.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

sound_d=pygame.mixer.Sound('died.wav')
sound_e=pygame.mixer.Sound('eating.wav')

size=[439,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption('snake')
timer=pygame.time.Clock()
size_block=20
count_block=20
color_rect=(0,0,0)
color_screen=(255,255,255)
count_rect=20
color_eat=(224,0,0)
margin=1

color_snake=(0,102,0)

class SnakeBlock:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def is_inside(self):
        return 0<=self.x<size_block and 0<=self.y<size_block
    def __eq__(self,other):
        return isinstance(other,SnakeBlock) and self.x==other.x and self.y== other.y
def get_random_empty_block():
    x=random.randint(0,count_block-1)
    y=random.randint(0,count_block-1)
    empty_block=SnakeBlock(x,y)
    while empty_block in snake_block:
        empty_block.x=random.randint(0,count_block-1)
        empty_block.y=random.randint(0,count_block-1)
    return empty_block
run=True

def draw_block(color_rect,row,column):
    pygame.draw.rect(screen,color_rect,[10+column*size_block+margin*(column+1),20+row*size_block+margin*(row+1),size_block,size_block])
snake_block=[SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]
apple=get_random_empty_block()

d_row=0
d_col=1

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and d_col!=0:
                d_row=-1
                d_col=0
            elif event.key==pygame.K_DOWN and d_col!=0:
                d_row=1
                d_col=0
            elif event.key==pygame.K_LEFT and d_row!=0:
                d_row=0
                d_col=-1
            elif event.key==pygame.K_RIGHT and d_row!=0:
                d_row=0
                d_col=1
                

    screen.fill(color_screen)
    for row in range(count_rect):
        for column in range(count_rect):
            draw_block(color_rect,row,column)
    
    head=snake_block[-1]
    
    if not head.is_inside():
        
        
        sound_d.play()
        run=False
        pygame.mixer.music.stop()
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
        pygame.quit()
        sys.exit()
    draw_block(color_eat,apple.x,apple.y)
    
    for block in snake_block:
        
        draw_block(color_snake,block.x,block.y)
        
    if apple==head:
        snake_block.append(apple)
        apple=get_random_empty_block()
        sound_e.play()

        
    new_head=SnakeBlock(head.x+d_row,head.y+d_col)
    if new_head in snake_block:
        sound_d.play()
        run=False
        pygame.mixer.music.stop()
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
        pygame.quit()
        sys.exit()
    snake_block.append(new_head)
    snake_block.pop(0)
    pygame.display.flip()

    timer.tick(5)
    
