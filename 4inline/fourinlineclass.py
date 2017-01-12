class FourInLine:
	def __init__(self):
		self._board = [[0 for i in range(8)] for i in range(8)]
		self._board[1][1] = 2
		self._turn = 1
		self._state = 0

	def getBoard(self):
		return self._board

	def getTurn(self):
		return self._turn

	def getState(self):
		return self._state
