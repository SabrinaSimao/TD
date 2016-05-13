# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:38:56 2016

@author: Alexandre Young
"""

class Actionable:

    wait= 60
    icon= "Default"
    
    def __init__( self, game_map, home):
        self.game_map= game_map
        self.home= home
        self.cycle= 1
        self.activate()
        
    def activate():
        None
        
    def action():
        None

class Monster( Actionable):
    hp_max= 10
    damage= 1
    
    def activate ( self):
        self.hp_current= self.hp_max
        self.cycle= self.wait
    
    def action( self):
        #função que executa o monstro, chamada por CycleManager
        self.move()
            
    def move( self):
        #tenta se mover para a tile abaixo
        #em sucesso:
        #retirar sua instância da tile anterior
        #atualziar home
        #checar se chegou no castelo
        #em falha:
        #nada
    
        target_tile= self.game_map.get_adjacent_tile(self.home, "Down")
        if target_tile!= None:
            if self.game_map.create(self, target_tile) == 1:
                self.game_map.erase(self, self.home)
                self.home= target_tile
                if self.game_map.castle.tile_is_castle(self.home):
                    self.invade()
    
    def take_damage( self, damage):
        self.hp_current -= damage
        if self.hp_current <= 0:
            self.game_map.castle.gain_gold(5)#mudar o 5 por uma variavel para cadas monstro, 5 = quantidade de gold a ser ganha
            self.game_map.erase(self, self.home)
                    
    def invade( self):
        #em caráter temporário:
        self.game_map.castle.take_damage(1)
        self.game_map.erase(self, self.home)
        
class Tower( Actionable):
    attack_range= 0
    cost = 1
    bullet= "Default"
    reload_time= 60
        
    def activate( self):
        self.watchlist= []
        self.build_watchlist()
        
    def build_watchlist( self):        
        tile_grid= self.game_map.tile_grid
        
        #procura por sí próprio
        x= -1
        y= -1
        for i in range( len( tile_grid)):
            for j in range( len( tile_grid[i])):
                if  tile_grid[i][j] == self.home:
                    x= i
                    y= j
                    break
                
        #recorta a seção relevante adcionando à watchlist
        #antes de adcionar, checar para não adcionar a si mesmo
        for i in range(x-self.attack_range, x+self.attack_range+1):
            for j in range(y-self.attack_range, y+self.attack_range+1):
                if i >= 0 and j >= 0 and i < len( tile_grid) and j < len( tile_grid[i]) and tile_grid[i][j].actionable != self:
                    self.watchlist.append( tile_grid[i][j])
    
    def seek_target( self):
        
        for tile in self.watchlist:
            if isinstance(tile.actionable, Monster):
                return tile
        return None
        
    def action( self):
        self.cycle= 1
        
        target= self.seek_target()
        if target != None:
            self.game_map.create_particle("Cannonball", self.home, target)
            self.cycle= self.reload_time
    #
#