class Toque:
	def __init__(self):
		self.number = ["5","1","9","6"]

	def getHint(self):
		return "????"

	def guess(self, attempt):
		response = ['?', '?', '?', '?']
		i = 0
		for char in attempt:
			if self.number[i] == char:
				response[i] = "*"
			elif char in self.number:
				response[i] = '-'
			i += 1
		return "".join(response)

