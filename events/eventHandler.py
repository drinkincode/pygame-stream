from board.boardHandler import BoardHandler
from actors.playerActor import PlayerActor
import pygame.event, sys
from pygame.locals import *

class EventHandler():
    def __init__(self, player: PlayerActor, boardHandler: BoardHandler):
        self.player = player
        self.boardHandler = boardHandler
        self.eventQueue = []
        
    def event(self, eventQueue: list, updatesList: list):
        for event in eventQueue: # event handling loop
            currXYList = self.boardHandler.actorPosDict[self.player.name]
            newX = currXYList[0]
            newY = currXYList[1]
            
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN:
                newX, newY = self.keyDown(event, newX, newY)

                        
            updatesList.append([self.player, newX, newY])
                
        return updatesList
    

    def keyDown(self, event: pygame.event, newX, newY):
        # left
        if ((event.key == K_LEFT or event.key == K_a) and self.player.isDirection(K_LEFT)):
            newX -= 1
        # right
        elif ((event.key == K_RIGHT or event.key == K_a) and self.player.isDirection(K_RIGHT)):
            if newX < self.boardHandler.boardWidth - 1:
                newX += 1
            else: 
                newX = 0
        # up
        elif ((event.key == K_UP or event.key == K_a) and self.player.isDirection(K_UP)):
            newY -= 1
        # down
        elif ((event.key == K_DOWN or event.key == K_a) and self.player.isDirection(K_DOWN)):
            if newY < self.boardHandler.boardHeight - 1:
                newY += 1
            else: 
                newY = 0
        return newX, newY
                        