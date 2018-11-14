import objects
import random

class Player:
    def __init__(self, newX, newY):
        self.x = newX   # x position of player
        self.y = newY   # y position of player
        self.size = 35
        self.policyTable = dict()   # this will be a dictionary of (state : action) pairs. This will be updated by value iteration and q-learning

    def getActionVector(self, board):
        # helper function called by aiMove() to get a vector of valid directions from the player's current position.

        validMoves = ["Left", "Right", "Up", "Down", "Stay"]

		# rule out which actions we can take depending on current and next x, y positions. Based on implementation in key.py
        if self.x == 0 or board.tiles[self.x-1][self.y].isWall():
		    validMoves.remove("Left")
        if self.x == board.width - 1 or board.tiles[self.x+1][self.y].isWall():
        	validMoves.remove("Right")
        if self.y == 0 or board.tiles[self.x][self.y-1].isWall():
        	validMoves.remove("Up")
        if self.y == board.height - 1 or board.tiles[self.x][self.y+1].isWall():
            validMoves.remove("Down")

        return validMoves

    def aiMove(self, board, graphics):
        # This function will be run in main.py main() function in the game loop.
        # board and graphics are the same as objects.board and objects.graphics. 
        # They're being passed to this function from main.py main() function

        boardSize = board.size  # grab the board size of the current board

        direction = random.choice(self.getActionVector(board))

        # set the direction vector for the player movement based on the newDirection variable
        xDirection = 0
        yDirection = 0

        # note that the x, y origin is at the top-left, which is why UP is -1 in the y direction.
        if direction == "Down":
            yDirection = 1
        elif direction == "Up":
            yDirection = -1
        elif direction == "Right":
            xDirection = 1
        elif direction == "Left":
            xDirection = -1

        #initial x and y positions
        x0 = self.x * boardSize + boardSize / 2
        y0 = self.y * boardSize + boardSize / 2

        # handle movement bounds checking. If player hits a wall or ends up on a perimeter tile, stop moving. 
        # Otherwise, keep moving and update graphics.
        if yDirection != 0:
            while ((self.y + yDirection >= 0 and self.y + yDirection < board.height) and 
            not (board.tiles[self.x][self.y + yDirection].isWall())):
                self.y += yDirection
                graphics.moveCanvas(0, boardSize * yDirection)
                
        elif xDirection != 0:
            while ((self.x + xDirection >= 0 and self.x + xDirection < board.width) and 
            not (board.tiles[self.x + xDirection][self.y].isWall())):
                self.x += xDirection
                graphics.moveCanvas(boardSize * xDirection, 0)

        #x and y positions after movement
        x1 = self.x * boardSize + boardSize / 2
        x2 = self.y * boardSize + boardSize / 2

        # render the line behind player
        graphics.drawLine(x0, y0, x1, x2)

    def move(self, event, newDirection):
        # pass argument None for event if you aren't using keyboard to move player. E.G: move(None, "Up")

        boardSize = objects.board.size  # grab the board size of the current board

        # set the direction vector for the player movement based on the newDirection variable
        xDirection = 0
        yDirection = 0

        # note that the x, y origin is at the top-left, which is why UP is -1 in the y direction.
        if newDirection == "Down":
            yDirection = 1
        elif newDirection == "Up":
            yDirection = -1
        elif newDirection == "Right":
            xDirection = 1
        elif newDirection == "Left":
            xDirection = -1

        #initial x and y positions
        x0 = self.x * boardSize + boardSize / 2
        y0 = self.y * boardSize + boardSize / 2

        # handle movement bounds checking. If player hits a wall or ends up on a perimeter tile, stop moving. 
        # Otherwise, keep moving and update graphics.
        if yDirection != 0:
            while ((self.y + yDirection >= 0 and self.y + yDirection < objects.board.height) and 
            not (objects.board.tiles[self.x][self.y + yDirection].isWall())):
                self.y += yDirection
                objects.graphics.moveCanvas(0, boardSize * yDirection)
                
        elif xDirection != 0:
            while ((self.x + xDirection >= 0 and self.x + xDirection < objects.board.width) and 
            not (objects.board.tiles[self.x + xDirection][self.y].isWall())):
                self.x += xDirection
                objects.graphics.moveCanvas(boardSize * xDirection, 0)

        #x and y positions after movement
        x1 = self.x * boardSize + boardSize / 2
        x2 = self.y * boardSize + boardSize / 2

        # render the line behind player
        objects.graphics.drawLine(x0, y0, x1, x2)