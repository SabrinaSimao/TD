# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:41:28 2016

@author: Paulo
"""

class Castle:
    def __init__(self):
        self.hp_max = 10
        self.hp_atual = self.hp_max
    
            
    def take_damage(self): #leva 1 ponto de dano, se a vida <= 0 retorna menos 1
        self.hp_atual -= 1
        if self.hp_atual <= 0:
            return -1