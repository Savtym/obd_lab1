# app Delegate

from model import ModelController
from view import ViewController 

class AppDelegate:
	def __init__(self):
		self.model = ModelController()
		self.view = ViewController(self.model)

	def __dealloc__(self):
		del self.view
		self.model.deserializeModel()
		del self.model
		print "application is finished"

app = AppDelegate()
for i in xrange(10):
	app.view.createBus('bus #%x' % i, 'mark-%o' % i, 'type')
app.view.listOfBus()
for i in xrange(6):
	app.view.createRoute('route #%x' % i, 'odesa', 'kyiv')
for i in xrange(6):
	app.model.buses[i].addRoute(app.model.routes[i])
app.view.listOfBus()

app.model.buses[2].name = "BUSSSSS"
app.model.routes[2].name = 2
app.model.routes[2].to = 'Dnipro'

print app.model.routes[2]

app.view.search('kyiv')

app.model.serilizationModel()

app.model.buses = []

app.view.listOfBus()

app1 = AppDelegate()

app1.model.deserializeModel()

app1.view.listOfBus()