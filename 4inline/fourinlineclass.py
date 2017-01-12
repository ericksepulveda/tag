class FourInLine:
  def __init__(self):
    self._board = [[0 for i in range(8)] for i in range(8)]
    self._turn = 1
    self._state = 0

  def getBoard(self):
    return self._board

  def getTurn(self):
    return self._turn

  def getState(self):
    return self._state

  def restart(self):
    self = FourInLine()

  def dropChip(self, col):
    rowIndex = 0
    for row in self._board:
      if row[col] == 0:
        row[col] = self._turn
        break
      rowIndex += 1
    return (col, rowIndex)

  def check4Horizontal(self, x,y):
    counter = 0
    for h in range(1,4):
      if x-h > 0 and self._board[y][x-h] == 1:
        counter += 1
      else:
        break
    for h in range(1,4):
      if x+h < 8 and self._board[y][x+h] == 1:
        counter += 1
      else:
        break
    if counter == 3:
      self._state = 1
      return True
    else:
      return False


