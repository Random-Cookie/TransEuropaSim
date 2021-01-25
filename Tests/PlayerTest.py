import Structure.GameBoard as gb
from Players.HumanPlayer import HumanPlayer

test_player = HumanPlayer("Joe")

test_board = gb.GameBoard([test_player], "Structure/Maps/classic.txt")

moves = 0
MAX_MOVES = 10

chosen_node = test_player.choose_start_pos(test_board)
test_player.add_start_node(test_board, chosen_node)

while moves < MAX_MOVES:
	moves += 1
	for player in test_board.get_players():
		chosen_node = player.make_move(test_board)
		test_player.add_node_to_network(test_board, chosen_node)

		print("----------")
		player.print_nodes_in_network()
		print("----------")
		player.print_cities_in_network(test_board)
		print("----------")
		player.print_edges_in_network()
