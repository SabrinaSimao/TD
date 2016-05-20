from actionable import Tower

class Cannon(Tower):
    attack_range= 3
    bullet= "Cannonball"
    icon= "Cannon"
    reload_time= 120
    cost = 10
    
class ArcherTower(Tower):
    attack_range= 3
    bullet= "Cannonball"
    icon= "archer_tower"
    reload_time= 50
    cost = 5