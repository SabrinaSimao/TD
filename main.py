# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:04:42 2016

@author: Alexandre Young
"""

import pygame
from gamemap import GameMap
import menu
import titulos

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
        'Slime_Fire': pygame.image.load('pictures\Slime_Fire.png'),
        'Slime_MagnataPNG': pygame.image.load('pictures\Slime_MagnataPNG.png'),
        'Olho': pygame.image.load('pictures\olho.png'),
#        'FatSlime': pygame.image.load('pictures\fatslime_no_bg.png'),
        'Cannon': pygame.image.load('pictures\cannon.png'),
        'Shadow': pygame.image.load('pictures\particles\shadow.png'),
        'Cannonball': pygame.image.load('pictures\particles\cannonball.png'),
        'archer_tower': pygame.image.load('pictures\\archer_tower.png')}

    def __init__(self, game_map, display):
        
        self.tile_grid= game_map.tile_grid
        self.particle_list= game_map.particle_list
        self.sprite_size= self.tile_grid[0][0].pixel
        self.particle_size= 16 #depois fazer isto em relação ao tamanho marcado na classe
        
        self.display= display
        
        self.display.init()
        self.canvas= self.display.set_mode([self.sprite_size*len( self.tile_grid[0]) + 224, self.sprite_size*len(self.tile_grid)])
        self.canvas.fill([255, 255, 255])
        
#        ---menu inicial do jogo---
        
      #  menu.start(self.canvas)
        
        
        
#        ----MENU_lateral-----
        menu.draw_menu(self.canvas,self.image_bank['Tile_Wall'])
#       
        
        pygame.draw.rect (self.canvas, (255, 0, 0), (900, 100, 32, 32,))
        pygame.draw.rect (self.canvas, (255, 0, 0), (900, 300, 32, 32,))
        pygame.draw.rect (self.canvas, (255, 0, 0), (900, 500, 32, 32,))
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

        #
                    
        #desenha partículas:
        for particle in self.particle_list:
            if particle.icon != None:
                self.canvas.blit(self.image_bank[particle.icon], particle.read_position())
            particle.update()

        #Parte dos botões inutil agora,eu acho
#        mouse_position = pygame.mouse.get_pos ()
#        click = pygame.mouse.get_pressed ()
#        
#        if 900 + 32 > mouse_position [0] > 900 and 100 + 32 > mouse_position [1] > 100:
#            menu.cannon_button (mouse_position, self.canvas, 900, 100, 32, 32, (100, 100, 100), (200, 200, 200), click)
#        else:
#            menu.cannon_button (mouse_position, self.canvas, 900, 100, 32, 32, (100, 100, 100), (200, 200, 200), click)
        
        # Money no menu lateral
        
        titulos.money_text_title ('Gold: ', game_map.castle.gold, (0, 0, 0), self.canvas)

        self.display.flip()
    #
#

class EventHandler:
    
    def __init__(self, game_map, event, mouse, keys, draw):
        self.game_map= game_map
        self.event= event
        self.mouse= mouse
        self.mouse_state= False
        self.mouse_tile= None
        self.keys= keys
        self.quit= False
        self.draw= draw
        self.selected_tower = None
    
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
        self.event.clear()
        
                
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
        
        #Trata do que fazer no clique do botão do mouse
        
        #parte do menu
        mouse_position = pygame.mouse.get_pos ()
        click = pygame.mouse.get_pressed ()
        
        if 900 + 32 > mouse_position [0] > 900 and 100 + 32 > mouse_position [1] > 100 and click[0] == True:

#            self.draw.desenhar_botão()
            
            self.selected_tower = menu.cannon_button (draw.canvas)
            
        if 900 + 32 > mouse_position [0] > 900 and 300 + 32 > mouse_position [1] > 200 and click[0] == True:
            
            self.selected_tower = menu.archer_button (draw.canvas)
            
            
        
        #clique nos tiles
        if self.selected_tower != None: #é inutil clicar nos tiles se  não tiver torre selecionada,tambem quebra o jogo
        
        
            if self.mouse.get_pressed()[0] != self.mouse_state:
                
                cost = tower.tower_cost(self.selected_tower)              
                
                if self.mouse.get_pressed()[0] == False:
                    self.mouse_state= False
                    
                    
                elif game_map.castle.gold >= cost and self.mouse_tile not in game_map.castle.home and self.mouse.get_pos()[0] < 800:
                    
                    create_successful = self.game_map.create(self.selected_tower, self.mouse_tile)
                    if create_successful == 1:
                        game_map.castle.gold -=  cost
                    
                    self.mouse_state= True
#
            
            
#Init
            


game_map= GameMap()
draw=  DrawHandler(game_map, pygame.display)
cycle= CycleHandler(game_map)
event= EventHandler(game_map, pygame.event, pygame.mouse, pygame.key, draw)
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