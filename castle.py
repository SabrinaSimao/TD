# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:41:28 2016

@author: Paulo
"""


class Castle:
    def __init__(self, home):
        self.hp_max = 30
        self.hp_current = self.hp_max
        self.home= home
        self.gold = 20
        
            
    def take_damage(self, damage):
        self.hp_current -= damage
        if self.hp_current <= 0:
            return -1
            
    def gain_gold(self, gold):
        self.gold += gold
            
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