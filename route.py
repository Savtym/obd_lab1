# route

import uuid
# import weakref
# from bus import Bus

class Route:
	def __init__(self, name, fromR, to):
		self.name = name
		self.fromR = fromR
		self.to = to

	def __dealloc__(self):
		print "route %s remove" % self.name

	# def addBus(self, bus):
	# 	if isinstance(bus, Bus):
	# 		self.bus = weakref.ref(bus)
	# 		print "Bus added with route"

	# def removeBus(self):
	# 	if getattr(self, 'bus'):
	# 		del self.bus
	# 		print "Bus remove from route"

	def bus(self):
		if getattr(self, 'bus'):
			print self.bus.name
		else:
			print "Route not have bus"

	def __repr__(self):
		return "Route %s: from %s to %s" % (self.name, self.fromR, self.to)