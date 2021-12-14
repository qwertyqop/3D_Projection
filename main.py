"""
sources:
https://www.mathworks.com/matlabcentral/answers/123763-how-to-rotate-entire-3d-data-with-x-y-z-values-along-a-particular-axis-say-x-axis#comment_487621

"""

import pygame
import math

WIDTH = 500
HEIGHT = 500
td=[[-2,-2,-2], [-2,2,-2], [2,2,-2], [2,-2,-2], [-2,-2,2], [-2,2,2], [2,2,2], [2,-2,2], [0,0,0]]

arr = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0]]

mult = 50
s = 0
pygame.init()
pygame.display.set_caption('boxplot')  # name of the window
screen=pygame.display.set_mode([WIDTH,HEIGHT])
clock=pygame.time.Clock()



while True:
    for i in range( len( arr ) ):
        thetax = ((2*math.pi)/1000)*(pygame.mouse.get_pos()[1]+250)
        thetay = ((2 * math.pi) / 1000) * (pygame.mouse.get_pos()[0]+250)

        #  x rotation
        x = td[i][0]
        y = td[i][1] * math.cos( thetax ) - td[i][2] * math.sin( thetax )
        z = td[i][1] * math.sin( thetax ) + td[i][2] * math.cos( thetax )
        #  y rotation
        x = x * math.cos( thetay ) + z * math.sin( thetay )
        y = y
        z = z * math.cos( thetay ) - x * math.sin( thetay )
        #  z rotation
        #x = td[i][0] * math.cos( thetay ) - td[i][1] * math.sin( thetay )
        #y = td[i][0] * math.sin( thetay ) + td[i][1] * math.cos( thetay )
        #z = td[i][2]

        z = z-10

        arr[i][0] = (x)
        arr[i][1] = (y)

        pygame.draw.circle( screen, [0, 0, 0], [mult * (x) + 250, mult * (y) + 250], 5 )  # rnder points

        pygame.draw.circle( screen, [0, 0, 0], [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]], 5 )

    for i in range( len( arr ) -1 ):  # render lines
        for j in range( len( arr ) -1 ):
            pygame.draw.line( screen, [0,0,0], [mult*arr[i][0]+250, mult*arr[i][1]+250], [mult*arr[j+1][0]+250, mult*arr[j+1][1]+250], 2 )

    pygame.display.update()
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
