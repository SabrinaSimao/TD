# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:07:18 2016

@author: Alexandre Young
"""

import monster_slime
import torre
import imagebank

class GameMap:
    
    def __init__(self):
        
        #tile_grid: contém a grid de Tiles
        tile_grid= []
        for i in range(19):
           tile_grid.append([])
            for j in range(25):
                tile_grid.append[i](Tile_Grass())
        for i in range (5):
            for j in range(5):
                tile_grid[i + 7][j + 10] = Tile_Wall()
                
        #TODO: decidir como implementar os pontos de Spawn e o Castelo no mapa
    #
    
    
    def create(self, creature, location):
        #Recebe, em string, um objeto e um local (Spawn, Mouse) onde criá-lo
        #creature: string, pode ser "Slime" ou "Cannon"
        #location: string, pode ser "Spawn" ou "Mouse"
    
        
        creaturedict={
            "Slime": lambda: Slime(self)
            "Cannon": lambda: Tower(5, 5, 5, canhao_image, "Cannon")
        }
        
        creature= creaturedict[creature]
        
        location={
            "Mouse": get_mouse_pos(self)
            "Spawn": #primeiro decidir de que forma guardar o ponto de spawn no mapa
        }
        
        
    #
        
    def 
    
    def get_mouse_pos(self):
        #Retorna o objeto Tile em que o mouse se encontra 
         
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
    icon= Imagebank("Default")
    
    def _init_ (self):
        self.creature = None
    
class Tile_Grass(Tile):
    icon= Imagebank("Tile_Grass")
    
class Tile_Wall(Tile):
    icon= Imagebank("Tile_Wall")