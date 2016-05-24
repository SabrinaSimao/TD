# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:10:02 2016

@author: chend
"""


import pygame
from gamemap import GameMap

game_map= GameMap()

pygame.font.init()
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


#Build label
def build_label (text_build, color, screen):
    build_text = font.render (text_build, True, color)
    screen.blit (build_text, [810, 110])


#Cannon Label
def cannon_label (text_cannon, color, screen):
    cannon_text = font.render (text_cannon, True, color)
    screen.blit (cannon_text, [810, 210])


#Build algo label
def buildalgo_label (text_buildalgo, color, screen):
    buildalgo_text = font.render (text_buildalgo, True, color)
    screen.blit (buildalgo_text, [810, 180])
    screen.blit (buildalgo_text, [810, 300])


#Cannon Label
def ballista_label (text_ballista, color, screen):
    ballista_text = font.render (text_ballista, True, color)
    screen.blit (ballista_text, [810, 330])