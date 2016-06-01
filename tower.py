from actionable import Tower

class Cannon(Tower):
    attack_range= 5
    bullet= "Cannonball"
    icon= "Cannon"
    reload_time= 120
    cost = 10
    
class ArcherTower(Tower):
    attack_range= 3
    bullet= "Arrow"
    icon= "Archer_tower"
    reload_time= 50
    cost = 5