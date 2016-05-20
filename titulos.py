# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:10:02 2016

@author: chend
"""


import pygame
from gamemap import GameMap

game_map= GameMap()


# Função título money
def money_text_title (text_money, money, color, screen):
#    pygame.draw.rect (screen, (255, 255, 255), (800, 0, 200, 100,)) # Foi o modo que consegui para dar um clear na tela :D
    pygame.font.init()
    pygame.init ()
    font = pygame.font.SysFont (None, 25)
    money_text = font.render (text_money + str(money), True, color)
    screen.blit (money_text, [810, 10])


# Função título lifes
def life_text_title (text_life, life, color, screen):
#    pygame.draw.rect (screen, (2, 255, 255), (800, 30, 200, 40,)) # Foi o modo que consegui para dar um clear na tela :D
    pygame.font.init()
    pygame.init ()
    font = pygame.font.SysFont (None, 25)
    life_text = font.render (text_life + str(life), True, color)
    screen.blit (life_text, [810, 40])