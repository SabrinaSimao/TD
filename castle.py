# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:41:28 2016

@author: Paulo
"""

class Castle:
    def __init__(self, home):
        self.hp_max = 10
        self.hp_current = self.hp_max
        self.home= home
    
            
    def take_damage(self): #leva 1 ponto de dano, se a vida <= 0 retorna menos 1
        self.hp_current -= 1
        if self.hp_current <= 0:
            return -1
            
    def tile_is_castle(self, tile):
        ##  Overview
        # recebe uma tile arbitrária e retorna se ela é ou não parte do castelo
        #----------------------------------------------------------------------
        ##  Parâmetros
        #  tile: uma instância arbitrária tipo Tile
        #----------------------------------------------------------------------
        ##  Retorno
        #  boolean True se tile faz parte do castelo
        #  boolean False se não faz
    
        for castle_tile in self.home:
            if tile == castle_tile:
                return True
        return False