# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:12:16 2016

@author: Alexandre Young
"""

from math import sin
from math import pi

class Particle:
    pixel= 16
    icon= "Default"
    duration= 60
    
    def __init__(self, game_map, origin_tile, target_tile):
        self.origin_tile= origin_tile
        self.target_tile= target_tile
        self.game_map=game_map
        self.trajectory= Trajectory(self)
        self.step= 0
        
    def read_position(self):
        return int(self.trajectory.x_current), int(self.trajectory.y_current)
    
    def update(self):
     
        self.step+=1
        self.trajectory.update()
        
        if self.step == self.duration:
            self.erase()
    #
            
    def erase(self):
        self.game_map.particle_holder.erase(self)
    
#
    
class BouncingDoppleganger(Particle):
    pixel= 32
    
    def __init__(self, game_map, icon, origin_tile, target_tile, duration):
        self.game_map= game_map
        self.icon= icon
        self.origin_tile= origin_tile
        self.target_tile= target_tile
        self.duration= duration
        
        self.trajectory= Trajectory(self)
        self.arch= Arch(self)
        
        game_map.particle_holder.create("Shadow", (game_map, origin_tile, target_tile, "Big", duration))
        
        self.step= 0
        
    def update(self):
     
        self.step+= 1
        self.trajectory.update()
        self.arch.update()
        
        if self.step == self.duration:
            self.erase()
    #
            
    def read_position(self):
        return int(self.trajectory.x_current), int(self.trajectory.y_current)-self.arch.y_current
            
    def erase(self):
        self.game_map.particle_holder.erase(self)
        
        
        
     
class Trajectory:
    
    def __init__(self, particle):
        self.particle= particle
        
        self.x_current, self.y_current= particle.game_map.distance_between(particle.origin_tile, particle.game_map.tile_grid[0][0])
        self.x_current= self.x_current*particle.origin_tile.pixel + particle.origin_tile.pixel - particle.pixel
        self.y_current= self.y_current*particle.origin_tile.pixel + particle.origin_tile.pixel - particle.pixel
        
        width, height= particle.game_map.distance_between(particle.origin_tile, particle.target_tile)
        
        x_finish= self.x_current + width*particle.origin_tile.pixel
        y_finish= self.y_current + height*particle.origin_tile.pixel
        
        self.x_increment= (x_finish - self.x_current)*(1/particle.duration)
        self.y_increment= (y_finish - self.y_current)*(1/particle.duration)
        
    #
    
    def update(self):
        
        self.x_current-= self.x_increment
        self.y_current-= self.y_increment
    #
#
    
class Bullet(Particle):


    damage= 5
    
    def __init__(self, game_map, origin_tile, target_tile):
        self.origin_tile= origin_tile
        self.target_tile= target_tile
        self.game_map=game_map
        self.trajectory= Trajectory(self)
        self.arch= Arch(self)
        game_map.particle_holder.create("Shadow", (game_map, origin_tile, target_tile, "Small", self.duration) )
        
        self.step= 0
    #
    
    def update(self):
     
        self.step+=1
        self.trajectory.update()
        self.arch.update()
        
        if self.step == self.duration:
            self.erase()
    #
            
    def read_position(self):
        return int(self.trajectory.x_current), int(self.trajectory.y_current)-self.arch.y_current
            
    def erase(self):
        if self.target_tile.actionable != None:
            self.target_tile.actionable.take_damage(self.damage)
            
        self.game_map.particle_holder.erase(self)
#
        
class Arch:
    def __init__(self, bullet):
        self.bullet= bullet
        self.y_current= 0
        width= ( (bullet.trajectory.x_increment*bullet.duration )**2  + (bullet.trajectory.y_increment*bullet.duration)**2 )**(1/2)
        self.y_max= width/2**(1/2)
        if self.y_max < 0:
            self.y_max*=-1
        
    def update(self):
        self.y_current= sin(pi*(self.bullet.step/self.bullet.duration))*self.y_max
        
        
    
class Shadow(Particle):
    
    def __init__(self, game_map, origin_tile, target_tile, size, duration):
        self.origin_tile= origin_tile
        self.target_tile= target_tile
        self.game_map=game_map
        if size == "Small":
            self.backup= "Shadow"
        elif size == "Big":
            self.backup= "Big_Shadow"
            self.pixel= 32
        self.duration= duration
        self.trajectory= Trajectory(self)
        self.step= 0
        
        self.trajectory= Trajectory(self)
        self.step= 0
    #
        
    def update(self):
     
        self.step+= 1
        self.trajectory.update()
        
        if self.step%1 == 0:
            if self.icon == "Default":
                self.icon= self.backup
            else:
                self.icon= "Default"
            
        if self.step == self.duration:
            self.erase()
    #
#
    
class Cannonball(Bullet):
    icon= "Cannonball"
    damage= 10
    duration= 40
    
class Arrow(Bullet):
    #icon= "Arrow"
    icon= "Cannonball" #fix rápido temporário pra diferenciar mais a torre de arqueiros
    damage= 5
    duration= 15
#