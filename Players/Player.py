from networkx import Graph
from abc import abstractmethod
from Graphics.DrawLib import NetworkToPoints

from Structure.Nodes import *
from Structure.GameBoard import GameBoard


class Player:
	def __init__(self, name):
		self.name = name
		self.__network = Graph()

	def get_network(self):
		return self.__network

	def print_nodes_in_network(self):
		points = NetworkToPoints.get_node_points(self.__network)
		for point in points:
			print("Node: " + str(point[0]).rjust(2, "0") + "," + str(point[1]).rjust(2, "0"))

	def print_cities_in_network(self, game_board: GameBoard):
		groups = NetworkToPoints.get_city_points(self.__network)
		for group in groups:
			if group:
				for point in group:
					city = game_board.get_cities().get(str(point[0]).rjust(2, "0") + str(point[1]).rjust(2, "0"))
					print(city.get_name() + ": " + str(point[0]).rjust(2, "0") + "," + str(point[1]).rjust(2, "0"))

	def print_edges_in_network(self):
		lines = NetworkToPoints.get_edge_lines(self.__network)
		for line in lines:
			print("Edge: " + str(line[0][0]).rjust(2, "0") + "," + str(line[0][1]).rjust(2, "0")
			      + str(line[1][0]).rjust(2, "0") + "," + str(line[1][1]).rjust(2, "0"))

	def add_start_node(self, game_board: GameBoard, chosen_node: str):
		self.__network.add_node(game_board.get_nodes().get(chosen_node))

	def add_node_to_network(self, game_board: GameBoard, chosen_node: [str, str]):
		self.__network.add_node(game_board.get_nodes().get(chosen_node[0]))
		edge = game_board.get_edges().get(chosen_node[0] + chosen_node[1])
		if edge is None:
			edge = game_board.get_edges().get(chosen_node[1] + chosen_node[0])
		try:
			self.__network.add_edge(edge[0], edge[1], weight=edge[2])
		except TypeError:
			print("Well done.....")

	@abstractmethod
	def choose_start_pos(self, game_board: GameBoard) -> str:
		print(self.name + " chose their starting position")
		return "0000"

	@abstractmethod
	def make_move(self, game_board: GameBoard) -> [str]: # node to add to network should always be first
		print(self.name + " took a turn")
		return ["0000", "0000"]
