# -*- coding: utf-8 -*-
"""
Created on Fri May 20 21:57:31 2016

@author: Alexandre Young
"""
import particle


class ParticleHolder:
    
    def __init__(self):
        self.shadow= []
        self.particle= []
            
    def create(self, target_particle, parameters):
        ##  Overview
        #  cria uma instância tipo Particle para um Tile alvo
        #----------------------------------------------------------------------
        ##  Parâmetros:
        #  particle: uma chave em String correspondente ao tipo de particle a
        # ser criada
        #  parameters: tuple representado os parâmetros de criação de
        # particle
        #----------------------------------------------------------------------
        ## Retorno:
        #  int 1 em caso de sucesso
        #  int -1 em caso de falha
        ##
        key_dict={
            "Cannonball": particle.Cannonball,
            "Shadow": particle.Shadow,
            "BouncingDoppleganger": particle.BouncingDoppleganger
        }
        
        target_particle= key_dict[target_particle](*parameters)
        
        if isinstance(target_particle, particle.Shadow):
            self.shadow.append(target_particle)
        else:
            self.particle.append(target_particle)
        return 1
        
    def erase(self, target_particle):
        ##  Overview
        #  apaga a instância de Particle recebida
        #----------------------------------------------------------------------
        ##  Parâmetros
        #  particle: instância tipo Particle
        #----------------------------------------------------------------------
        #  Retorno
        #  int 1 em caso de sucesso
        #  int -1 em caso de falha
        ##
    
        if isinstance(target_particle, particle.Shadow):
    
            for i in range(len(self.shadow)):
                if self.shadow[i] == target_particle:
                    self.shadow.pop(i)
                    return 1
        else:
            
            for i in range(len(self.particle)):
                if self.particle[i] == target_particle:
                    self.particle.pop(i)
                    return 1
        return -1