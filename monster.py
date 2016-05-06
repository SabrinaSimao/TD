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
        if self.hp_current == 0:
            self.mapa.erase(self)
            
    def move(self):
        #tenta se pra a tile abaixo
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


class JohnnyBravoSlime (Monster):
    icon = "JohnnyBravoSlime"
