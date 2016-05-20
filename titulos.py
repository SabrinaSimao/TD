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
    pygame.draw.rect (screen, (255, 255, 255), (800, 0, 200, 100,)) # Foi o modo que consegui para dar um clear na tela :D
    pygame.font.init()
    pygame.init ()
    font = pygame.font.SysFont (None, 25)
    money_text = font.render (text_money + str(money), True, (0, 0, 0))
    screen.blit (money_text, [810, 10])