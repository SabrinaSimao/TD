from actionable import Tower

class Cannon(Tower):
    attack_range= 3
    bullet= "Cannonball"
    icon= "Cannon"
    reload_time= 120
    cost = 10
    
class archer_tower(Tower):
    attack_range= 3
    bullet= "Cannonball"
    icon= "archer_tower"
    reload_time= 60
    cost = 5
    
def tower_cost(selected_tower):
    if selected_tower == "Cannon":
        return 10
    if selected_tower == "archer":
        return 5