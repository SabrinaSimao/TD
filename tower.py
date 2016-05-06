# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:27:41 2016

@author: sabri
"""

"""Projeto final de DesSoft da Engenharia 1C
    Tower Defense"""
from monster import Monster

class Tower():
    attack_range= 0
    damage= 1
    icon= "Default"
    
    def __init__(self, game_map, home):
        self.cycle= 1
        self.game_map=game_map
        self.home= home
        self.watchlist= []
        self.build_watchlist()
        
    def build_watchlist(self):
        
        tile_grid= self.game_map.tile_grid
        
        #procura por sí próprio
        x= -1
        y= -1
        for i in range( len( tile_grid)):
            for j in range( len( tile_grid[i])):
                if  tile_grid[i][j] == self.home:
                    x= i
                    y= j
                    break
                
        #recorta a seção relevante adcionando à watchlist
        #antes de adcionar, checar para não adcionar a si mesmo
        for i in range(x-self.attack_range, x+self.attack_range+1):
            for j in range(y-self.attack_range, y+self.attack_range+1):
                if i >= 0 and j >= 0 and i < len( tile_grid) and j < len( tile_grid[i]) and tile_grid[i][j].creature != self:
                    self.watchlist.append( tile_grid[i][j])
    
    def seek_target(self):
        
        for tile in self.watchlist:
            if isinstance(tile.creature, Monster):
                #falta conferir que creature target não é uma torre
                return tile.creature
        return None
        
    def take_damage(self, damage):
        self.hp_current -= damage
        if self.hp_current <= 0:
            self.game_map.erase(self, self.home)
    
        
    def main(self):
        self.cycle= 1
        
        target= self.seek_target()
        if target != None:
            target.take_damage( self.damage)
            self.cycle= 20
    #
#


class Cannon(Tower):
    attack_range= 3
    damage= 5
    icon= "Cannon"