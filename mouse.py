# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:34:27 2016

@author: Paulo
"""

import pygame

def mouse_pos_obj(tile_grid):
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    posição_x,posição_y = [mouse_x//32, mouse_y//32]
    return tile_grid[posição_x][posição_y]