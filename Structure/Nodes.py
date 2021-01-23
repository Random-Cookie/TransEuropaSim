class Node:
	def __init__(self, node_id: str):
		self.id = node_id


class City(Node):
	def __init__(self, node_id: str, name: str):
		Node.__init__(self, node_id)
		self.name = name
