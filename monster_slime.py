class Monster:
    cycle= 60
    def __init__ (self, mapa):
        self.mapa=mapa
    
    def main(self):
        #função que executa o monstro, chamada por CycleManager
        self.move()
        if self.current_hp == 0:
            self.mapa.erase(self)
            
    #def move(self):
    #TODO: função move()    

class Slime (Monster):
    icon = "slime.bmp"
    max_hp = 10
    cycle = 60
    
    def __init__ (self, mapa):
        self.current_hp= self.max_hp
        self.mapa= mapa
        
