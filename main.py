# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:04:42 2016

@author: Alexandre Young
"""

import pygame
from gamemap import GameMap

class CycleHandler:
    #Decide quando executar os objetos do jogo (monstros, torres, etc)

    def __init__(self, game_map):
        
        self.tile_grid= game_map.tile_grid
        self.spawn= game_map.spawn
        self.castle= game_map.castle
        self.cyclecounter= 0 # conta qual ciclo estamos
        self.cyclelimit= 27720
        
    #
    
    def update(self):
        
        
        for tile_column in self.tile_grid:
            for tile in tile_column:
                if tile.creature != None:
                    if tile.creature.cycle != 0 and self.cyclecounter % tile.creature.cycle == 0:
                        tile.creature.main()
                        
        if self.cyclecounter % self.spawn.cycle == 0:
            self.spawn.main()
                    
        self.cyclecounter+= 1
        self.cyclecounter%= self.cyclelimit
    #
#
            
class DrawHandler:
    #desenha os sprites na tela a cada ciclo de jogo
    image_bank= {
        'Tile_Grass': pygame.image.load('pictures\grass.bmp'),
        'Tile_Wall': pygame.image.load('pictures\wall.bmp'),
        'Slime': pygame.image.load('pictures\slime.png'),
        'Cannon': pygame.image.load('pictures\cannon.png')}

    def __init__(self, game_map, display):
        self.tile_grid= game_map.tile_grid
        self.sprite_size= self.tile_grid[0][0].pixel
        
        self.display= display
        
        self.display.init()
        self.canvas= self.display.set_mode([self.sprite_size*len( self.tile_grid[0] ), self.sprite_size*len(self.tile_grid)])
        self.canvas.fill([0, 0, 0])
    #
        
    def update(self):
        ## Overview: desenha os sprites no mapa
        # primeiro desenha as tiles sequencialmente
        # depois desenha as criaturas contidas em cada tile
    
        #deseha tiles:
        for height in range(len(self.tile_grid)):
            for width in range(len(self.tile_grid[height])):
                self.canvas.blit(self.image_bank[self.tile_grid[height][width].icon], [width*self.sprite_size, height*self.sprite_size])
            #
        #
            
        #desenha criaturas:
        for height in range(len(self.tile_grid)):
            for width in range(len(self.tile_grid[height])):
                
                if self.tile_grid[height][width].creature != None:
                    self.canvas.blit(self.image_bank[self.tile_grid[height][width].creature.icon], [width*self.sprite_size, height*self.sprite_size])
            #
        #
        self.display.flip()
    #
#

class EventHandler:
    
    def __init__(self, event):
        self.event= event
    
    def update(self):
        self.event.pump()
#
            
            
#Init

game_map= GameMap()
draw=  DrawHandler(game_map, pygame.display)
cycle= CycleHandler(game_map)
event= EventHandler(pygame.event)
gamespeed= 17 #em milissegundos de duração de cada ciclo

current_time= pygame.time.get_ticks
sleep= pygame.time.wait

#Main
while True:
    
    initial_time= current_time()
    cycle.update()
    draw.update()
    event.update()
    
    elapsed_time= current_time() - initial_time
    sleep_duration= gamespeed - elapsed_time
    
    if sleep_duration > 0:
        sleep(sleep_duration)
#


































