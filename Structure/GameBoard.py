import networkx as nx
from Structure.Nodes import *


class GameBoard:
	def __add_node(self, cities: dict, node_id: str):
		if cities.keys().__contains__(node_id):
			city = City(node_id, cities.get(node_id))
			self.cities.append(city)
			self.map.add_node(city)
		else:
			self.map.add_node(Node(node_id))

	@staticmethod
	def map_cities(city_list) -> dict:
		city_dict = {}
		city_list = city_list.splitlines()
		for city in city_list:
			city_data = city.split(',')
			city_dict[city_data[0]] = city_data[1]
		return city_dict

	def __generate_map(self, filepath: str):
		ret = nx.Graph()
		# Read map file
		map_file = open(filepath)
		# "#" splits config sections
		map_data = map_file.read().split('#')
		# ":\n" denotes end of config title
		rows = map_data[1].split(':\n')[1].splitlines()
		cities = self.map_cities(map_data[2].split(':\n')[1])

		for i in range(0, len(rows)):
			# print(str(i) + ": " + rows[i])
			# Add initial node for each row at starting position
			row_data = rows[i].split(',')
			start_val = int(row_data[0])
			row_len = int(row_data[1])
			self.__add_node(cities, str(start_val).rjust(2, '0') + str(i).rjust(2, '0'))
			for j in range(1, row_len):
				self.__add_node(cities, str(start_val + (2 * j)).rjust(2, '0') + str(i).rjust(2, '0'))

	def __init__(self, players, map_filepath: str):
		self.players = players
		self.cities = []
		self.map = nx.Graph()
		self.__generate_map(map_filepath)


gb = GameBoard([], "Structure/Maps/classic.txt")
print("Complete")