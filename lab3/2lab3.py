import pygame
from pygame.draw import *
 
pygame.init()
 
FPS = 30
screen = pygame.display.set_mode((400, 400))
 
screen.fill("white")
circle(screen,(255,255,0),(150,150),100) #голова
circle(screen,(255,0,0),(110,130),20) #левый глаз
circle(screen,(0,0,0),(110,130),8) #зрачок
circle(screen,(255,0,0),(190,130),15) #правый глаз
circle(screen,(0,0,0),(190,130),8) #зрачок
polygon(screen,(0,0,0),[(100,200),(190,200),(190,220),(100,220)]) #рот
line(screen,(0,0,0),(130,115),(50,80),15)#левая бровь
line(screen,(0,0,0),(170,115),(270,85),15)
 
 
 
pygame.display.update()
 
clock = pygame.time.Clock()
finished = False
 
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
 
pygame.quit()
