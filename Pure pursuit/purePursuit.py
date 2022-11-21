import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.locals import *

vf = None
xb = []
yb = []
inputs = []

with open('Pure pursuit/pp_input.txt') as file:
    for line in file.readlines():
        inputs.append(line.rstrip().rsplit(','))

vf = int(inputs[0][0])
xb = [int(x) for x in inputs[1]]
yb = [int(x) for x in inputs[2]]

xf = [0]
yf = [50]

pygame.init()

size = width, height = (800, 800)
center_coords = (width/2, height/2)

screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

pygame.display.set_caption('Pure Pursuit')

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_boomber = font.render("B", True, (255,0,0), (0,0,0))
position_fighter = font.render("F", True, (0,255,0), (0,0,0))
position_match = font.render("Caught", True, (0,255,0), (0,0,0))
position_escape = font.render("Escaped", True, (255,0,0), (0,0,0))

textRect1 = position_boomber.get_rect()
textRect2 = position_fighter.get_rect()
textRect4 = position_match.get_rect()
textRect5 = position_escape.get_rect()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for t in range(len(xb)):

        pygame.time.delay(100)

        position_time = font.render("Time:"+str(t), True, (255,255,255), (0,0,0))
        textRect3 = position_time.get_rect()
        textRect3.center = (90,height-50)
        screen.blit(position_time , textRect3)

        if t > 10:
            textRect5.center = center_coords
            screen.blit(position_escape , textRect5)
            print('Bomber escaped!')
            running = False
            pygame.display.flip()
            break

        dist = np.sqrt( (yb[t] - yf[t])**2 + (xb[t] - xf[t])**2 )

        if dist <= 10:
            textRect4.center = center_coords
            screen.blit(position_match, textRect4)
            print('caught at time', t)
            running = False
            pygame.display.flip()
            break

        cosx = (xb[t] - xf[t]) / dist
        sinx = (yb[t] - yf[t]) / dist

        xf.append(xf[t] + vf * cosx)
        yf.append(yf[t] + vf * sinx)

        pygame.draw.line(screen, (0, 0, 0), (center_coords[0]-2000,center_coords[1]), (center_coords[0]+2000,center_coords[1]))
        pygame.draw.line(screen, (0, 0, 0), (center_coords[0],center_coords[1]-2000), (center_coords[0],center_coords[1]+2000))
        
        if(t>0):
            pygame.draw.line(screen, (0, 0, 255), (center_coords[0] + xf[t-1]*2,center_coords[1] + yf[t-1]*2), (center_coords[0] + xf[t]*2,center_coords[1] + yf[t]*2),2)
            pygame.draw.line(screen, (255, 0, 0), (center_coords[0] + xb[t-1]*2,center_coords[1] + yb[t-1]*2), (center_coords[0] + xb[t]*2,center_coords[1] + yb[t]*2),2)

        print('Red line = Bomber, Blue line = Fighter')

        pygame.display.flip()
        pygame.time.delay(100)

    #running = False
pygame.time.delay(1000)
pygame.quit()