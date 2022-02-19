from main import *
from header import *

def setup():
    size(game.startX + game.boardWidth * game.tileSize, game.startY + game.boardHeight * game.tileSize)
    stroke(0)
    background(0, 0, 0)
    initBoard()
    restart()
    noLoop()
    #print(board)
    
def draw():
    drawBoard()
    
def mouseClicked():
    tileX = ((mouseX - game.startX) ) / game.tileSize
    tileY = ((mouseY - game.startY) ) / game.tileSize

    if mouseButton == LEFT:
        mouseLeftClick(tileX, tileY)
        #print("------ Your pressed board[" + str(tileX) + "][" + str(tileY) + "] with a type of " + str(game.board[tileX][tileY].type) + " and revealed: " + str(game.board[tileX][tileY].revealed))
    elif mouseButton == RIGHT:
        mouseRightClick(tileX, tileY)
    redraw()

    
def keyTyped():
    tileX = ((mouseX - game.startX) ) / game.tileSize
    tileY = ((mouseY - game.startY) ) / game.tileSize

    if key == 'R' or key == 'r':      
        restart()
    elif key == ' ':
        #print("------ Your pressed board[" + str(tileX) + "][" + str(tileY) + "] is flagged: " + str(game.board[tileX][tileY].flagged) + " and revealed: " + str(game.board[tileX][tileY].revealed))
        mouseRightClick(tileX, tileY)
    elif key == 'o' or key == 'O':
        mouseLeftClick(tileX, tileY)

    redraw()
