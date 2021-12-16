from sys import exit, stdout
import JSON


def fileGrep(inpt_file: str, quick: bool) -> dict[str, (str|int|dict)]:
	"""
	Will take infromation from a JSON file, to be used in the simulation, if\n
	quick is TRUE the program will look in bin. This is to make the file name\n
	quicker to type.\n
	@param inpt_file: 	str\n
	@param quick: 		bool\n
	@return: 			dict[str, (str|int|dict)]
	"""
	if (quick):
		pass
	pass


def strInpt(inpt: str) -> dict[str, (str|int|dict)]:
	"""
	If the usere wishes to write the creature specifications in the CLI, this\n
	will be the function used to parse it.\n
	@param inpt: 	str\n
	@return: 		dict[str, (str|int|dict)]
	"""
	pass


def main():
	pass


if __name__ == "__main__":
	main()
	exit()