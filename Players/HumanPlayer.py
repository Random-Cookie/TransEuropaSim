from Players.Player import Player
from networkx import Graph

from Structure.GameBoard import GameBoard


class HumanPlayer(Player):
	def __init__(self, name):
		Player.__init__(self, name)

	def choose_start_pos(self, game_board: GameBoard) -> str:
		coord = ""
		while len(coord) != 4 and (not coord.isnumeric()):
			coord = input("Input co-ordinates of starting position:")
		return coord

	def make_move(self, game_board: GameBoard) -> [str, str]:  # node to add to network should always be first
		coords = []
		coord = ""
		while len(coord) != 4 and (not coord.isnumeric()):
			coord = input("Input co-ordinates of first node to connect:")
		coords.append(coord)
		coord = ""
		while len(coord) != 4 and (not coord.isnumeric()):
			coord = input("Input co-ordinates of second node to connect:")
		coords.append(coord)
		return coords
