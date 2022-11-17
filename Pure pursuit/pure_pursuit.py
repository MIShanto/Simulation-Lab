import math
import pygame

pygame.init()
 
screen = pygame.display.set_mode((800, 600))
white = (255, 255, 255)


t=0
d=0
xf= []
yf= []
xb= []
yb= []

print("\nSIMULATION OF PURE PURSUIT PROBLEM IN C\n\n")
print("Enter Target path, xb[t] & yb[t]:")

for i in range(0, 13):
    xb.append(float(input()))
    yb.append(float(input()))

print("Enter Fighter's Initial path, xf[0] & yf[0]:")

xf.append(float(input()))
yf.append(float(input()))

print("Reading Fighter velocity, vf from file.....")

try:
    f = open("FighterSpeed.txt")
    vf = float(f.read())
except:
    print("err while reading.")
finally:
    f.close()

for t in range(13):
    d = math.sqrt(pow((yb[t] - yf[t]),2) + pow((xb[t] - xf[t]),2))
    if(d <= 10):
        print(f"\nCaught at {t} mts and {d} kms\n")
        break
        
    else:
        cos_theta = (xb[t] - xf[t])/d
        sin_theta = (yb[t] - yf[t])/d

        xf.append(xf[t] + (vf * cos_theta))
        yf.append(yf[t] + (vf * sin_theta))

        x_cor = int(xf[t])
        y_cor = int(yf[t])
        pygame.draw.circle(screen, white,
                (x_cor, y_cor), 3, 1)
    
if(t>11):
    print("Target Escaped\n")

while True :
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()

        # Draws the surface object to the screen. 
        pygame.display.update() 
