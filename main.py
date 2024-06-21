import random, pygame, sys, os
from pygame.locals import *
from actors.actor import Actor
from board.boardHandler import BoardHandler
from actors.npcHandler import NpcHandler
 
FPS = 30
WINDOWWIDTH = 2000
WINDOWHEIGHT = 1200
BOXSIZE = 100
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

NPC_TIME_TO_MOVE = 1000

def main():
    npc_num_moves = 1
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    pygame.display.set_caption('Game Window')
    
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'
    
    DISPLAYSURF.fill(BGCOLOR)
    
    
    boardHandler = BoardHandler(BOARDWIDTH, BOARDHEIGHT)
    player, NpcHandler = startGame(boardHandler)
    while True: # main game loop
        mouseClicked = False
        # direction sprite is facing
        direction = RIGHT
        updatesList = []
        updatesList = NpcHandler.getNpcUpdates(pygame.time.get_ticks() , updatesList)
        for event in pygame.event.get(): # event handling loop
            currXYList = boardHandler.actorPosDict[player.name]
            newX = currXYList[0]
            newY = currXYList[1]
            
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN:
                # left
                if (event.key == K_LEFT or event.key == K_a):
                    currXYList = boardHandler.actorPosDict[player.name]
                    newX -= 1
                # right
                elif (event.key == K_RIGHT or event.key == K_a):
                    currXYList = boardHandler.actorPosDict[player.name]
                    if newX < BOARDWIDTH - 1:
                        newX += 1
                    else: 
                        newX = 0
                # up
                elif (event.key == K_UP or event.key == K_a):
                    currXYList = boardHandler.actorPosDict[player.name]
                    newY -= 1
                
                # down
                elif (event.key == K_DOWN or event.key == K_a):
                    currXYList = boardHandler.actorPosDict[player.name]
                    if newY < BOARDHEIGHT - 1:
                        newY += 1
                    else: 
                        newY = 0
                        
        updatesList.append([player, newX, newY])
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

def npcActorUpdates(boardHandler: BoardHandler, npc_num_moves):
    updatesList = []
    for key in boardHandler.actorPosDict.keys():
        actorPosList = boardHandler.actorPosDict[key]
        
        x = actorPosList[0]
        y = actorPosList[1]
        
        actor = boardHandler.board[x][y]
        
        if (pygame.time.get_ticks() / NPC_TIME_TO_MOVE) > npc_num_moves:
            if 'npc' in actor.name:
                actor.x += 1
                updatesList.append([actor, actor.x, actor.y])
                npc_num_moves += 1
    return updatesList, npc_num_moves

def startNcpHandler():
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
                'xPos': 0,
                'yPos': 0,
                'color': RED
            },
            'path': [],
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
                'xPos': 0,
                'yPos': 0,
                'color': RED
            },
            'path': [],
        }
    ]
    npcHandler = NpcHandler()
    npcHandler.createBulkNpcs
    return npcHandler
           
def startGame(boardHandler: BoardHandler):
    updatesList = []
    npcHandler = startNcpHandler()
    # create new player dict
    initActorsList = [
        {
            'name': 'john', 
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
            'xPos': 8,
            'yPos': 9,
            'color': GREEN
        },
        
        # {
        #     'name': 'npc', 
        #     'statsList': [
        #         ['healthStats', 100],
        #         ['stamina', 100]
        #     ],
        #     'attackList': [
        #         {
        #             'atkName': 'punch',
        #             'atkDamage': 10,
        #             'atkLevel': 1,
        #             'atkCost': []
        #         }
        #     ],
        #     'xPos': 0,
        #     'yPos': 0,
        #     'color': RED
        # }
    ]

    for actor in initActorsList:
        newActor = Actor(actor['name'], actor['statsList'], actor['attackList'], actor['xPos'], actor['yPos'])
        newActor.color = actor['color']
        
        updatesList.append([newActor, newActor.x, newActor.y])
    
    updatesList = npcHandler.getNpcUpdates(pygame.time.get_ticks(), updatesList)
    
    boardHandler.updateBoard(updatesList)
    drawBoard(boardHandler.board)
    pygame.display.update()
    
    player = updatesList[0][0]
    return player, npcHandler
    

if __name__ == '__main__':
    main()