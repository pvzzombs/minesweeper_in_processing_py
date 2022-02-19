from header import *

class Cell:
    def __init__(self, x, y, type, revealed, flagged):
        self.x = x
        self.y = y
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def isValid(self, x, y):
        if x >= 0 and x <= (game.boardWidth-1) and y >= 0 and y <= (game.boardHeight-1):
            return True
        return False

    def amIValid(self):
        if self.x >= 0 and self.x <= (game.boardWidth-1) and self.y >= 0 and self.y <= (game.boardHeight-1):
            return True
        return False

    def isValidAndNotMine(self, x, y):
        if x >= 0 and x <= (game.boardWidth-1) and y >= 0 and y <= (game.boardHeight-1) and game.board[x][y].type != -1:
            return 1
        return 0

    def isMine(self, x, y):
        if game.board[x][y].type == -1:
            return 1
        return 0

    def amIMine(self):
        if game.board[self.x][self.y].type == -1:
            return 1
        return 0

    def reveal(self):
        if game.gameOver == True:
            if self.type == -1 and not(self.revealed):
                # if a mine
                # reveal other mines
                self.revealed = True
                #print("Reveal other tiles...")
                for y in range(0, game.boardHeight, 1):
                    for x in range(0, game.boardWidth, 1):
                        temp = game.board[x][y]
                        if temp.isMine(x, y) and temp.revealed == False:
                            game.board[x][y].reveal()
            return

        #print("Current: " + str(self.x) + " " + str(self.y))
        if self.revealed == True:
            # gameOver[1] += 1
            # print(str(gameOver[1]) + " " + str(self.x) + " " + str(self.y))
            return
        else:
            if self.type == -1:
                return
            elif self.type == 0:
                # reveal neighbors
                self.revealed = True
                if self.flagged:
                    self.flagged = False
                if self.isValid(self.x, self.y-1):
                    game.board[self.x][self.y-1].reveal()
                if self.isValid(self.x+1, self.y):
                    game.board[self.x+1][self.y].reveal()
                if self.isValid(self.x, self.y+1):
                    game.board[self.x][self.y+1].reveal()
                if self.isValid(self.x-1, self.y):
                    game.board[self.x-1][self.y].reveal()
            else:
                self.revealed = True

    def spriteID(self):
        if self.flagged:
            return 11
        elif self.revealed:
            t = self.type
            if t == -1:
                return 9
            else:
                return t
        else:
            return 10
