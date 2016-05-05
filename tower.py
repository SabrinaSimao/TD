# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:27:41 2016

@author: sabri
"""

"""Projeto final de DesSoft da Engenharia 1C
    Tower Defense"""
    
class Tower():
    alcance = 5
    cycle = 1
    dano = 1
    icon = 'default.png'
    
    def __init__(self, game_map):
        
        self.game_map=game_map
        
    def main(self):
        None
    #
#


class Cannon(Tower):
    alcance= 5
    cycle= 20
    dano= 5
    icon= "cannon.png"