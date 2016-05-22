# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:10:02 2016

@author: chend
"""


import pygame
from gamemap import GameMap

game_map= GameMap()

pygame.font.init()
pygame.init ()
font = pygame.font.SysFont ('Castellar', 25)
font.set_bold (True)



# Função título money
def money_text_title (text_money, money, color, screen):
    money_text = font.render (text_money + str(money), True, color)
    screen.blit (money_text, [810, 10])


# Função título lifes
def life_text_title (text_life, life, color, screen):
    life_text = font.render (text_life + str(life), True, color)
    screen.blit (life_text, [810, 40])