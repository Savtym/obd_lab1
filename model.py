# modelController

import pickle
from bus import Bus
from route import Route

fileName = 'model.pickle'

class ModelController:
	def __init__(self):
		self.buses = []
		self.routes = []
		print "create model"
		
	def serilizationModel(self):
		with open (fileName, 'wb') as f:
			pickle.dump(self.buses, f)

	def deserializeModel(self):
		with open (fileName, 'rb') as f:
			self.buses = pickle.load(f)

	def addBus(self, bus):
		if isinstance(bus, Bus):
			result = True
			for busCur in self.buses:
				if busCur.id == bus.id:
					result = False
					break
			if result:
				self.buses.append(bus)
			else:
				print "this bus exist"

	def removeBus(self, bus):
		self.buses.remove(bus)

	def addRoute(self, route):
		result = True;
		for routeCur in self.routes:
			if routeCur.name == route.name:
				result = False
				break
		if result:
			self.routes.append(route)
			print "create Route"
		else:
			print "not create Route, because exist it`s name"