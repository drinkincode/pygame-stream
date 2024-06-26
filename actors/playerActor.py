from actors.actor import Actor
class PlayerActor(Actor):
    def __init__(self, initDir, playerName, playerStatsList, playerAttackList, x, y):
        super().__init__(playerName, playerStatsList, playerAttackList, x, y)
        self.direction = initDir
        
    def isDirection(self, direction)->bool:
        if self.direction == direction:
            return True
        self.direction = direction
        return False
    
    