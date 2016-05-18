import random

class Spawn:
    ##
    #Overview:
    #Spawn controla e define a sequência de monstros a serem criados
    #A classe GameMap contem uma instância de Spawn para cada ponto origem de monstros
    ##
    #Atributos:
    #
    #   - wave_wait - intervalo de criação entre o fim de uma wave e a próxima, em ciclos 
    #   - self.cycle - intervalo em ciclos até a próima execução de action()
    #   - mapa - Referência ao objeto Mapa, para pedir para ele criar os monstros
    
    def __init__ (self, game_map, home):    
        self.wave_wait= 600
        self.cycle= self.wave_wait
        self.wave= None
        self.game_map= game_map
        self.home= home #objeto tipo Tile, onde o Spawn se encontra
        self.difficulty= 2
        self.packet_list= [MonPacket1, MonPacket2, MonPacket3, MonPacket4, MonPacket5, MonPacket6, MonPacket7]
        self.boss_wave_list=[
            Wave(60, BossPacket1.monster),
            Wave(60, BossPacket2.monster)
            ]
        
    def make_wave (self):
        
        ##Criar as waves e devolver ela
        
        #loop if pra criar wave                   
            
        difficulty = self.difficulty
        monster_list= []

        while difficulty != 0:
            
            n = len(self.packet_list)
            for i in range(len(self.packet_list)):
                if (self.packet_list[i].cost) > difficulty:
                    n = i
                    break
            
            packet= self.packet_list[random.randint(0, n-1)]
            
            for monster in packet.monster:
                monster_list.append(monster)
                
            difficulty -= packet.cost         
                
            time = int(120 / (self.difficulty**(1/2)))
            
            return Wave(time, monster_list)
        ##
        
    def action(self):
        ## Se não tiver Wave ativa, carregar a próxima
        if self.wave == None:
            if self.difficulty % 10 != 0:
                self.wave= self.make_wave()
            else:
                self.wave=self.boss_wave_list[self.difficulty//10] 
            self.difficulty+= 2
        ##
            
        ## Pedir pro mapa criar o monstro, se não conseguir criar (retorno -1)  tentar denovo próximo ciclo
        if self.game_map.create(self.wave.monster_list[0], self.home) != -1:
            
            self.wave.monster_list.pop(0)
            self.cycle= self.wave.monster_interval
        else:
            
            self.cycle= 1
        ##
            
        if len( self.wave.monster_list ) == 0:
            self.wave= None
            self.cycle= self.wave_wait
    #
class Wave:
    def __init__ (self,monster_interval, monster_list):
        self.monster_interval= monster_interval #intervalo de espera entre criar os monstros, em ciclos
        self.monster_list= monster_list #lista dos TIPOS de monstro a serem gerados

class MonPacket1:
    cost= 1
    monster= ["Slime"]
class MonPacket2:
    cost= 2
    monster= ["Slime_nobg"]
class MonPacket3:
    cost= 3
    monster= ["GlassSlime"]
class MonPacket4:
    cost= 4
    monster= ["JohnnyBravoSlime"]
class MonPacket5:
    cost= 5
    monster= ["Slime_MagnataBMP"]
class MonPacket6:
    cost= 6
    monster= ["Slime_Fire"]
class MonPacket7:
    cost= 7
    monster= ["Olho"]
class BossPacket1:
    monster= ["Slime","Slime","Slime", "Slime", "GlassSlime", "GlassSlime", "Olho"]
class BossPacket2:
    cost= 20
    monster= ["Slime", "Slime", "Slime", "Slime", "GlassSlime", "Slime_Fire", "Slime_Fire", "Slime_Fire", "Olho", "Olho", "Olho"]
