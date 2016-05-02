# -*- coding: utf-8 -*-
'''
Created on Mon May  2 14:32:08 2016

@author: Paulo

castelo([7,10])
até([12,15])

'''
class Tile():
    pixel = 32
    icon= Imagebank("Default")
    
    def _init_ (self):
        self.creature = None
    
class Tile_Grass(Tile):
    icon= Imagebank("Tile_Grass")
    
class Tile_Wall(Tile):
    icon= Imagebank("Tile_Wall")

def Map_create():
    Map = []
    for i in range(19):
        Map.append([])
        for j in range(25):
            Map[i].append(Tile_Grass())
    for i in range (5):
        for j in range(5):
            Map[i + 7][j + 10] = Tile_Wall()
            
    return Map
            
Map = Map_create()
print(Map)