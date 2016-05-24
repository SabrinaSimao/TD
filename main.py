# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:04:42 2016

@author: Alexandre Young
"""

import pygame
from gamemap import GameMap
from menu import Menu
from particle import Shadow
import labels
import tower
import os

#não sei se da para não importar esses dois,seria necessário fazer 
# o jogo checar se o player tem dinheiro suficiente em outro lugar



class CycleHandler:
    #Decide quando executar os objetos do jogo (monstros, torres, etc)

    def __init__(self, game_map):
            
        self.tile_grid= game_map.tile_grid
        self.game_map= game_map
        self.spawn= game_map.spawn
        self.castle= game_map.castle
        self.cyclecounter= 0 # conta qual ciclo estamos
        self.cyclelimit= 27720
        
    #
    
    def update(self,start):
        
        if start == False:
            return


        
        routine_buffer=[]
        
        for tile_column in self.tile_grid:
            for tile in tile_column:
                if tile.actionable != None:
                    if tile.actionable.cycle != 0 and self.cyclecounter % tile.actionable.cycle == 0:
                        routine_buffer.append( tile.actionable.update)
                        
        for shadow in game_map.particle_holder.shadow:
            routine_buffer.append( shadow.update)
            
        for particle in game_map.particle_holder.particle:
            routine_buffer.append( particle.update)
        
        for routine in routine_buffer:
            routine()
        
        if self.cyclecounter % self.spawn.cycle == 0:
            self.spawn.update()
            
        if self.cyclecounter % 20 == 0:
            self.game_map.set_move_values()
        #Vale a pena ver que outros valores são mais apropriados
                    
        self.cyclecounter+= 1
        self.cyclecounter%= self.cyclelimit
    #
#
            
class DrawHandler:
    #desenha os sprites na tela a cada ciclo de jogo
    image_bank= {
        "Default": pygame.image.load('pictures\Default.png'),
        'Tile_Grass': pygame.image.load('pictures\\tiles\grass.bmp'),
        'Tile_Wall': pygame.image.load('pictures\\tiles\Tile_Wall.png'),
        'Tile_Door': pygame.image.load('pictures\\tiles\Tile_Door.bmp'),
        'Tile_Water': pygame.image.load('pictures\\tiles\Tile_Water.bmp'),
        'Tile_Farm': pygame.image.load('pictures\\tiles\Tile_Farm.bmp'),
        'Tile_Highgrass': pygame.image.load('pictures\\tiles\Tile_Highgrass.bmp'),
        'Tile_Mountain': pygame.image.load('pictures\\tiles\Tile_Mountain.bmp'),
        'Tile_Tree': pygame.image.load('pictures\\tiles\Tile_Tree.png'),
        'Tile_Dirt': pygame.image.load('pictures\\tiles\Tile_Dirt.bmp'),
        'Tile_Menu': pygame.image.load('pictures\\tiles\Tile_Menu.png'),
        'Titulo': pygame.image.load('pictures\\Titulo.png'),
        'Lost': pygame.image.load('pictures\\Lost.png'),
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
        'Big_Shadow': pygame.image.load('pictures\particles\Big_Shadow.png'),
        'Cannonball': pygame.image.load('pictures\particles\cannonball.png'),
        'Archer_tower': pygame.image.load('pictures\\archer_tower.png')}

    def __init__(self, game_map, display):
        
        self.tile_grid= game_map.tile_grid
        self.game_map= game_map
        self.sprite_size= self.tile_grid[0][0].pixel
        self.display= display
        
        self.display.init()
        self.canvas= self.display.set_mode([self.sprite_size*len( self.tile_grid[0]) + 224, self.sprite_size*len(self.tile_grid)])
        self.canvas.fill([255, 255, 255])
        
        
#        -----imagem para o menu inicial----
        
        self.canvas.blit(self.image_bank['Titulo'], (0 ,0))
        self.display.flip()
        
        
    #




    def update(self,start):
        ## Overview: desenha os sprites no mapa
        # primeiro desenha as tiles sequencialmente
        # depois desenha as criaturas contidas em cada tile
    
    
    #    ----------------começo do start-----------        
        
        if start == False:

            

                
            if pygame.mouse.get_pressed()[0] == True or pygame.key.get_pressed()[pygame.K_RETURN] == True:
                return True
                
                
                
            else:
                return False
                
#        ---------final do start--------
    
    #        ----MENU_lateral-----                
        x = 800 
    
        for i in range(7):
            y = 0
    
            for j in range(19):
                self.canvas.blit(self.image_bank['Tile_Menu'], (x ,y))
                y += 32
            x+=32
        #botoes
        
        
        pygame.draw.rect (self.canvas, (255 , 0 ,0), (900, 200, 32, 32)) # cannon_button
        pygame.draw.rect (self.canvas, (255, 0, 0), (900, 400, 32, 32)) # archer_button
#        pygame.draw.rect (self.canvas, (255, 0, 0), (900, 600, 32, 32)) # balista_button
        
        selected={
            "Cannon": 200,
            "Archer_Tower": 400
        }
        if Menu.button_selected != None:
            pygame.draw.rect (self.canvas, (0, 255, 0), (900, selected[Menu.button_selected], 32, 32)) # balista_button
        
        
        
        #deseha tiles:
        for height in range(len(self.tile_grid)):
            for width in range(len(self.tile_grid[height])):
                self.canvas.blit(self.image_bank[self.tile_grid[height][width].icon], [width*self.sprite_size, height*self.sprite_size])
            #
        #desenha sombras
        for shadow in self.game_map.particle_holder.shadow:
            self.canvas.blit(self.image_bank[shadow.icon], shadow.read_position())
        #desenha criaturas:
            
        for height in range(len(self.tile_grid)):
            for width in range(len(self.tile_grid[height])):
                if self.tile_grid[height][width].actionable != None and self.tile_grid[height][width].actionable.icon != "Default":
                    self.canvas.blit(self.image_bank[self.tile_grid[height][width].actionable.icon], [width*self.sprite_size, height*self.sprite_size])

        #
                    
        #desenha partículas:
        for particle in self.game_map.particle_holder.particle:
            self.canvas.blit(self.image_bank[particle.icon], particle.read_position())
        
        # Money no menu lateral
        labels.money_text_title ('Gold: ', game_map.castle.gold, (255, 255, 10), self.canvas)

        # Life no menu lateral
        labels.life_text_title ('Life: ', game_map.castle.hp_current, (0, 255, 120), self.canvas)

        # Build label        
        labels.build_label ('Build menu:', (255, 255, 255), self.canvas)

        # Cannon label        
        labels.cannon_label ('cannon', (200, 200, 200), self.canvas)

        # Buildalgo label        
#        labels.buildalgo_label ('Build', (200, 200, 200), self.canvas)

        #Ballista label        
        labels.archer_label ('archer', (200, 200, 200), self.canvas)

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
        
        self.Green = 0,255,0
    
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
        
        if 900 + 32 > mouse_position [0] > 900 and 200 + 32 > mouse_position [1] > 200 and click[0] == True:

#            self.draw.desenhar_botão()
            
            self.selected_tower = Menu.button_selected= "Cannon"
            
        if 900 + 32 > mouse_position [0] > 900 and 400 + 32 > mouse_position [1] > 300 and click[0] == True:
            
            self.selected_tower = Menu.button_selected= "Archer_Tower"
            
            
        
        #clique nos tiles
        if Menu.button_selected != None: #é inutil clicar nos tiles se  não tiver torre selecionada,tambem quebra o jogo
        
        
            if self.mouse.get_pressed()[0] != self.mouse_state:
                
                selected_tower={
                    "Cannon": tower.Cannon,
                    "Archer_Tower": tower.ArcherTower
                }
                
                cost = selected_tower[Menu.button_selected].cost      
                
                if self.mouse.get_pressed()[0] == False:
                    self.mouse_state= False
                    
                    
                elif game_map.castle.gold >= cost and self.mouse_tile not in game_map.castle.home and self.mouse.get_pos()[0] < 800:
                    
                    create_successful = self.game_map.create(Menu.button_selected, self.mouse_tile)
                    if create_successful == 1:
                        game_map.castle.gold -=  cost
                    
                    self.mouse_state= True
#
            
            
#Init

start = False

os.environ['SDL_VIDEO_WINDOW_POS'] = "150, 40"

game_map= GameMap()
draw=  DrawHandler(game_map, pygame.display)
cycle= CycleHandler(game_map)
event= EventHandler(game_map, pygame.event, pygame.mouse, pygame.key, draw)
gamespeed= 16 #em milissegundos de duração de cada ciclo

current_time= pygame.time.get_ticks
sleep= pygame.time.wait

pygame.display.set_caption("Slime Wars")
#Main

while not event.quit:
    
    
    initial_time= current_time()
    cycle.update(start)
    start = draw.update(start)
    event.update()
    
    elapsed_time= current_time() - initial_time
    sleep_duration= gamespeed - elapsed_time
    
    if sleep_duration > 0:
        sleep(sleep_duration)        
#