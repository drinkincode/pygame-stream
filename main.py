import random, pygame, sys, os
from pygame.locals import *
from actors.actor import Actor
from board.boardHandler import BoardHandler

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

BGCOLOR = GREEN
LIGHTBGCOLOR = GRAY
BOXCOLOR = CYAN
HIGHLIGHTCOLOR = BLUE

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)


def main():
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
    updatesList = []
    
    # create new player
    name = 'john'
    statsList = [
        ['healthStats', 100],
        ['stamina', 100]
    ]
    attackList = [
        {
            'atkName': 'punch',
            'atkDamage': 10,
            'atkLevel': 1,
            'atkCost': []
        }
    ]
    xPos = 8
    yPos = 9
    
    player = Actor(name, statsList, attackList)
    player.color = RED
   
    updatesList.append([player, xPos, yPos])
    boardHandler.updateBoard(updatesList)
    drawBoard(boardHandler.board)
    
    while True: # main game loop
        mouseClicked = False
        # direction sprite is facing
        direction = RIGHT
        updatesList = []
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
        
        # drawBoard(boardHandler.board)
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

def startGame():
    return True


if __name__ == '__main__':
    main()