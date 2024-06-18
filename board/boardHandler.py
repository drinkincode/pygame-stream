from actors.actor import Actor
class BoardHandler():
    def __init__(self, boardWidth, boardHeight):
        self.board = self.createBoard(boardWidth, boardHeight)
        
        # {
        #    'actorName': [x, y]
        # }
        self.actorPosDict = {}
        
    def createBoard(self, boardWidth, boardHeight):
        board = [ [0]* boardHeight for _ in range(boardWidth) ]
        return board
    
    # updatesList: [actor, x, y]
    def updateBoard(self, updatesList):
        for update in updatesList:
            actor = update[0]
            x = update[1]
            y = update[2]
            
            isOnBoard = self.doesActorExist(actor)
            
            if isOnBoard:
                currX = isOnBoard[0]
                currY = isOnBoard[1]
                self.board[currX][currY] = 0
                
            self.board[x][y] = actor
            self.actorPosDict[actor.name] = [x, y]
            return True
            
    def doesActorExist(self, actor: Actor):
        res = False
        if actor.name in self.actorPosDict.keys():
            res = self.actorPosDict[actor.name]
        return res