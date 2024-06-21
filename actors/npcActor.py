from actors.actor import Actor
from board.boardHandler import BoardHandler

class NpcActor(Actor):
    
    def __init__(self, npcDict: dict):
        self.actorDict = npcDict['actor']
        
        # actor params
        name = self.actorDict['name']
        statsList = self.actorDict['statsList']
        attackList = self.actorDict['attackList']
        x = self.actorDict['x']
        y = self.actorDict['y']
        
        super().__init__(name, statsList, attackList, x, y)
    
        self.path = list[npcDict['path']]
        
        self.nextMove = self.path[0]
        self.nextMoveTicks = self.nextMove[1]

        self.pathLoc = 0
        
    def setPath(self, location, timePerMove):
        # [[newX, newY], 1000], [[newX, newY], 1000]]
        # location: [x, y]
        self.path.append([location, timePerMove])
        return self.path
    
    def getUpdate(self, ticks):
        
        # No Update
        if ticks >= self.nextMoveTicks:
            return False
        
        # set new loc -> [x, y]
        newLoc = self.nextMove[0]
        
        self.pathLoc += 1
        
        # is end of path
        if self.pathLoc >= len(self.path):
            self.path.reverse()
            self.pathLoc = 0
        
        # set next move
        self.nextMove = self.path[self.pathLoc]        
        # update ticks to next move
        self.nextMoveTicks = ticks + self.nextMove[1]
        
        return newLoc

