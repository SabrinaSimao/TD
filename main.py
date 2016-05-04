# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:04:42 2016

@author: Alexandre Young
"""

import pygame
import map

pygame.init

class CycleManager:
    #Decide quando executar os objetos do jogo (monstros, torres, etc)

    def __init__(self, game_map):
        
        self.tile_grid= game_map.tile_grid
        self.castle= game_map.castle
        self.cyclecounter= 0 # conta qual ciclo estamos
        self.cyclelimit= 27720
        
    #
    
    def update(self):
        
        for tile_column in self.tile_grid:
            for tile in tile_column:
                if tile.creature != None:
                    tile.creature.main()
    #
#
            
class DrawManager:
    #desenha os sprites na tela a cada ciclo de jogo
    image_bank= {
        'Tile_Grass': pygame.image.load('pictures\grass.bmp'),
        'Tile_Wall': pygame.image.load('pictures\wall.bpm'),
        'Slime': pygame.image.load('pictures\slime.png'),
        'Cannon': pygame.image.load('pictures\cannon.png')}

    def __init__(self, map, canvas):
        self.canvas= canvas
        self.tile_grid= map.tile_grid
        self.sprite_size= Tile.pixel
        
        self.canvas.init()
        self.canvas.set_mode(self.sprite_size*len( self.tile_grid[0] ), self.sprite_size*len(self.tile_grid))
        self.canvas.fill( (0, 0, 0) )
    #
        
    def update(self):
        ## Overview: desenha os sprites no mapa
        # primeiro desenha as tiles sequencialmente
        # depois desenha as criaturas contidas em cada tile
    
        #deseha tiles:
        for height in len(self.tile_grid):
            for width in len(self.tile_grid[height]):
                self.canvas.blit(image_bank[tile_grid[height][width].icon], [width*sprite_size, height*sprite_size])
            #
        #
            
        #desenha criaturas:
        for height in len(self.tile_grid):
            for width in len(self.tile_grid[height]):
                
                if tile_grid[height][width].creature != None:
                    self.canvas.blit(image_bank[tile_grid[height][width].creature.icon], [width*sprite_size, height*sprite_size])
            #
        #
        canvas.flip()
    #
#
            
            
#Init

game_map= GameMap()
draw=  DrawManager(game_map, pygame.display)
cycle= CycleManager(game_map)
gamespeed= 60 #em ciclos/segundo

#Main
while True:
    
    initial_time= pygame.time.get_ticks()
    cycle.update()
    draw.update()
    
    elapsed_time= pygame.time.get_ticks() - initial_time
    sleep_duration= (1/60) - elapsed_time
    
    if sleep_duration > 0:
        pygame.time.wait(sleep_duration)
#


































