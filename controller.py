import flask #import login modules from flask
#look for flask skeleton
#import django
import model
import view



class Controller:
	def __init__(self):
		self.model = model.Model()
		self.view = view.View()

	def next_method(self):
		pass
