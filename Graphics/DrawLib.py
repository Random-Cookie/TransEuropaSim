import networkx as nx
import psychopy.visual
import psychopy.event
from Structure.Nodes import Colour


class BasicNetworkDrawer:
	def __init__(self, network: nx.Graph, cities: dict):
		self.network = network
		self.cities = cities

	def draw_nodes(self, win: psychopy.visual.Window):
		points = []
		for node in self.network.nodes:
			nid = node.get_id()
			x = (int(nid[0:2]) * 22) - 400
			y = (int(nid[2:4]) * -40) + 240
			points.append([x, y])

		node_dots = psychopy.visual.ElementArrayStim(
			win=win,
			units="pix",
			nElements=len(self.network.nodes),
			elementTex=None,
			elementMask="circle",
			xys=points,
			sizes=5,
			colors=[-1, -1, -1]
		)
		node_dots.draw()

	def draw_cities(self, win: psychopy.visual.Window):
		points = [[], [], [], [], []]
		for city in self.cities.values():
			cid = city.get_id()
			x = (int(cid[0:2]) * 22) - 400
			y = (int(cid[2:4]) * -40) + 240
			if city.get_colour() == Colour.blue:
				points[0].append([x, y])
			elif city.get_colour() == Colour.red:
				points[1].append([x, y])
			elif city.get_colour() == Colour.orange:
				points[2].append([x, y])
			elif city.get_colour() == Colour.yellow:
				points[3].append([x, y])
			else:
				points[4].append([x, y])

		city_size = 15

		blue_cities = psychopy.visual.ElementArrayStim(
			win=win,
			units="pix",
			nElements=len(points[0]),
			elementTex=None,
			elementMask="circle",
			xys=points[0],
			sizes=city_size,
			colors=[-1, -1, 1]
		)
		red_cities = psychopy.visual.ElementArrayStim(
			win=win,
			units="pix",
			nElements=len(points[1]),
			elementTex=None,
			elementMask="circle",
			xys=points[1],
			sizes=city_size,
			colors=[1, -1, -1]
		)
		orange_cities = psychopy.visual.ElementArrayStim(
			win=win,
			units="pix",
			nElements=len(points[2]),
			elementTex=None,
			elementMask="circle",
			xys=points[2],
			sizes=city_size,
			colors=[1, 0, -1]
		)
		yellow_cities = psychopy.visual.ElementArrayStim(
			win=win,
			units="pix",
			nElements=len(points[3]),
			elementTex=None,
			elementMask="circle",
			xys=points[3],
			sizes=city_size,
			colors=[1, 1, -1]
		)
		green_cities = psychopy.visual.ElementArrayStim(
			win=win,
			units="pix",
			nElements=len(points[4]),
			elementTex=None,
			elementMask="circle",
			xys=points[4],
			sizes=city_size,
			colors=[-1, 1, -1]
		)

		blue_cities.draw()
		red_cities.draw()
		orange_cities.draw()
		yellow_cities.draw()
		green_cities.draw()
