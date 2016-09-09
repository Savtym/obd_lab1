# bus

import uuid
from route import Route

class Bus:
	def __init__(self, name, mark, type):
		self.id = uuid.uuid1()
		self.name = name
		self.mark = mark
		self.type = type
		self.__route = None

	def __dealloc__(self):
		if self.__route is not None:
			del self.__route
		print "Bus is removed"	

	def __repr__(self):
		result = "Bus name: %s; mark: %s; type: %s;" % (self.name, self.mark, self.type)
		if self.__route is not None:
			result += " %s;" % self.__route
		return result

	def addRoute(self, route):
		if isinstance(route, Route):
			self.__route = route
			print "Route add"
		else:
			print "Route not added"

	def removeRoute(self):
		if self.__route is not None:
			self.__route = 0
			print "Route remove"
		else:
			print "Route not remove, because bus not have a route"

	@property
	def route(self):
		result = "This bus not have a route"
		if self.__route is not None:
			result = "%s" % self.__route.to
		return result