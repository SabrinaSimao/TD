class Monster:
    cycle= 60
    icon = "Default"
    hp_max = 10
    
    
    def __init__ (self, game_map, home):
        self.game_map= game_map
        self.home= home
        self.game_map= game_map
        self.hp_current= self.hp_max
    
    def main(self):
        #função que executa o monstro, chamada por CycleManager
        self.move()
            
    def move(self):
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
    
    def take_damage(self, damage):
        self.hp_current -= damage
        if self.hp_current <= 0:
            self.game_map.erase(self, self.home)
                    
    def invade(self):
        #em caráter temporário:
        self.game_map.castle.take_damage(1)
        self.game_map.erase(self, self.home)
        
    
        

class Slime (Monster):
    icon = "Slime"
    hp_max = 10
    cycle= 60
    
class Slime_nobg (Monster):
    icon = "Slime_nobg"
    hp_max = 10
    cycle= 60

class GlassSlime (Monster):
    icon = "GlassSlime"
    hp_max = 50
    cycle= 120

class JohnnyBravoSlime (Monster):
    icon = "JohnnyBravoSlime"
    hp_max = 30
    cycle= 60

#class FatSlime (Monster):
#    icon = "FatSlime"