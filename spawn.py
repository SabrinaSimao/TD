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
        
        
        
        ##Criar as waves e guardar em uma lista
        self.wave_list=[]
        
        self.wave_list.append( Wave(180, ["Slime_nobg", "Slime_nobg", "Slime_nobg"]) )
        self.wave_list.append( Wave(120, ["Slime_nobg", "JohnnyBravoSlime", "Slime_nobg", "GlassSlime"]) )
        self.wave_list.append( Wave(90, ["Slime_nobg", "JohnnyBravoSlime", "Slime_nobg", "GlassSlime", "Slime_MagnataBMP", "Slime_Fire"]) )
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
