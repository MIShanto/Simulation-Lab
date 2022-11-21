import numpy as np
import pygame

pygame.init()
pygame.display.set_caption("pp")

screen_size = (1000, 600)
center = (screen_size[0]/2, screen_size[1]/2)

screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))

f = pygame.font.get_default_font()
font = pygame.font.SysFont(f, 32)

caught_text = font.render("Caught", False, (0, 255, 0), (0, 0, 0))
escape_text = font.render("Escaped", False, (255, 0, 0), (0, 0, 0))

text_rect1 = caught_text.get_rect()
text_rect2 = escape_text.get_rect()

vf = 0
xb = []
yb = []
xf = []
yf = []
input = []

file = open("Practice/pp_input.txt")

for lines in file:
    line = lines.rstrip('\n').split(',')
    input.append(line)

vf = int(input[0][0])

for i in input[1]:
    xb.append(int(i))

for i in input[2]:
    yb.append(int(i))

xf = [0]
yf = [20]

running = True

while running:

    for t in range(len(xb)):
        time_text = font.render(f"Time: {t}", False, (255, 0, 0), (0, 0, 0))
        text_rect3 = time_text.get_rect()
        text_rect3.center = (90, 100)
        screen.blit(time_text, text_rect3)

        if(t > 10):
            text_rect3.center = center
            screen.blit(time_text, text_rect3)
            break

        dist = np.sqrt( (yb[t] - yf[t])**2 + (xb[t] - xf[t])**2 )

        if dist <= 10:
            text_rect1.center = center
            screen.blit(caught_text, text_rect1)
            break

        cosx = (xb[t] - xf[t]) / dist
        sinx = (yb[t] - yf[t]) / dist

        xf.append(xf[t] + vf * cosx)
        yf.append(yf[t] + vf * sinx)

        pygame.draw.line(screen, (0, 0, 0), (center[0]-1000,center[1]), (center[0]+1000,center[1]))
        pygame.draw.line(screen, (0, 0, 0), (center[0],center[1]-1000), (center[0],center[1]+1000))

        if(t>0):
            pygame.draw.line(screen, (0, 0, 255), (center[0] + xf[t-1]*2,center[1] + yf[t-1]*2), (center[0] + xf[t]*2,center[1] + yf[t]*2),2)
            pygame.draw.line(screen, (255, 0, 0), (center[0] + xb[t-1]*2,center[1] + yb[t-1]*2), (center[0] + xb[t]*2,center[1] + yb[t]*2),2)

        pygame.display.flip()
        pygame.time.delay(500)

    pygame.display.flip()
    pygame.time.delay(1000)
    running = False
    pygame.quit()