class BoardHandler():
    def __init__(self, boardWidth, boardHeight):
        self.board = self.createBoard(boardWidth, boardHeight)
        
    def createBoard(self, boardWidth, boardHeight):
        board = [[0] * boardWidth] * boardHeight
        return board