import pygame

pygame.init()
pygame.display.set_caption("Bezier")

screen_size = (1000, 600)

screen = pygame.display.set_mode(screen_size)
screen.fill((0,0,0))

f = pygame.font.get_default_font()
font = pygame.font.SysFont(f, 32)

position_text1 = font.render("P0", False, (255, 255, 255), (0, 0,0 ))
position_text2 = font.render("P2", False, (255, 255, 255), (0, 0,0 ))
position_text3 = font.render("P3", False, (255, 255, 255), (0, 0,0 ))
position_text4 = font.render("P4", False, (255, 255, 255), (0, 0,0 ))

text_rect1 = position_text1.get_rect()
text_rect2 = position_text2.get_rect()
text_rect3 = position_text3.get_rect()
text_rect4 = position_text4.get_rect()

P0 = (100.0 , 500.0)
P1 = (200.0 , 100.0)
P2 = (600.0 , 80.0)
P3 = (650.0 , 410.0)

running = True
speed = 0.004
t = 0
while running:
    
    while t < 1:
        t += speed

        BEZ0 = (pow((1-t), 3) * P0[0], pow((1-t), 3) * P0[1])
        BEZ1 = (3 * t * pow((1-t), 2) * P1[0], 3 * t * pow((1-t), 2) * P1[1])
        BEZ2 = (3 * t * t * pow((1-t), 1) * P2[0], 3 * t * t * pow((1-t), 1) * P2[1])
        BEZ3 = (t * t * t * P3[0], t * t * t  * P3[1])

        P = (BEZ0[0] + BEZ1[0] + BEZ2[0] + BEZ3[0],BEZ0[1] + BEZ1[1] + BEZ2[1] + BEZ3[1])

        x,y = round(P[0]) , round(P[1])

        text_rect1.center = P0
        text_rect2.center = P1
        text_rect3.center = P2
        text_rect4.center = P3 

        screen.blit(position_text1, text_rect1)
        screen.blit(position_text2, text_rect2)
        screen.blit(position_text3, text_rect3)
        screen.blit(position_text4, text_rect4)

        pygame.draw.line(screen , (0,255,0) , P0 , P1 , 1)
        pygame.draw.line(screen , (0,0,255) , P2 , P3 , 1)
        pygame.draw.circle(screen , (255,255,255) , (x , y) , 2)
        pygame.display.flip()
        pygame.time.delay(10)
    
    pygame.time.delay(1000)
    running = False

    pygame.quit()