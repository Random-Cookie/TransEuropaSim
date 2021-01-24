import enum


class Colour(enum.Enum):
	blue = 0,
	red = 1,
	orange = 2,
	yellow = 3,
	green = 4


class Node:
	def __init__(self, node_id: str):
		self.__id = node_id

	def get_id(self) -> str:
		return self.__id


class City(Node):
	def __init__(self, node_id: str, name: str, colour: Colour):
		Node.__init__(self, node_id)
		self.name = name
		self.colour = colour

	def get_name(self) -> str:
		return self.name

	def get_colour(self) -> Colour:
		return self.colour
