# store a value as an array in order to be passed as reference

class Settings:
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.boardWidth = 30
        self.boardHeight = 20
        self.tileSize = 30
        self.totalMines = 30
        self.board = []
        self.mines = []
        self.gameOver = False
        self.win = False
        self.imgNames=[]
        self.imgs = []
        #self.update = True
        self.font = None

    def prepareImages(self):
        for i in range(0, 13, 1):
            self.imgNames.append(str(i) + ".png")

    def loadImages(self):
        for i in range(0, len(self.imgNames), 1):
            self.imgs.append(loadImage(self.imgNames[i]))

game = Settings()
