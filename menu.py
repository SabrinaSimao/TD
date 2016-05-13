# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:47:37 2016

@author: chend
"""

import pygame

#mouse_position = pygame.mouse.get_pos ()

def cannon_button (mouse_position, screen, x, y, width, height, color1, color2, click):
    #Coloração do botão
    if x + width > mouse_position [0] > x and y + height > mouse_position [1] > y:
        pygame.draw.rect (screen, color1, (x, y, width, height))
        #Funções do botão
        if click [0] == 1:
            print ('1') #Algo para construir canhão
            pygame.draw.rect (screen, color2, (x, y, width, height))

    else:
        pygame.draw.rect (screen, color2, (x, y, width, height))
        

    