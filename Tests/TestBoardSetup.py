import Structure.GameBoard as gb
import psychopy.visual
from Graphics.DrawLib import BasicNetworkDrawer

test_board = gb.GameBoard([], "Structure/Maps/classic.txt")
drawer = BasicNetworkDrawer(test_board.get_map(), test_board._cities)
win = psychopy.visual.Window(
	size=[1280, 720],
	units="pix",
	fullscr=False,
	color=[0.9, 0.9, 0.9]
)

drawer.draw_edges(win)
drawer.draw_nodes(win)
drawer.draw_cities(win)
win.flip()

while 'escape' not in psychopy.event.waitKeys():

	drawer.draw_edges(win)
	drawer.draw_nodes(win)
	drawer.draw_cities(win)

	win.flip()

win.close()
