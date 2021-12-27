from datetime import datetime


class Book:
	def __init__(self, name):
		self.errors = []
		self.new_book = True
		self.set_name(name)
		self.set_last_update()
		self.set_creation_date()
		self.recipes_list = {'starter': [],
							 'lunch' : [],
							 'dessert': []}

	def	set_name(self, name):
		if not name:
			self.errors.append('Missing name for recipe book')
			return
		elif type(name) is not str:
			self.errors.append('Wrong type for book name')
			return
		self.name = name

	def set_last_update(self):
		if not self.new_book:
			now = datetime.now()
			self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")
		else:
			self.last_update = '-'

	def	set_creation_date(self):
		self.new_book = False
		now = datetime.now()
		self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")

	def add_recipe(self, recipe):
		self.recipes_list[recipe.recipe_type].append(recipe)

	def	__str__(self):
		if not self.recipes_list['starter']:
			format_starter = None
		elif self.recipes_list['starter']:
			# Do the get_format_recipe inside recipe class in order to return __str__ into a string
			format_starter = [recipe.get_format_recipe for recipe self.recipes_list['starter']]
		elif not self.recipes_list['lunch']:
			format_lunch = None
		elif self.recipes_list['lunch']:
			format_lunch = None
		elif not self.recipes_list['dessert']:
			format_dessert = None
		elif self.recipes_list['dessert']:
			format_dessert = None
		return f"{self.name}\n\ncreation_date : {self.creation_date}\nlast_update: {self.last_update}\nstarters : {format_starter}\nlunch : {format_lunch}\ndessert : {format_dessert}"
