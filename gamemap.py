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

    def __init__(self):
        self.tile_grid= []
        for i in range(19):
           self.tile_grid.append([])
           for j in range(25):
                self.tile_grid[i].append(Tile_Grass())
                
        castle_home=[]
        for i in range (5):
            for j in range(5):
                self.tile_grid[i + 7][j + 10] = Tile_Wall()
                castle_home.append( self.tile_grid[i + 7][j + 10])
                
        self.spawn= Spawn(self, self.tile_grid[0][12])
        self.castle= Castle(castle_home)
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
        
        if x >= 0 and y >= 0 and x < len(self.tile_grid) and y < len(self.tile_grid[0]):
            ##DEBUG:
            return self.tile_grid[x][y]
        return None
    
    def create(self, creature, target_tile):
        ##  Overview
        #  cria ou clone uma instância de uma criatura para um Tile alvo
        #----------------------------------------------------------------------
        ##  Parâmetros:
        #  creature: pode ser tanto uma chave em String correspondente a
        # um tipo de Monster ou Tower, para a criação de uma nova instância,
        # ou uma instância desses tipos, para mover uma já existente
        # target_tile: instância de Tile onde criar a criatura
        #----------------------------------------------------------------------
        ## Retorno:
        #  int 1 em caso de sucesso
        #  int -1 em caso de falha
    
        
        creaturedict={
            "Slime": monster.Slime,
            "Cannon": tower.Cannon
        }
        
        if target_tile.creature == None:
            #checagem de se creature é uma chave ou objeto
            if isinstance(creature, str):
                creature= creaturedict[creature](self, target_tile)
            target_tile.creature= creature
            return 1 #sinal de que criou com sucesso
        return -1 #sinal de que não conseguiu criar
    #
        
#    def 
    
         
    #
         
    def erase(self, target_creature, target_tile):
        ##  Overview
        #  apaga a criatura em location
        #  recebe também a criatura a ser apagada como mecanismo de autenticação
        #  dessa forma criaturas podem apagar só a si mesmas
        #----------------------------------------------------------------------
        ##  Parâmetros
        #  target_creature: instância de Monster ou Tower a ser apagada
        #  target_tile: instância de Tile que contém a criatura a ser apagada
        #----------------------------------------------------------------------
        #  Retorno
        #  int 1 em caso de sucesso
        #  int -1 em caso de falha
        
        if target_tile.creature == target_creature:
            target_tile.creature= None
            return 1
        return -1
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