import pygame
import numpy as np
import random as rn
import math
from pygame.gfxdraw import aacircle as circ
from pygame.gfxdraw import filled_circle as fcirc

#screen
pygame.init()
Xsize=800
Ysize=600
screen=pygame.display.set_mode((Xsize,Ysize))
pygame.display.set_caption("simul_reflekcija")
c1=np.array([220,0,0])
#playground
def draw(screen,color,spos,epos):
    pygame.draw.line(screen,color,spos,epos,1)

#target
r=10
tx=rn.randint(Xsize/2,800)
ty=rn.randint(420,600)
def target(x,y):
    fcirc(screen,x,y,r,[250,0,0])
 


#get angle
def angle(x,y):
    d1=math.sqrt(math.pow((x/2-0),2)+math.pow((y/2-0),2))
    d2=math.sqrt(math.pow((x/2-x/2),2)+math.pow((y/2-0),2))
    kut=math.acos(d2/d1)
    
    return kut
#calculate
n1=1.000277
n2=1.330    
def calc(x,y,z):
    kut2= math.degrees(math.sin(z)*x/y)
    print(180-math.degrees(kut2))
    return kut2
    
#line2
def line2(x,y,z):
    d=math.sqrt(math.pow((x/2-x/2),2)+math.pow((y/2-600),2))
    lin=d/z
    return lin


 



running=True
while running:
    #basic
    screen.fill((0,0,0))
    draw(screen,c1,[Xsize/2,0],[Xsize/2,600])
    draw(screen,c1,[0,Ysize/2],[800,Ysize/2])
    target(tx,ty)
    pygame.draw.line(screen,[0,0,250],[0,0],[Xsize/2,Ysize/2],1)  
    kut=angle(Xsize,Ysize)
    kut2=calc(n1,n2,kut)
    dline=line2(Xsize,Ysize,kut2)
    pygame.draw.line(screen,[0,250,0],[Xsize/2,Ysize/2],[dline+Xsize,600],1)
    pygame.display.update()
    n2+=0.5
    print("n= ",n2)
        

    
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    

