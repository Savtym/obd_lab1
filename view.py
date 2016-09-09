#viewController

import weakref
from model import ModelController
from bus import Bus
from route import Route

kyiv = "kyiv"

class ViewController:
	def __init__(self, model):
		self.model = model
		print "use commands for the app:\n\tcreate bus: createBus(name, mark, type)\n\tcreate route: Route(name, from, to)\n\tserilization model: serilizationModel()\n\tdeserialize model: deserializeModel()\n\tadd a route to the bus: addRoute(route)\n\tremove a route to the bus: removeRoute()\n\tremove bus: removeBus(bus)\n\tsearch route name: search(value)\n"

	def createBus(self, name, mark, type):
		bus = Bus(name, mark, type)
		self.model.addBus(bus)
		print "bus created"
		return bus

	def createRoute(self, name, fromR ,to):
		route = Route(name, fromR, to)
		self.model.addRoute(route)
		print "route created"
		return route

	def removeBus(self, bus):
		self.model.removeBus(bus)
		print "bus removed"

	def serilizationModel(self):
		self.model.serilizationModel()
		print "serilizated model"

	def deserializeModel(self):
		self.model.deserializeModel()
		print "deserialized model"

	def search(self, value):
		buses = []
		for bus in self.model.buses:
			if bus.route == value:
				buses.append(bus)
		if len(buses) == 0:
			print "Result: not found"
		else:
			print "Result: %s" % buses

	def listOfBus(self):
		print "List of Buses:"
		for bus in self.model.buses:
			print bus
		print "End"

# model = ModelController()
# view = ViewController(model)
# bus = view.createBus('bus','mark', 'type')
# route = view.createRoute('kyiv', 'odessa', 'kyiv');
# bus.addRoute(route)
# view.search(kyiv)
# print bus
# print route
# bus.name = "bus1"
# view.model.removeBus(bus)
# view.listOfBus()