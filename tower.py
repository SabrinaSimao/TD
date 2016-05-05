# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:27:41 2016

@author: sabri
"""

"""Projeto final de DesSoft da Engenharia 1C
    Tower Defense"""
    
class Tower():
    attack_range= 5
    damage= 1
    icon= "Default"
    
    def __init__(self, game_map, home):
        self.cycle= 1
        self.game_map=game_map
        self.home= home
        
    def main(self):
        None
    #
#


class Cannon(Tower):
    attack_range= 5
    damage= 5
    icon= "Cannon"
    
    def main(self):
        self.cycle= 1 #prepara para atirar assim que algo entrar no alcance
        
        #checa se algo está dentro do alcance
        #se estiver, atirar nele e setar cycle pra 20