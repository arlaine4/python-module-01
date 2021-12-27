import sys


class Recipe:
	def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
				 ingredients=None, description=None, recipe_type=None):
		self.errors = []
		self.set_name(name)
		self.set_cooking_lvl(cooking_lvl)
		self.set_cooking_time(cooking_time)
		self.set_ingredients(ingredients)
		self.description = description if type(description) is str else ''
		self.set_recipe_type(recipe_type)
		self.verif_valid_params()

	def	verif_valid_params(self):
		if len(self.errors) != 0:
			for i, error in enumerate(self.errors):
				print(f"{i} : {error}")
			sys.exit("\nInvalid recipe, stopping now")

	def check_valid_ingredients(self, ingredients):
		valid = map(lambda x: True if (type(x) is str and len(x) > 2) else False, ingredients)
		if False in valid:
			return False
		return True

	def set_name(self, name):
		if not name:
			self.errors.append('Missing name for recipe')
			return
		elif type(name) is not str:
			self.errors.append('Wrong type for recipe name')
			return
		self.name = name

	def	set_cooking_lvl(self, cooking_lvl):
		if not cooking_lvl:
			self.errors.append('Missing cooking level for recipe')
			return
		elif type(cooking_lvl) not in [int, float]:
			self.errors.append('Wrong type for recipe cooking_lvl')
			return
		self.cooking_lvl = cooking_lvl

	def set_cooking_time(self, cooking_time):
		if not cooking_time:
			self.errors.append('Missing cooking time for recipe')
			return
		elif type(cooking_time) not in [int, float]:
			self.errors.append('Wrong type for recipe cooking_time')
			return
		self.cooking_time = cooking_time

	def	set_ingredients(self, ingredients):
		if not ingredients:
			self.errors.append('Missing ingredients for recipe')
			return
		elif not self.check_valid_ingredients(ingredients):
			self.errors.append('Wrong type for one or more recipe ingredients')
			return
		self.ingredients = ingredients

	def set_recipe_type(self, recipe_type):
		if not recipe_type:
			self.errors.append('Missing recipe type')
			return
		elif type(recipe_type) is not str:
			self.errors.append('Wrong type for recipe type')
			return
		elif recipe_type not in ['starter', 'lunch', 'dessert']:
			self.errors.append('Invalid recipe type')
			return
		self.recipe_type = recipe_type

	def	__str__(self):
		return f"name : {self.name}\ncooking_lvl : {self.cooking_lvl}\ncooking_time: {self.cooking_time}\ningredients : {self.ingredients}\ndescription : {self.description}\nrecipe_type : {self.recipe_type}"
