# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 19:34:09 2016

@author: Alexandre Young
"""

class CycleManager:
    #Decide quando executar os objetos do jogo (monstros, torres, etc)

    def __init__(map):
        
        self.monster= map.monster
        self.tower= map.tower
        self.castle= map.castle
        self.cyclecounter= 0 # conta qual ciclo estamos
        self.cyclelimit= 27720
        
    #
    
    def cycle():
        
        for monster in self.monster:
            
            if self.cyclecounter % monster.cyclespeed == 0
                monster.main()
        #
                
        for tower in self.tower:
            
            if self.
        #
            
    #
        
        
        
        