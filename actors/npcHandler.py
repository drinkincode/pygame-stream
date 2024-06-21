from actors.actor import Actor
from actors.npcActor import NpcActor

class NpcHandler():
    def __init__(self):
       self.npcList = []
       
    def createNpc(self, npcDict: dict):
        # actor: Actor, updatesList: list, path: list, timePerMove
        
        actor = npcDict['actor']
        pathList = npcDict['path']
        
        newNpc = NpcActor(actor, pathList)
        self.npcList.append(newNpc)
        return True
    
    def createBulkNpcs(self, npcsList: list):
        for npcDict in npcsList:
            self.createNpc(npcDict)
            
    def getNpcUpdates(self, ticks, updatesList: list):
        for i in range(len(self.npcList)):
            hasUpdate = self.npcList[i].getUpdate(ticks)
            if hasUpdate:
                x = hasUpdate[0]
                y = hasUpdate[1]
                updatesList.append([self.npcList[i], x, y])
                
        return updatesList
    
    # def setPath(self, direction, distance):
    #     # [['right', 5, 1000], ['up', 5, 1000]]
    #     self.paths.append([direction, distance])
    #     return self.paths