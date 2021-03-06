# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:07:18 2016

@author: Alexandre Young
"""
import monster
import tower
from actionable import Tower
from actionable import Monster
import particle
from castle import Castle
from spawn import Spawn
from particleholder import ParticleHolder

class GameMap:
    ##  Overview
    #  Instancia o mapa que será usado no jogo
    #  Essencialmente uma grid de Tiles com uma coleção de métodos para mover
    # o conteúdo das Tiles entre elas
    #--------------------------------------------------------------------------
    ##  Atributos
    #  tile_grid: uma lista 2D de instâncias de Tiles, cada instância é única,
    # mas várias instâncias de mesmo tipo coexistem na lista
    #  spawn: instância de Spawn, por enquanto apenas um exist em todo o mapa
    #  castle: instância de castle, apenas um existe
    ##

    def __init__(self):     
    
        self.tile_grid = [
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
            [9,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9],
            [9,1,1,7,7,7,1,1,1,1,1,1,3,1,1,1,1,1,1,6,6,6,1,1,9],
            [9,1,1,1,7,1,1,1,1,1,1,1,3,1,1,1,1,1,1,6,6,6,1,1,9],
            [9,1,1,1,7,1,1,1,1,1,1,1,3,1,1,1,1,1,1,6,6,6,1,1,9],
            [9,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9],
            [9,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9],
            [9,1,1,1,1,1,1,1,1,1,2,2,0,2,2,1,1,1,1,1,1,1,1,1,9],
            [9,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,9],
            [9,3,3,3,3,3,3,3,3,3,0,2,2,2,0,3,3,3,3,3,3,3,3,3,9],
            [9,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,9],
            [9,1,1,1,1,1,1,1,1,1,2,2,0,2,2,1,1,1,1,1,1,1,1,1,9],
            [9,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9],
            [9,8,8,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9],
            [9,1,8,8,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,5,5,1,1,1,9],
            [9,1,1,8,8,1,1,1,1,1,1,1,3,1,1,1,1,1,5,5,5,5,1,1,9],
            [9,1,1,1,8,8,1,1,1,1,1,1,3,1,1,1,1,5,5,5,5,5,5,1,9],
            [9,1,1,1,1,8,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,9],
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]]
    
        map_dict = {
             9 : Tile_Highgrass,
             8 : Tile_Water,
             7 : Tile_Tree,
             6 : Tile_Farm,
             5 : Tile_Mountain,
             3 : Tile_Dirt,
             2 : Tile_Wall,
             1 : Tile_Grass,
             0 : Tile_Door
        }
        
        self.border_tile=[]
                
        for i in range( len(self.tile_grid)):
            for j in range( len(self.tile_grid[i])):
                self.tile_grid[i][j]= map_dict[self.tile_grid[i][j]]()
                if isinstance(self.tile_grid[i][j], Tile_Highgrass):
                    self.border_tile.append(self.tile_grid[i][j])
        
        castle_home=[]
        for i in range (5):
            for j in range(5):
                castle_home.append( self.tile_grid[i + 7][j + 10])
                
        self.spawn= Spawn(self, self.tile_grid[0][12])
        self.castle= Castle(castle_home)
        
        self.particle_holder= ParticleHolder()
        
        self.set_move_values()
    #
    
    def set_move_values(self):
        grid= self.tile_grid
        
        for column in grid:
            for tile in column:
                if tile.move_value > 0:
                    tile.setDefaultValue()
                
        level= 0
        keep_on= True
        while keep_on:
            keep_on= False
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j].move_value == level:
                        if j != len(grid[i])-1 and grid[i][j+1].move_value == -1 and not isinstance(grid[i][j].actionable, Monster):
                            grid[i][j+1].move_value= level+1
                            keep_on= True
                        if j!= 0 and grid[i][j-1].move_value == -1 and not isinstance(grid[i][j].actionable, Monster):
                            grid[i][j-1].move_value= level+1
                            keep_on= True
                        if i != len(grid)-1 and grid[i+1][j].move_value == -1 and not isinstance(grid[i][j].actionable, Monster):
                            grid[i+1][j].move_value= level+1
                            keep_on= True
                        if i != 0 and grid[i-1][j].move_value == -1 and not isinstance(grid[i][j].actionable, Monster):
                            grid[i-1][j].move_value= level+1
                            keep_on= True
            level+=1
        #
        #precisa checar se eu não tou fechando completamente caminhos
    
    def distance_between(self, tile1, tile2):
        ##  Overview
        #  recebe duas tiles e retorna a distância entre elas, em número de tiles
        # de distância
        #----------------------------------------------------------------------
        ##  Parâmetros:
        #  tile1, tile2: instância arbitrária de tipo Tile
        #----------------------------------------------------------------------
        ##  Retorno:
        #  x: distância horizontal em número de tiles de distância entre tile1
        # e tile2
        #  y: distância vertical em número de tiles de distância entre tile1
        # e tile2
        ##
        x1, y1, x2, y2= 0, 0, 0, 0
        found= 0
        
        for i in range(len (self.tile_grid)):
            for j in range (len (self.tile_grid[i])):
                if self.tile_grid[i][j] == tile1:
                    x1, y1= j, i
                    found+= 1
                if self.tile_grid[i][j] == tile2:
                    x2, y2= j, i
                    found+= 1
                if found == 2:
                    break
        #
        x, y= (x1 - x2), (y1 - y2)
        
        return x, y
    #
    
    def get_adjacent_tile(self, tile, direction):
        ##  Overview
        #  recebe uma tile e uma direção (cima, baixo, etc) e 
        # retorna a tile adjacente na direção dada
        #----------------------------------------------------------------------
        ##  Parâmetros:
        #  tile: instância arbitrária de tipo Tile
        #  direction: Uma direção em formato string, pode ser "Up", "Right"
        # "Down" ou "Left"
        #----------------------------------------------------------------------
        ##  Retorno:
        #  Tile adjacent_tile que é a tile adjacente a ser entregue
        #  None em caso de falha, se não houver uma tile adjacente na direção
        # dada, por exemplo quando você busca por tile_grid[0][0] com direção
        # "Up"
        ##
        directiondict={
            "Up": [-1, 0],
            "Right": [0, 1],
            "Down": [1, 0],
            "Left": [0, -1]
        }
        
        found= False
        x=-1
        y=-1
        #acha a posição x, y da tile na grid
        for i in range(len (self.tile_grid)):
            for j in range (len (self.tile_grid[i])):
                if self.tile_grid[i][j] == tile:
                    x= i
                    y= j
                    found= True
                    break
        
        if  not found:
            return None
        
        x+= directiondict[direction][0]
        y+= directiondict[direction][1]
        
        if x >= 0 and y >= 0 and x < len(self.tile_grid) and y < len(self.tile_grid[x]):
            ##DEBUG:
            return self.tile_grid[x][y]
        return None
    
    def create(self, actionable, target_tile):
        ##  Overview
        #  cria ou clone uma instância tipo Actionable para um Tile alvo
        #----------------------------------------------------------------------
        ##  Parâmetros:
        #  actionable: pode ser tanto uma chave em String correspondente a
        # um tipo de Monster ou Tower, para a criação de uma nova instância,
        # ou uma instância desses tipos, para mover uma já existente
        #  target_tile: instância de Tile onde criar o actionable
        #----------------------------------------------------------------------
        ## Retorno:
        #  int 1 em caso de sucesso
        #  int -1 em caso de falha
        ##
        key_dict={
            "Slime": monster.Slime,
            "Slime_nobg": monster.Slime_nobg,
            "GlassSlime": monster.GlassSlime,
            "JohnnyBravoSlime": monster.JohnnyBravoSlime,
            "Slime_MagnataPNG": monster.Slime_MagnataPNG,
            "Olho": monster.Olho,
            "Slime_Fire": monster.Slime_Fire,
#            "FatSlime": monster.FatSlime,
            "Cannon": tower.Cannon,
            'Archer_Tower': tower.ArcherTower
        }
        
        if isinstance(actionable, str):
                actionable= key_dict[actionable](self, target_tile)
        
        if isinstance(actionable, Tower) and isinstance(target_tile, Tile_Grass) and target_tile.actionable == None:
            #falta checar se eu estou interrompendo um caminho permanentemente
            target_tile.move_value= -100
            target_tile.actionable= actionable
            return 1
        elif isinstance(actionable, Monster) and target_tile.actionable == None:
            target_tile.actionable= actionable
            return 1
        return -1
    #
         
    def erase(self, target_actionable, target_tile):
        ##  Overview
        #  apaga a instância de Actionable na Tile dada
        #  O actionable é recebido como mecanismo de autenticação
        #  dessa forma actionables podem apagar somente a si mesmas
        #----------------------------------------------------------------------
        ##  Parâmetros
        #  target_actionable: instância tipo Actionable
        #  target_tile: instância de Tile que contém o actionable a ser apagado
        #----------------------------------------------------------------------
        #  Retorno
        #  int 1 em caso de sucesso
        #  int -1 em caso de falha
        ##
        if target_tile.actionable == target_actionable:
            target_tile.actionable= None
            return 1
        return -1
        
#
         
class Tile():
    #move value de zero são os pontos de entrada
    #move value de -1 são tiles movíveis normais, mas sem o valor inicializado
    #moves de -10 pra baixo são tiles que não podemos mover para

    pixel = 32
    icon= "Default"
    
    def __init__ (self):
        self.actionable = None
        self.setDefaultValue()
        
    def setDefaultValue(self):
        self.move_value= -1
    
class Tile_Grass(Tile):
    icon= "Tile_Grass"
    
class Tile_Wall(Tile):
    icon= "Tile_Wall"
    
    def setDefaultValue(self):
        self.move_value= -10
    
class Tile_Door(Tile):
    icon= "Tile_Door"
    
    def setDefaultValue(self):
        self.move_value= 0
    
class Tile_Dirt(Tile):
    icon= "Tile_Dirt"
    
class Tile_Mountain(Tile):
    icon= "Tile_Mountain"
    
    def setDefaultValue(self):
        self.move_value= -10
    
class Tile_Farm(Tile):
    icon= "Tile_Farm"
    
    def setDefaultValue(self):
        self.move_value= -10
        

class Tile_Tree(Tile):
    icon= "Tile_Tree"
    
    def setDefaultValue(self):
        self.move_value= -10
    
class Tile_Water(Tile):
    icon= "Tile_Water"
    
    def setDefaultValue(self):
        self.move_value= -10
    
class Tile_Highgrass(Tile):
    icon= "Tile_Highgrass"
    