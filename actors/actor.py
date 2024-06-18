from attack.attackHandler import AttackHandler
from stats.baseStatHandler import BaseStatHandler
class Actor():
    def __init__(self, name, statsList, __attackList = [], __x = -1, __y = -1):
        self.name = name 
        self.statManager = BaseStatHandler(statsList)
        self.attackManager = AttackHandler(__attackList)
        self.x = __x
        self.y = __y
        
    def print_greeting(self):
        print('Hi! I\'m ' + self.name )
        
    #TODO Change to collision detection
    #TODO Calc new Location on Board
        #TODO Direction change
    #TODO Set NEW loction on Board
    #TODO Update Actor representation on display
    
    
    
    
        
        
    
    # def addAttack(self, atkName, atkDamage, __atkLevel = 1):
    #     newAttack = Attack(atkName, atkDamage, __atkLevel)
    #     self.attacksList.append(newAttack)
        