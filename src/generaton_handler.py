from sys import exit


if __name__ == "__main__":
	exit()


from field import Field


class GenerationHandler(object):
	def __init__(self, field: Field):
		self.field = field

	def nextGeneration(self) -> ():
		pass

	def addBunnys(self, amt: int) -> ():
		pass

	def addWolf(self, amt: int) -> ():
		pass

	def __str__(self) -> str:
		return f"Field amount: 1"
