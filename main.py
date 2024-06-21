import random, pygame, sys, os
from pygame.locals import *
from actors.playerActor import PlayerActor
from actors.actor import Actor
from board.boardHandler import BoardHandler
from actors.npcHandler import NpcHandler
from events.eventHandler import EventHandler
 
FPS = 30
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
BOXSIZE = 50
BOARDWIDTH = 16
BOARDHEIGHT = 10

XMARGIN =  int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE))) / 2)

GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = CYAN
HIGHLIGHTCOLOR = BLUE

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

def main():
    npc_num_moves = 1
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    pygame.display.set_caption('Game Window')
    
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    
    
    DISPLAYSURF.fill(BGCOLOR)
    
    
    boardHandler = BoardHandler(BOARDWIDTH, BOARDHEIGHT)
    player, NpcHandler = startGame(boardHandler) 
    updatesList = []
    
    eventHandler = EventHandler(player, boardHandler)
    
    while True: # main game loop
        mouseClicked = False
        # direction sprite is facing
        direction = RIGHT
       
        updatesList = NpcHandler.getNpcUpdates(pygame.time.get_ticks(), updatesList)
        updatesList = eventHandler.event(pygame.event.get(), updatesList)

        boardHandler.updateBoard(updatesList)
        drawBoard(boardHandler.board)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (BOXSIZE) + XMARGIN
    top = boxy * (BOXSIZE) + YMARGIN
    return (left, top)
    
def drawBoard(board):
    for boxX in range(BOARDWIDTH):
        for boxY in range(BOARDHEIGHT):
            currBoxColor = BOXCOLOR
            if isinstance(board[boxX][boxY], Actor):
                currBoxColor = board[boxX][boxY].color
            left, top = leftTopCoordsOfBox(boxX, boxY)
            pygame.draw.rect(DISPLAYSURF, currBoxColor, (left, top, BOXSIZE, BOXSIZE))

def startNcpHandler():
    npcPath = []
    
    moveX = 1
    moveY = 1
    moveTime = 1000
    move = [[moveX, moveY], moveTime]
    npcPath.append(move)
    
    npcNumMoves = 4
    for i in range(npcNumMoves):
        moveX += 1
        move = [[moveX, moveY], moveTime]
        npcPath.append(move)
    
    npcPath2 = []
    moveY += 1
    moveTime += 500
    move = [[moveX, moveY], moveTime]
    npcPath2.append(move)
    for i in range(npcNumMoves):
        moveX += 1
        move = [[moveX, moveY], moveTime]
        npcPath2.append(move)
        
    print('npc1 path: ' + str(npcPath))
    print('npc2 path: ' + str(npcPath2))
    
    npcList = [
        
        {
            'actor': {
                'name': 'npc', 
                'statsList': [
                    ['healthStats', 100],
                    ['stamina', 100]
                ],
                'attackList': [
                    {
                        'atkName': 'punch',
                        'atkDamage': 10,
                        'atkLevel': 1,
                        'atkCost': []
                    }
                ],
                'x': 1,
                'y': 1,
                'color': RED
            },
            'path': npcPath,
        },
        {
            'actor': {
                'name': 'npc2', 
                'statsList': [
                    ['healthStats', 100],
                    ['stamina', 100]
                ],
                'attackList': [
                    {
                        'atkName': 'punch',
                        'atkDamage': 10,
                        'atkLevel': 1,
                        'atkCost': []
                    }
                ],
                'x': 1,
                'y': 2,
                'color': RED
            },
            'path': npcPath2,
        }
    ]
    npcHandler = NpcHandler()
    npcHandler.createBulkNpcs(npcList)
    return npcHandler
           
def startGame(boardHandler: BoardHandler):
    updatesList = []
    npcHandler = startNcpHandler()
    # create new player dict
    playerActorsDict = {
        'name': 'john', 
        'statsList': [
            ['healthStats', 100],
            ['stamina', 100],
        ],
        'attackList': [
            {
                'atkName': 'punch',
                'atkDamage': 10,
                'atkLevel': 1,
                'atkCost': []
            }
        ],
        'xPos': 8,
        'yPos': 9,
        'color': GREEN
    }
    
    playerName = playerActorsDict['name']
    playerStatsList = playerActorsDict['statsList']
    playerAttackList = playerActorsDict['attackList']
    x = playerActorsDict['xPos']
    y = playerActorsDict['yPos']
    y = playerActorsDict['yPos']
    playerDir = K_UP
    
    newActor = PlayerActor(playerDir, playerName, playerStatsList, playerAttackList, x, y)
    
    newActor.color = playerActorsDict['color']
    
    updatesList.append([newActor, newActor.x, newActor.y])
    
    updatesList = npcHandler.getNpcUpdates(pygame.time.get_ticks(), updatesList)
    
    boardHandler.updateBoard(updatesList)
    drawBoard(boardHandler.board)
    pygame.display.update()
    
    player = updatesList[0][0]
    return player, npcHandler

if __name__ == '__main__':
    main()