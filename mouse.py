# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:34:27 2016

@author: Paulo
"""

def mouse_pos():
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    return [mouse_x//32, mouse_y//32]