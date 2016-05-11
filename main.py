# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:04:42 2016

@author: Alexandre Young
"""

import pygame
from gamemap import GameMap
import menu

#não sei se da para não importar esses dois,seria necessário fazer 
# o jogo checar se o player tem dinheiro suficiente em outro lugar
import tower

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
                if tile.actionable != None:
                    if tile.actionable.cycle != 0 and self.cyclecounter % tile.actionable.cycle == 0:
                        routine_buffer.append( tile.actionable.action)
        
        for routine in routine_buffer:
            routine()
        
        if self.cyclecounter % self.spawn.cycle == 0:
            self.spawn.action()
                    
        self.cyclecounter+= 1
        self.cyclecounter%= self.cyclelimit
    #
#
            
class DrawHandler:
    #desenha os sprites na tela a cada ciclo de jogo
    image_bank= {
        'Tile_Grass': pygame.image.load('pictures\\tiles\grass.bmp'),
        'Tile_Wall': pygame.image.load('pictures\\tiles\Tile_Wall.png'),
        'Tile_Door': pygame.image.load('pictures\\tiles\Tile_Door.bmp'),
        'Tile_Water': pygame.image.load('pictures\\tiles\Tile_Water.bmp'),
        'Tile_Farm': pygame.image.load('pictures\\tiles\Tile_Farm.bmp'),
        'Tile_Highgrass': pygame.image.load('pictures\\tiles\Tile_Highgrass.bmp'),
        'Tile_Mountain': pygame.image.load('pictures\\tiles\Tile_Mountain.bmp'),
        'Tile_Tree': pygame.image.load('pictures\\tiles\Tile_Tree.png'),
        'Tile_Dirt': pygame.image.load('pictures\\tiles\Tile_Dirt.bmp'),
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
        self.canvas= self.display.set_mode([self.sprite_size*len( self.tile_grid[0]) + 200, self.sprite_size*len(self.tile_grid)])
        self.canvas.fill([0, 0, 0])
        mouse_position = pygame.mouse.get_pos ()
        menu.cannon_button (mouse_position, self.canvas, 900, 100, 32, 32, (100, 100, 100), (200, 200, 200))
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

                if self.tile_grid[height][width].actionable != None:
                    self.canvas.blit(self.image_bank[self.tile_grid[height][width].actionable.icon], [width*self.sprite_size, height*self.sprite_size])
        mouse_position = pygame.mouse.get_pos ()
        if 900 + 32 > mouse_position [0] > 900 and 100 + 32 > mouse_position [1] > 100:
            menu.cannon_button (mouse_position, self.canvas, 900, 100, 32, 32, (100, 100, 100), (200, 200, 200))
        else:
            menu.cannon_button (mouse_position, self.canvas, 900, 100, 32, 32, (100, 100, 100), (200, 200, 200))

            
        #
        self.display.flip()
    #
#

class EventHandler:
    
    def __init__(self, game_map, event, mouse, keys,):
        self.game_map= game_map
        self.event= event
        self.mouse= mouse
        self.mouse_state= False
        self.mouse_tile= None
        self.keys= keys
        self.quit= False
    
    def update(self):
        self.window_event()
        self.keyboard_event()
        self.mouse_event()
        
        #Mouse events:
        x, y= self.mouse.get_pos()[0]//self.game_map.tile_grid[0][0].pixel, self.mouse.get_pos()[1]//self.game_map.tile_grid[0][0].pixel
        if x <= 24:
            self.mouse_tile= self.game_map.tile_grid[y][x]
        else:
            pass
        
        
        if self.mouse.get_pressed()[0] != self.mouse_state:
            if self.mouse.get_pressed()[0] == False:
                self.mouse_state= False
            else:
                self.mouse_event()
                
    def window_event(self):
        self.event.pump()
        
        if self.event.peek(pygame.QUIT):
            self.quit= True
        
                
    def keyboard_event(self):
        if self.keys.get_pressed()[pygame.K_ESCAPE]:
            self.quit= True
    
    def mouse_event(self):
        #Atualiza tile que o mouse está em cima
        x, y= self.mouse.get_pos()[0]//self.game_map.tile_grid[0][0].pixel, self.mouse.get_pos()[1]//self.game_map.tile_grid[0][0].pixel
        if x <= 24:
            self.mouse_tile= self.game_map.tile_grid[y][x]
        else:
            pass
        
        #Trata do que fazer no clique do botão
        if self.mouse.get_pressed()[0] != self.mouse_state:
            
            if self.mouse.get_pressed()[0] == False:
                self.mouse_state= False
            elif game_map.castle.gold >= tower.Cannon.cost and self.mouse_tile not in game_map.castle.home:
                game_map.castle.gold -=  tower.Cannon.cost
                self.game_map.create("Cannon", self.mouse_tile)
                self.mouse_state= True
#
            
            
#Init

game_map= GameMap()
draw=  DrawHandler(game_map, pygame.display)
cycle= CycleHandler(game_map)
event= EventHandler(game_map, pygame.event, pygame.mouse, pygame.key)
gamespeed= 17 #em milissegundos de duração de cada ciclo

current_time= pygame.time.get_ticks
sleep= pygame.time.wait

#Main

while not event.quit:
    
    initial_time= current_time()
    cycle.update()
    draw.update()
    event.update()
    
    elapsed_time= current_time() - initial_time
    sleep_duration= gamespeed - elapsed_time
    
    if sleep_duration > 0:
        sleep(sleep_duration)        
#