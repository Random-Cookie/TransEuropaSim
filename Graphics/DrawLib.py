import networkx as nx
import psychopy.visual
import psychopy.event
from Structure.Nodes import *


class NetworkToPoints:
	@staticmethod
	def get_node_points(network: nx.Graph) -> []:
		points = []
		for node in network.nodes:
			nid = node.get_id()
			x = int(nid[0:2])
			y = int(nid[2:4])
			points.append([x, y])
		return points

	@staticmethod
	def get_city_points_dep(cities: dict) -> [[], [], [], [], []]:
		points = [[], [], [], [], []]
		for city in cities.values():
			cid = city.get_id()
			x = int(cid[0:2])
			y = int(cid[2:4])
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
		return points

	@staticmethod
	def get_city_points(network: nx.Graph) -> [[], [], [], [], []]:
		points = [[], [], [], [], []]
		for node in network.nodes:
			if isinstance(node, City):
				cid = node.get_id()
				x = int(cid[0:2])
				y = int(cid[2:4])
				if node.get_colour() == Colour.blue:
					points[0].append([x, y])
				elif node.get_colour() == Colour.red:
					points[1].append([x, y])
				elif node.get_colour() == Colour.orange:
					points[2].append([x, y])
				elif node.get_colour() == Colour.yellow:
					points[3].append([x, y])
				else:
					points[4].append([x, y])
		return points

	@staticmethod
	def get_edge_lines(network: nx.Graph) -> []:
		points = []
		for edge in network.edges.data():
			start = edge[0].get_id()
			end = edge[1].get_id()
			weight = int(edge[2].get('weight'))
			start_point = [int(start[0:2]), int(start[2:4])]
			end_point = [int(end[0:2]), int(end[2:4])]
			points.append((start_point, end_point, weight))
		return points


class BasicNetworkDrawer:
	def __init__(self, network: nx.Graph, cities: dict):
		self.network = network
		self.cities = cities
		self.X_MUL = 22
		self.X_OFF = -400
		self.Y_MUL = -40
		self.Y_OFF = 240

	def draw_nodes(self, win: psychopy.visual.Window):
		points = NetworkToPoints.get_node_points(self.network)
		for point in points:
			point[0] *= self.X_MUL
			point[0] += self.X_OFF
			point[1] *= self.Y_MUL
			point[1] += self.Y_OFF

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
		points = NetworkToPoints.get_city_points(self.network)
		for group in points:
			for point in group:
				point[0] *= self.X_MUL
				point[0] += self.X_OFF
				point[1] *= self.Y_MUL
				point[1] += self.Y_OFF
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

	def draw_edges(self, win: psychopy.visual.Window):
		lines = NetworkToPoints.get_edge_lines(self.network)
		for line in lines:
			l = psychopy.visual.Line(
				win=win,
				units="pix",
				lineColor=[-1, -1, -1]
			)
			if line[2] == 2:
				l.lineWidth = 4
			l.start = [(line[0][0] * self.X_MUL) + self.X_OFF, (line[0][1] * self.Y_MUL) + self.Y_OFF]
			l.end = [(line[1][0] * self.X_MUL) + self.X_OFF, (line[1][1] * self.Y_MUL) + self.Y_OFF]
			l.draw()
