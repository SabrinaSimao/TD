# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:07:18 2016

@author: Alexandre Young
"""

import monster
import tower
from castle import Castle
from spawn import Spawn

class GameMap:
    
    def __init__(self):
        
        #tile_grid: contém a grid de Tiles
        self.tile_grid= []
        for i in range(19):
           self.tile_grid.append([])
           for j in range(25):
                self.tile_grid[i].append(Tile_Grass())
        for i in range (5):
            for j in range(5):
                self.tile_grid[i + 7][j + 10] = Tile_Wall()
                
        self.spawn= Spawn(self, self.tile_grid[0][12])
        self.castle= Castle()
    #
    
    
    def create(self, creature, location):
        #Recebe, em string, um objeto e um local (Spawn, Mouse) onde criá-lo
        #creature: string, pode ser "Slime" ou "Cannon"
        #location: string, pode ser "Spawn" ou "Mouse"
    
        
        creaturedict={
            "Slime": monster.Slime,
            "Cannon": tower.Cannon
        }
        
        locationdict={
            "Mouse": lambda: self.mouse_pos_obj(),
            "Spawn": self.spawn.home
        }
        
        target_tile= locationdict[location]
        
        if target_tile.creature == None:
            target_tile.creature= creaturedict[creature](self)
            return 1 #sinal de que criou com sucesso
        return -1 #sinal de que não conseguiu criar
    #
        
#    def 
    
         
    #
         
    def erase(self, creature):
        
        # Procura creature no mapa de tiles
        # quando achar, limpar o atributo creature da Tile
        
        for tile_column in self.tile_grid:
            for tile in tile_column:
                
                if creature == tile.creature:
                    tile.creature= None
                    break
                #
            #
        #
    #
#
         
class Tile():
    pixel = 32
    icon= "Default"
    
    def __init__ (self):
        self.creature = None
    
class Tile_Grass(Tile):
    icon= "Tile_Grass"
    
class Tile_Wall(Tile):
    icon= "Tile_Wall"