import pygame

pygame.init()
pygame.display.set_caption("Bezier Curve")

screenSize = (1000,600)
screen = pygame.display.set_mode(screenSize)

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_text1 = font.render("P0", True, (255,255,255), (0,0,0))
position_text2 = font.render("P1", True, (255,255,255), (0,0,0))
position_text3 = font.render("P2", True, (255,255,255), (0,0,0))
position_text4 = font.render("P3", True, (255,255,255), (0,0,0))

textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()
textRect3 = position_text3.get_rect()
textRect4 = position_text4.get_rect()


P0 = (100.0 , 500.0)
P1 = (200.0 , 100.0)
P2 = (600.0 , 80.0)
P3 = (650.0 , 410.0)


running = True
speed = 0.004
t= 0

while running:
    screen.fill((0,0,0))
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        while t < 1:
            t += speed

            BEZ0 = (pow(1-t , 3) * P0[0] , pow(1-t , 3) * P0[1])
            BEZ1 = (3 * t * pow(1-t , 2) * P1[0] , 3 * t * pow(1-t , 2) * P1[1])
            BEZ2 = (3 * t * t * (1 - t) * P2[0] , 3 * t * t * (1 - t) * P2[1])
            BEZ3 = (pow(t , 3) * P3[0] , pow(t , 3) * P3[1])

            #P = (BEZ0[0] + BEZ1[0] + BEZ2[0] + BEZ3[0],BEZ0[1] + BEZ1[1] + BEZ2[1] + BEZ3[1])
            P = (BEZ0 + BEZ1 + BEZ2 + BEZ3,BEZ0[1] + BEZ1[1] + BEZ2[1] + BEZ3[1])

            x,y = round(P[0]) , round(P[1])

            textRect1.center = P0
            textRect2.center = P1
            textRect3.center = P2
            textRect4.center = P3 

            screen.blit(position_text1 , textRect1)
            screen.blit(position_text2 , textRect2)
            screen.blit(position_text3 , textRect3)
            screen.blit(position_text4 , textRect4)

            pygame.draw.line(screen , (0,255,0) , P0 , P1 , 1)
            pygame.draw.line(screen , (0,0,255) , P2 , P3 , 1)
            pygame.draw.circle(screen , (255,255,255) , (x , y) , 2)
            pygame.display.flip()
    
    pygame.time.delay(10000)
    pygame.quit()
    break