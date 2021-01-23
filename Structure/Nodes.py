class Node:
	def __init__(self, node_id: str):
		self.__id = node_id

	def get_id(self) -> str:
		return self.__id



class City(Node):
	def __init__(self, node_id: str, name: str):
		Node.__init__(self, node_id)
		self.name = name

	def get_name(self) -> str:
		return self.name
