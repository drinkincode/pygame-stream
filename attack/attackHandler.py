from attack.attack import Attack
class AttackHandler():
    def __init__(self, __attackList=[]):
        self.attackList = []
        
        for atkDict in __attackList:
            
            atkName = atkDict['atkName']
            atkDamage = atkDict['atkDamage']
            atkLevel = atkDict['atkLevel']
            atkCost = atkDict['atkCost']
            
            self.attackList.append(Attack(atkName, atkDamage, atkLevel, atkCost))
    
    
    def print_attacks(self):
        print('Attacks - ')
        for i in range(len(self.attackList)):
            attack = self.attackList[i]
            attack.print_attack()

    def add_attack(self, atkDict):
        
        atkName = atkDict['atkName']
        atkDamage = atkDict['atkDamage']
        atkLevel = atkDict['atkLevel']
        atkCost = atkDict['atkCost']
        
        try:
            self.attackList.append(Attack(atkName, atkDamage, atkLevel, atkCost))
            return True
        except():
            return False
        