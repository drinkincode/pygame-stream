import random, pygame, sys
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

BGCOLOR = NAVYBLUE
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
    
    DISPLAYSURF.fill(BGCOLOR)
    boardHandler = BoardHandler(BOARDWIDTH, BOARDHEIGHT)
    drawBoard(boardHandler.board)
    
    while True: # main game loop
        mouseClicked = False
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def updateActorLocaction(board, actor: Actor):
    return board

def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (BOXSIZE) + XMARGIN
    top = boxy * (BOXSIZE) + YMARGIN
    return (left, top)
    
def drawBoard(board):
    for boxX in range(BOARDWIDTH):
        for boxY in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            
    


if __name__ == '__main__':
    main()