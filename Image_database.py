# -*- coding: utf-8 -*-
"""
Created on Tue May  3 08:36:47 2016

@author: Paulo
"""
from pygame.image import load


class Imagebank():
    
    bank = {'Tile_Grass': load('pictures\grass.bmp'),
    'Tile_Wall': load('pictures\wall.bmp'),
    'Slime': load('pictures\slime.png'),
    'Slime_nobg': load('pictures\slime_no_bg.png'),
    'GlassSlime': load('pictures\glassslime_no_bg.png'),
    'JohnnyBravoSlime': load('pictures\johnnybravoslime_no_bg.png'),
#    'FatSlime': load('pictures\fatyslime_no_bg.png'),
    'Cannon': load('pictures\cannon.png')}