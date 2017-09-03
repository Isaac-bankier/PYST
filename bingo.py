###############################
#           bingo.py          #
#          Play bingo         #
#      By Isaac Bankier       #
###############################

import random

class game(object):

    def __init__(self, size=100, initialFill = 0.15, spacer=" ", taken="__"):
        #Find the ideal hight and width of the board.
        self.width = 1
        self.hight = size
        for i in range(1, int(size/2)):
            j = size / i
            if abs(j - i) < abs(self.width - self.hight):
                self.width = j
                self.hight = i

        #Fill the board with the numbers 0 to 99 and then set some to be blank
        self.board = [taken if random.random() < (1.0 - initialFill) else str(y).rjust(2, "0") for y in [x for x in range(0, size)]]

        #Set the attributes of the class.
        self.width = int(self.width)
        self.hight = int(self.hight)
        self.size = size
        self.initialFill = initialFill
        self.spacer = spacer
        self.taken = taken

    def printBoard(self):
        #Go through the boardStr and place a newline every time there should be a new line.
        boardStr = ""
        for i in range(0, self.size):
            if i % (self.width) == 0:
                boardStr += "\n"
            boardStr += self.board[i]+self.spacer
        return boardStr

    #Remove a number from the board.
    def play(self, number):
        self.board[number]=self.taken

g=game()

userIn = ""

#while the user hasn't entered q remove the selected character.
while userIn != "q":
    print(g.printBoard())
    userIn = input("\nEnter the called number or type 'q' to quit: ")
    try:
        g.play(int(userIn))
    except:
        continue
