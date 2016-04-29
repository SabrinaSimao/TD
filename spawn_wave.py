class Spawn:
    ##
    #Overview:
    #
    ##
    #Atributos:
    #
    #   - wave_wait - intervalo de criação entre o fim de uma wave e a próxima, em ciclos 
    #   - self.cycle - intervalo em ciclos até a próima execução de main()
    #   - mapa - Referência ao objeto Mapa, para pedir para ele criar os monstros
    
    def __init__ (self, mapa):
        
        self.wave_wait= 600
        self.cycle= self.wave_wait
        self.current_wave= None
        self.mapa= mapa
        
        
        
        ##Criar as waves e guardar em uma lista
        self.wave_list=[]
        
        self.wave_list.append( Wave(180, ["Slime", "Slime", "Slime"]) )
        self.wave_list.append( Wave(120, ["Slime","Slime", "Slime", "Slime", "Slime", "Slime", "Slime", "Slime"]) )
        ##
        
    def main(self):
        ## Se não tiver Wave ativa, carregar a próxima
        if self.current_wave == None:
            self.current_wave= (self.wave_list[0])
            self.wave_list.pop(0)
        ##
            
        ## Pedir pro mapa criar o monstro, se não conseguir criar (retorno -1)  tentar denovo próximo ciclo
        if self.mapa.create(self.current_wave.monster_list[0], "Spawn") != -1:
            
            self.current_wave.monster_list.pop(0)
            self.cycle= self.current_wave.monster_interval
        else:
            
            self.cycle= 1
        ##
            
        if len( self.currentwave.monster_list ) == 0:
            self.current_wave= None
            self.cycle= self.wave_wait
    #
class Wave:
    def __init__ (self,monster_interval, monster_list):
        self.monster_interval= monster_interval #intervalo de espera entre criar os monstros, em ciclos
        self.monster_list= monster_list #lista dos TIPOS de monstro a serem gerados
