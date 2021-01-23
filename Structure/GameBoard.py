import networkx as nx
from Structure.Nodes import *


class GameBoard:
	def __add_node(self, cities: dict, node_id: str):
		"""Add a node to the map, deciding whether to add a city or normal node should be added
		:param cities: Cities Dictionary
		:param node_id: ID of node to add
		:return: None
		"""
		node = None
		if node_id in cities.keys():
			node = City(node_id, cities.get(node_id))
			self.cities[node_id] = node
			self.map.add_node(node)
		else:
			node = Node(node_id)
			self.map.add_node(node)
		self.nodes[node_id] = node

	def __add_edge(self, double_tracks: dict, start: Node, end: Node):
		if start.get_id() in double_tracks.keys() and end.get_id() in double_tracks.get(start.get_id()):
			edge = (start, end, {'weight': 2})
			self.map.add_edges_from([edge])
		else:
			edge = (start, end, {'weight': 1})
			self.map.add_edges_from([edge])

	@staticmethod
	def map_cities(city_list: str) -> dict:
		""" turn cities list into a dictionary
		:param city_list: List of cities in form of a string from config file
		:return: a dictionary of all cities where: node_id -> name
		"""
		city_dict = {}
		city_list = city_list.splitlines()
		for city in city_list:
			city_data = city.split(',')
			city_dict[city_data[0]] = city_data[1]
		return city_dict

	@staticmethod
	def map_double_tracks(track_list: []) -> dict:
		track_dict = {}
		for track in track_list:
			track = track.split(',')
			if track_dict.keys().__contains__(track[0]):
				track_dict[track[0]].append(track[1])
			else:
				track_dict[track[0]] = [track[1]]
		return track_dict

	def __generate_map(self, filepath: str):
		"""Generate a game map from a config file
		:param filepath: File path of the map config file
		:return: none
		"""
		ret = nx.Graph()
		# Read map file
		map_file = open(filepath)
		# "#" splits config sections
		map_data = map_file.read().split('#')
		# ":\n" denotes end of config title
		rows = map_data[1].split(':\n')[1].splitlines()
		cities = self.map_cities(map_data[2].split(':\n')[1])
		double_tracks = self.map_double_tracks(map_data[3].split(':\n')[1].splitlines())
		# build map nodes and edges
		for i in range(0, len(rows)):
			# Add initial node for each row at starting position
			row_data = rows[i].split(',')
			start_val = int(row_data[0])
			row_len = int(row_data[1])
			prev_node_id = "0000"
			for j in range(0, row_len):
				node_id = str(start_val + (2 * j)).rjust(2, '0') + str(i).rjust(2, '0')
				self.__add_node(cities, node_id)
				if j != 0:  # no horizontal edge needed for first node in row
					self.__add_edge(double_tracks, self.nodes[node_id], self.nodes[prev_node_id])
				if i != 0:  # no intermediate edges needed for first row
					top_left = str((start_val - 1) + (2 * j)).rjust(2, '0') + str(i - 1).rjust(2, '0')
					top_right = str((start_val + 1) + (2 * j)).rjust(2, '0') + str(i - 1).rjust(2, '0')
					if top_left in self.nodes.keys():
						self.__add_edge(double_tracks, self.nodes.get(node_id), self.nodes.get(top_left))
					if top_right in self.nodes.keys():
						self.__add_edge(double_tracks, self.nodes.get(node_id), self.nodes.get(top_right))
				prev_node_id = node_id

	def __init__(self, players: [], map_filepath: str):
		self.players = players
		self.cities = {}
		self.nodes = {}
		self.map = nx.Graph()
		self.__generate_map(map_filepath)


gb = GameBoard([], "Structure/Maps/classic.txt")
print("Complete")
