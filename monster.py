from actionable import Monster

class Slime (Monster):
    backup= "Slime"
    hp_max = 10
    gold= 5
    wait= 60
    
class Slime_nobg (Monster):
    backup= "Slime_nobg"
    hp_max = 5
    wait= 50
    jump= 10
    gold= 10

class GlassSlime (Monster):
    backup= "GlassSlime"
    hp_max = 50
    wait= 120
    gold= 10

class JohnnyBravoSlime (Monster):
    backup= "JohnnyBravoSlime"
    hp_max = 30
    wait= 60
    gold= 15

class Slime_MagnataPNG (Monster):
    backup= "Slime_MagnataPNG"
    hp_max = 50
    wait= 60
    gold= 50
    
class Slime_Fire (Monster):
    backup= "Slime_Fire"
    hp_max = 60
    wait= 60
    gold= 60
    
class Olho (Monster):
    backup= "Olho"
    hp_max = 180
    wait= 20
    gold= 80
    
#class FatSlime (Monster):
#    icon = "FatSlime"