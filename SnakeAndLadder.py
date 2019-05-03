import random
import time


class LudoBoard(object):
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.cellOccupied = {}
        self.ladderLength = [0,0,0,5,7,9 ]
        self.boardLayout = []

        self._createBoard()
        self._addLadder()
        #self._printBoard()
        self._addSnake()
        self._printBoard()

    def _createBoard(self):
        for i in range(self.boardSize):
           self.boardLayout.append(0)

    def _printBoard(self):
        for index, value  in enumerate(self.boardLayout):
            print("%s=%s" % (index, value))

    def _addLadder(self):
       #Add Ladders
       for index, value in enumerate(self.boardLayout):
          cellValue = random.choice(self.ladderLength)
          if index+cellValue < self.boardSize:
              if cellValue > 0:
                  # Cell is occupied either by ladder head or ladder foot.
                  if index+cellValue in self.cellOccupied:
                      self.boardLayout[index] = 0
                      continue
                  if index in self.cellOccupied:
                      self.boardLayout[index] = 0
                      continue
                  self.cellOccupied[index] = 1
                  self.cellOccupied[index+cellValue] = 1
                  self.boardLayout[index] = cellValue
          else:
              self.boardLayout[index] = 0

    def _addSnake(self):
        for reverseIndex, value in reversed(list(enumerate(self.boardLayout))):
            cellValue = random.choice(self.ladderLength)
            if reverseIndex - cellValue > 0:
                # If cell value is less than 0, that it points to non existing cells.
                if cellValue > 0:
                    # Cell is occupied either by ladder head or ladder foot.
                    if reverseIndex - cellValue in self.cellOccupied:
                        #self.boardLayout[index] = 0
                        continue
                    if reverseIndex in self.cellOccupied:
                        #self.boardLayout[index] = 0
                        continue
                    self.cellOccupied[reverseIndex] = 1
                    self.cellOccupied[reverseIndex - cellValue] = 1
                    # Add a negative number such that its easy to subtract
                    self.boardLayout[reverseIndex] = cellValue * (-1)

    def movePlayer(self, currentPosition, diceRoll):
        # if user is at boundary and currentPosition + dice
        #exeeds board layout, stick to same position
        if currentPosition + diceRoll < self.boardSize:
            newPosition = currentPosition + diceRoll
            if self.boardLayout[newPosition] > 0:
                print("Great Luck!! Got a ladder. Jump %s steps ahead." % self.boardLayout[newPosition])
                time.sleep(2)
            elif self.boardLayout[newPosition] < 0:
                print("Bad luck!! Encountered a Snake. Go back %s steps" % (-1 * self.boardLayout[newPosition]))
                time.sleep(2)
            newPosition += self.boardLayout[newPosition]
            return newPosition
        elif currentPosition + diceRoll == self.boardSize:
            newPosition = currentPosition + diceRoll
            return newPosition
        else:
            return currentPosition

class Player(object):
    def __init__(self):
        self.pos = 0

def gameLogic(playerObj, gameObj, playerName):
    print("Player %s rolling the dice" % playerName)
    time.sleep(1)
    rollDice = random.choice([1,2,3,4,5,6])
    print("Dice Number=%s" % rollDice)
    time.sleep(1)
    playerObj.pos = gameObj.movePlayer(playerObj.pos, rollDice)
    if rollDice == 6:
        print("Awesome!! 6 .. One more chance to roll the dice")
        time.sleep(1)
        gameLogic(playerObj, gameObj, playerName)
    return  playerObj.pos

def main(boardSize):
    ludogame=LudoBoard(boardSize)
    p1= Player()
    p2= Player()
    print("Starting the game")
    while p1.pos != boardSize and p1.pos != boardSize:
        position = gameLogic(p1, ludogame, "P1")
        print("Player1 position = %s" % position)
        print("---------------------------------------")
        if p1.pos == boardSize:
            print("P1 winner")
            break
        time.sleep(1)
        position = gameLogic(p2, ludogame, "P2")
        print("Player2 position = %s" % position)
        print("---------------------------------------")

        if p2.pos == boardSize :
           print("P2 winner")
           break

if __name__ == "__main__":
    boardSize = 100
    main(boardSize)
