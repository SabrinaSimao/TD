# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:47:37 2016

@author: chend
"""

import pygame

#mouse_position = pygame.mouse.get_pos ()

def cannon_button (screen):
    #Coloração do botão

#    pygame.draw.rect (screen, color, (x, y, width, height))
    pygame.draw.rect (screen, (0, 255, 0), (900, 100, 32, 32,)) # cannon_button
    pygame.draw.rect (screen, (255, 0, 0), (900, 200, 32, 32,)) # ballista_button
    pygame.draw.rect (screen, (255, 0, 0), (900, 300, 32, 32,)) # tower 3
    
    return 'Cannon'
        
def ballista_button (screen):
    
    #    pygame.draw.rect (screen, color, (x, y, width, height))
    pygame.draw.rect (screen, (255, 0, 0), (900, 100, 32, 32,)) # cannon_button
    pygame.draw.rect (screen, (0, 255, 0), (900, 200, 32, 32,)) # ballista_button
    pygame.draw.rect (screen, (255, 0, 0), (900, 300, 32, 32,)) # tower 3
    
    return 'ballista'

 