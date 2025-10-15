from entries import *
from attacks import *
from database import *
from player import *
from PIL import Image
import random
from damage_step import *
import time
import imageData
import os
import sys
from display_attr import *
from saving import *

import matplotlib.pyplot as plt
import matplotlib.image as mpimg





import sys, pygame, entries

WHITE = (255,255,255)
BLACK = (0,0,0)
screen = pygame.display.set_mode((300, 150))
border = pygame.Rect(300,150,150,100)

def draw(a,b):
    
    # screen.blit(BG, (0,-50))
    # pygame.draw.circle(screen,WHITE,(30,100),20,25)
    screen.blit(a,(20,90))
    screen.blit(b,(220,0))
    pygame.display.update()

def sprites(Mon, opp):
    global curs
    
    first = get_own_images(Mon)
    second = get_opp_image(opp)
    
    
    
   # draw background
    
    
    a = pygame.image.load(first).convert()
    b = pygame.image.load(second).convert()

    return a,b

def main(Mon, opp):
    pygame.init()
    a,b= sprites(Mon,opp)
    clock = pygame.time.Clock()
    draw(a,b)
    run = True
    pygame.display.flip()
    pygame.display.set_caption("Battle")
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            curs.y = 150 
        if key_pressed[pygame.K_RIGHT]:
            curs.x = 350
        if key_pressed[pygame.K_LEFT]:
            curs.x = 300
        if key_pressed[pygame.K_DOWN]:
            curs.y = 180
        draw(a,b)
    
        

# Retrieve image location from image database, using given mon name
def get_own_images(Mon):
    for i,j in Dex.items():
        if j == Mon.name:
            imNumbMe = i
    return f'imageData/firered-leafgreen/back/{imNumbMe}.png'

def get_opp_image(Mon):
    for i,j in Dex.items():
        if j == Mon.name:
            imNumb = i
    return f'imageData/firered-leafgreen/{imNumb}.png'

def get_background(BG):
    bg = "/home/wtc/Desktop/projects/tpokemon/imageData/backgrounds/forest.png"
    return bg

def batView(Mon, opp):

    main(Mon, opp)
    pygame.quit()
