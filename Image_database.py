# -*- coding: utf-8 -*-
"""
Created on Tue May  3 08:36:47 2016

@author: Paulo
"""
from pygame.image import load


class Imagebank():
    
    bank = {'Tile_Grass': load('pictures\grass.bmp'),
    'Tile_Wall': load('pictures\wall.bpm'),
    'Slime': load('pictures\slime.png'),
    'Cannon': load('pictures\cannon.png')}