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
        self.current_wave= None
        self.game_map= game_map
        self.home= home #objeto tipo Tile, onde o Spawn se encontra
        self.dificuldade = 2
        self.packet_list=[MonPacket1, MonPacket2, MonPacket3, MonPacket4, MonPacket5, MonPacket6, MonPacket7,
                          MonPacket_Boss1, MonPacket_Boss2]
        self.wave_list1 =[Wave(120, [MonPacket_Boss1])]#Pacote dos Bosses
        self.wave_list2 =[Wave(80, [MonPacket_Boss2])]
        
    def wave_maker (self):
        
        ##Criar as waves e guardar em uma lista
        self.wave_list=[]
        #loop if pra criar wave apenas se acabar a ultima                    
        if self.current_wave == None:        
            
            soma = self.dificuldade
            lista_de_mobs = []

            while soma > 0:
                n = 0
                for i in range(len(self.packet_list)):
                    if (self.packet_lista[i].cost) <= soma:
                        n = i
                    else:
                        break
                
                selecionado = random.randint(0,n)
                lista_de_mobs.append(self.packet_lista[selecionado])
                soma -= self.packet_list[selecionado]            
            lista_de_monster = []    
            for i in range(len(lista_de_mobs)):
                lista_de_monster.append(lista_de_mobs[i].monster)
            time = int(360 / (self.dificuldade**(1/2)))
            self.wave_list.append( Wave(time, lista_de_monster) )
            self.dificuldade += 2
            
            
        ##
        
    def action(self):
        ## Se não tiver Wave ativa, carregar a próxima
        if self.current_wave == None:
            self.current_wave= (self.wave_list[0])
            self.wave_list.pop(0)
        ##
            
        ## Pedir pro mapa criar o monstro, se não conseguir criar (retorno -1)  tentar denovo próximo ciclo
        if self.game_map.create(self.current_wave.monster_list[0], self.home) != -1:
            
            self.current_wave.monster_list.pop(0)
            self.cycle= self.current_wave.monster_interval
        else:
            
            self.cycle= 1
        ##
            
        if len( self.current_wave.monster_list ) == 0:
            self.current_wave= None
            self.cycle= self.wave_wait
    #
class Wave:
    def __init__ (self,monster_interval, monster_list):
        self.monster_interval= monster_interval #intervalo de espera entre criar os monstros, em ciclos
        self.monster_list= monster_list #lista dos TIPOS de monstro a serem gerados

class MonPacket1:
    cost= 1
    monster= "Slime"
class MonPacket2:
    cost= 2
    monster= "Slime_nobg"
class MonPacket3:
    cost= 3
    monster= "GlassSlime"
class MonPacket4:
    cost= 4
    monster= "JohnnyBravoSlime"
class MonPacket5:
    cost= 5
    monster= "Slime_MagnataBMP"
class MonPacket6:
    cost= 6
    monster= "Slime_Fire"
class MonPacket7:
    cost= 7
    monster= "Olho"
class MonPacket_Boss1:
    cost= 10
    monster= "Slime","Slime","Slime", "Slime", "GlassSlime", "GlassSlime", "Olho"
class MonPacket_Boss2:
    cost= 20
    monster= "Slime", "Slime", "Slime", "Slime", "GlassSlime", "Slime_Fire", "Slime_Fire", "Slime_Fire", "Olho", "Olho", "Olho"
