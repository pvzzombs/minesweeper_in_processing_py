from cell import *

## board[x][y][0] -> Mine
## board[x][y][1] -> Hidden, Revealed, Flag
def prepareBoard():
    game.font = createFont("Consolas", 16)
    game.prepareImages()
    game.loadImages()
    for x in range(0, game.boardWidth, 1):
        tempRow = []
        for y in range(0, game.boardHeight, 1):
            tempRow.append(Cell(x, y, 0, False, False))
        game.board.append(tempRow)
    #print("Done preparing board...")
    #print("Result is " + str(gameOver[0]))

def resetBoard():
    game.mines = []
    game.gameOver = False
    game.win = False
    for y in range(0, game.boardHeight, 1):
        for x in range(0, game.boardWidth, 1):
            game.board[x][y].type = 0
            game.board[x][y].revealed = False
            game.board[x][y].flagged = False
    #print("Done resetting board...")

def addMines(difficulty):
    # for i in range(0, difficulty, 1):
    #     #uniqueMine = True
    #     rTile = [int(floor(random(0, game.boardWidth))), int(floor(random(0, game.boardHeight)))]
    #     if len(game.mines):
    #         for j in range(0, len(game.mines), 1):
    #             while rTile[0] == game.mines[j][0] and rTile[1] == game.mines[j][1]:
    #                 rTile = [int(floor(random(0, game.boardWidth))), int(floor(random(0, game.boardHeight)))]
    #     game.board[rTile[0]][rTile[1]].type = -1
    #     game.mines.append(rTile)
    i = 0
    while i < difficulty:
        rTile = [int(floor(random(0, game.boardWidth))), int(floor(random(0, game.boardHeight)))]
        if game.board[rTile[0]][rTile[1]].type != 1:
            game.board[rTile[0]][rTile[1]].type = -1
            game.mines.append(rTile)
            i += 1
    #print("Done adding mines...")

def addHints():
    for y in range(0, game.boardHeight, 1):
        for x in range(0, game.boardWidth, 1):
            temp = game.board[x][y]
            if temp.isMine(x, y) == 0:
                m = 0
                #main check
                if temp.isValid(x, y-1):
                    m += temp.isMine(x, y-1)
                if temp.isValid(x+1, y-1):
                    m += temp.isMine(x+1, y-1)
                if temp.isValid(x+1, y):
                    m += temp.isMine(x+1, y)
                if temp.isValid(x+1, y+1):
                    m += temp.isMine(x+1, y+1)
                if temp.isValid(x, y+1):
                    m += temp.isMine(x, y+1)
                if temp.isValid(x-1, y+1):
                    m += temp.isMine(x-1, y+1)
                if temp.isValid(x-1, y):
                    m += temp.isMine(x-1, y)
                if temp.isValid(x-1, y-1):
                    m += temp.isMine(x-1, y-1)
                game.board[x][y].type = m
    #print("Done adding hints...")

def isSolvable():
    l = len(game.mines)
    for i in range(0, l, 1):
        x = game.mines[i][0]
        y = game.mines[i][1]
        temp = game.board[x][y]
        hint = 0
        hint += temp.isValidAndNotMine(x, y-1)
        hint += temp.isValidAndNotMine(x+1, y-1)
        hint += temp.isValidAndNotMine(x+1, y)
        hint += temp.isValidAndNotMine(x+1, y+1)
        hint += temp.isValidAndNotMine(x, y+1)
        hint += temp.isValidAndNotMine(x-1, y+1)
        hint += temp.isValidAndNotMine(x-1, y)
        hint += temp.isValidAndNotMine(x-1, y-1)
        if not(hint):
            return False
    return True


def checkIfWin():
    if game.gameOver:
        return

    allTilesRevealedExceptMines = False
    flaggedMines = 0

    for i in range(0, len(game.mines), 1):
        letx = game.mines[i][0]
        lety = game.mines[i][1]
        if game.board[letx][lety].amIMine() and game.board[letx][lety].flagged == True:
            flaggedMines += 1
        else:
            return
    #print("Mines cleared")
    for y in range(0, game.boardHeight, 1):
        for x in range(0, game.boardWidth, 1):
            tmp1 = game.board[x][y]
            if (tmp1.type >= 0 and tmp1.revealed) or (tmp1.amIMine() and tmp1.flagged):
                allTilesRevealedExceptMines = True
            else:
                allTilesRevealedExceptMines = False
                #print("------ Your pressed board[" + str(x) + "][" + str(y) + "] is flagged: " + str(tmp1.flagged) + " and revealed: " + str(tmp1.revealed))
                return
    #print("All non mine tiles revealed")
    if flaggedMines == game.totalMines and allTilesRevealedExceptMines:
        #print("You win...")
        game.win = True

def mouseLeftClick(tileX, tileY):
    tmp1 = game.board[tileX][tileY].revealed
    tmp2 = game.board[tileX][tileY].amIMine()
    tmp3 = game.board[tileX][tileY].flagged
    if not(tmp1):
        if tmp2:
            game.gameOver = True
            if tmp3:
                game.board[tileX][tileY].flagged = False
        game.board[tileX][tileY].reveal()
    checkIfWin()

def mouseRightClick(tileX, tileY):
    if not(game.board[tileX][tileY].revealed):
        if game.board[tileX][tileY].flagged:
            game.board[tileX][tileY].flagged = False
        else:
            game.board[tileX][tileY].flagged = True
    checkIfWin()

def drawBoard():
    for y in range(0, game.boardHeight, 1):
        for x in range(0, game.boardWidth, 1):
            t1 = game.board[x][y]
            t2 = t1.spriteID()
            if game.gameOver:
                if not(t1.amIMine()) and t1.flagged:
                    t2 = 12
            image(game.imgs[t2], game.startX + x*game.tileSize, game.startY + y*game.tileSize, game.tileSize, game.tileSize)
            #game.board[x][y].colorize()
            #rect(game.startX + x*game.tileSize, game.startY + y*game.tileSize, game.tileSize, game.tileSize)
    if game.win:
        textFont(game.font, 30)
        fill(0)
        text("You Win, Press R to restart", 10, 30)
    elif game.gameOver:
        textFont(game.font, 30)
        fill(0)
        text("Nice try, Press R to restart", 10, 30)

def initBoard():
    prepareBoard()

def restart():
    resetBoard()
    addMines(game.totalMines)
    addHints()
    print("Can be solved?: " + str(isSolvable()))
