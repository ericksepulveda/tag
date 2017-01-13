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

  def dropChip(self, player, col):
    rowIndex = 0
    for row in self._board:
      if row[col] == 0:
        row[col] = self._turn
        break
      rowIndex += 1
    return (col, rowIndex)

  def check4Horizontal(self, x, y):
    counter = 0
    player = self._turn
    for h in range(1, 4):
      if x-h >= 0 and self._board[y][x-h] == player:
        counter += 1
      else:
        break
    for h in range(1, 4):
      if x+h < 8 and self._board[y][x+h] == player:
        counter += 1
      else:
        break
    if counter == 3:
      self._state = player
      return True
    else:
      return False

  def check4Vertical(self, x, y):
    counter = 0
    player = self._turn
    for v in range(1, 4):
      if y-v >= 0 and self._board[y-v][x] == player:
        counter += 1
      else:
        break
    for v in range(1, 4):
      if y+v < 8 and self._board[y+v][x] == player:
        counter += 1
      else:
        break
    if counter == 3:
      self._state = player
      return True
    else:
      return False
  def check4DiagonalID(self, x, y): 
    counter  = 0
    player = self._turn
    for d in range(1,4):
      if y-d >=0 and x-d >=0 and self._board[y-d][x-d] == player:
        counter += 1
      else:
        break
    for d in range(1,4):
      if y+d <8 and x+d <8 and self._board[y+d][x+d] == player:
        counter += 1
      else:
        break
    if counter == 3:
      self._state = player
      return True
    else:
      return False

  def check4DiagonalDI(self, x, y): 
    counter  = 0
    player = self._turn
    for d in range(1,4):
      if y+d <8 and x-d >=0 and self._board[y+d][x-d] == player:
        counter += 1
      else:
        break
    for d in range(1,4):
      if y-d >=0 and x+d <8 and self._board[y-d][x+d] == player:
        counter += 1
      else:
        break
    if counter == 3:
      self._state = player
      return True
    else:
      return False


  def otherPlayer(self, player):
    return 2 if player == 1 else 1

  def nextPlayer(self):
    self._turn = self.otherPlayer(self._turn)

  def play(self, col):
    r = self.dropChip(self.getTurn(), col)
    status = self.check4Horizontal(r[0], r[1])
    status = status or self.check4Vertical(r[0], r[1])  
    status = status or self.check4DiagonalID(r[0], r[1])
    status = status or self.check4DiagonalDI(r[0], r[1])
    self.nextPlayer();
    return status
