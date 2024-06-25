from actors.actor import Actor
from actors.npcActor import NpcActor

class NpcHandler():
    def __init__(self):
       self.npcList = []
       
    def createBulkNpcs(self, npcsList: list):
        for npcDict in npcsList:
            self.createNpc(npcDict)
            
    def createNpc(self, npcDict: dict):
        # actor: Actor, updatesList: list, path: list, timePerMove
        
        
        newNpc = NpcActor(npcDict)
        self.npcList.append(newNpc)
        return True
    
    def getNpcUpdates(self, ticks, updatesList: list):
        for i in range(len(self.npcList)):
            hasUpdate = self.npcList[i].getUpdate(ticks)
            if hasUpdate:
                x = hasUpdate[0]
                y = hasUpdate[1]
                updatesList.append([self.npcList[i], x, y])
                
        return updatesList
