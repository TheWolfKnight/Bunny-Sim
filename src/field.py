from sys import exit


if __name__ == "__main__":
	exit()


from enum import Enum, auto
from bunny import Bunny
from wolf import Wolf


class Wether(Enum):
	pass


class Fiel(object):
	"""
	A field contains a population of bunnys and of wolfs, with a wether. It will then be used
	to handle the accessing of the local elements, and will tell the generation handler when
	there are no more bunnys and/or wolfs.
	"""
	def __init__(self, amt_bunny: int, amt_wolf: int, wether: Wether,
				 bunny_specifics: dict[str, (str|int|dict)]=None, wolf_specifics: dict[str, (str|int|dict)]=None):
		self.amt_bunny = amt_bunny
		self.bunny_specifics = bunny_specifics

		self.amt_wolf = amt_wolf
		self.wolf_specifics = wolf_specifics

		self.wether = wether

		self.current_bunny_pop: list[Bunny] = _generateBunnyPop()
		self.current_wolf_pop: list[Wolf] = _generateWolfPop()

	def _generateWolfPop(self) -> list[Wolf]:
		pass

	def _generateBunnyPop(self) -> list[Wolf]:
		pass

	def killBunny(self, amt: int) -> bool:
		assert isinstance(amt, int), "The variabel \"amt\" in killBunny must be an integer!"
		self.bunny -= amt
		if (self.bunny < 1):
			return False
		return True

	def addBunnys(self, amt: int) -> ():
		pass

	def addWolf(self, amt: int) -> ():
		pass

	def __str__(self) -> str:
		return f"Amount of bunnys: {self.amt_bunny}\nAmount of wolfs: {self.amt_wolf}\nWether: {self.wether}"
