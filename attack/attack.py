class Attack():
    def __init__(self, atkName, atkDamage, atkLevel = 1, atkCost = []):
        self.name = atkName
        self.damage = atkDamage
        self.attackLevel = atkLevel
        self.attackCost = atkCost
        
    def increase_damage(self, damageIncrease):
        self.damage += damageIncrease
        
    def increase_level(self, levels):
        self.attackLevel += levels
    
    # TODO add cost obj to costList
    def increase_cost(self, cost):
        self.attackCost.append(cost)
    
    def print_attack(self):
        print(self.name + ': ' + str(self.damage) + ', level: ' + str(self.attackLevel))
        print('Attack cost: ' + ''.join(self.attackCost))