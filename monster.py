class Monster:
    cycle= 60
    icon = "Default"
    hp_max = 10
    
    
    def __init__ (self, game_map, home):
        self.mapa= mapa
        self.home= home
        self.game_map= game_map
    
    def main(self):
        #função que executa o monstro, chamada por CycleManager
        self.move()
        if self.current_hp == 0:
            self.mapa.erase(self)
            
    def move(self):
        #tenta se pra a tile abaixo
        #em sucesso:
        #retirar sua instância da tile anterior
        #atualziar home
        #checar se chegou no castelo
        #em falha:
        #nada
    
        None
    
        

class Slime (Monster):
    icon = "Slime"
    hp_max = 10
    cycle= 60
    
