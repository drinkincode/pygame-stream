from actor import Actor
class NpcActor(Actor):
    def __init__(self, name, statsList, __attackList = [], __x = -1, __y = -1):
        super().__init__(name, statsList, __attackList = [], __x = -1, __y = -1)
        self.paths = []
        
    def setPath(self, direction, distance, timePerMove):
        # [['right', 5, 1000], ['up', 5, 1000]]
        self.paths.append([direction, distance, timePerMove])
        
        return True
    
    
