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
        
        routine_buffer=[]
        for tile_column in self.tile_grid:
            for tile in tile_column:
                if tile.creature != None:
                    if tile.creature.cycle != 0 and self.cyclecounter % tile.creature.cycle == 0:
                        routine_buffer.append( tile.creature.main)
        
        for routine in routine_buffer:
            routine()
        
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
        'Slime_nobg': pygame.image.load('pictures\slime_no_bg.png'),
        'GlassSlime': pygame.image.load('pictures\glassslime_no_bg.png'),
        'JohnnyBravoSlime': pygame.image.load('pictures\johnnybravoslime_no_bg.png'),
#        'FatSlime': pygame.image.load('pictures\fatslime_no_bg.png'),
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
    
    def __init__(self, game_map, event, mouse):
        self.game_map= game_map
        self.event= event
        self.mouse= mouse
        self.mouse_state= False
        self.mouse_tile= None
    
    def update(self):
        self.event.pump()
        
        x, y= self.mouse.get_pos()[0]//self.game_map.tile_grid[0][0].pixel, self.mouse.get_pos()[1]//self.game_map.tile_grid[0][0].pixel
        self.mouse_tile= self.game_map.tile_grid[y][x]
        
        if self.mouse.get_pressed()[0] != self.mouse_state:
            if self.mouse.get_pressed()[0] == False:
                self.mouse_state= False
            else:
                self.mouse_event()
    
    def mouse_event(self):
        self.game_map.create("Cannon", self.mouse_tile)
        self.mouse_state= True
#
            
            
#Init

game_map= GameMap()
draw=  DrawHandler(game_map, pygame.display)
cycle= CycleHandler(game_map)
event= EventHandler(game_map, pygame.event, pygame.mouse)
gamespeed= 17 #em milissegundos de duração de cada ciclo

current_time= pygame.time.get_ticks
sleep= pygame.time.wait

#Main
done = False
pygame.mouse.set_pos(0,0)

while not done:
    
    initial_time= current_time()
    cycle.update()
    draw.update()
    event.update()
    keys=pygame.key.get_pressed()
    
    elapsed_time= current_time() - initial_time
    sleep_duration= gamespeed - elapsed_time
    
    if sleep_duration > 0:
        sleep(sleep_duration)
        
    if keys[pygame.K_ESCAPE]:
        done = True
        
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        
#


































