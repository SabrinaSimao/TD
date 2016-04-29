class Monster:
    def __init__ (self, max_hp, speed):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.speed = speed
        
    def dead (current_hp):
        if current_hp == 0:
            return 'dead'

class Slime (Monster):
    icon = "slime.bmp"
    max_hp = 10
    speed = 60
    def __init__ (self, max_hp):
        self.current_hp = max_hp
