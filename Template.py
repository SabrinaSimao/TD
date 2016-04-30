# -*- coding: utf-8 -*-
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


 
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_w = 800
screen_h = 600
screen_size = (screen_w, screen_h) #se for apenas 600, nao vai caber uma tile de 32x32 no fim da tela
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tower Defense")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

 #Onde as coisas são inicializadas
slime_image = pygame.image.load("slime.png").convert()
slime_dmg_image = pygame.image.load("slime_dmg.png").convert()
canhao_image = pygame.image.load("canhao.png").convert()
fundo = pygame.image.load("teste.png").convert()



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(fundo,(0,0))
    for x in range(0, 11):
        for y in range(0, 11):
            screen.blit(slime_dmg_image, [x*32,y*32])
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()