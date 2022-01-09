from datetime import datetime


class Book:
    def __init__(self, name):
        self.errors = []
        self.new_book = True
        self.set_name(name)
        self.set_last_update()
        self.set_creation_date()
        self.recipes_list = {'starter': [],
                             'lunch': [],
                             'dessert': []}

    def set_name(self, name):
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
        if not self.new_book:
            self.set_last_update()

    def get_format_recipe(self, key):
        recipe_txt = ''
        for recipe in self.recipes_list[key]:
            recipe_txt += f'\n{recipe.__str__()}'
        return recipe_txt
	
    def get_recipe_by_types(self, recipe_type):
        print(self.get_format_recipe(recipe_type))

    def get_type_for_recipe_name(self, name):
        types = ['starter', 'lunch', 'dessert']
        for recipe_type in types:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    return recipe_type, recipe
        return None, None

    def get_recipe_by_name(self, name):
        in_, recipe = self.get_type_for_recipe_name(name)
        if not in_:
            print(f"{name} not in recipe list.")
        else:
            print(recipe.__str__())
        """elif name in self.recipes_list['starter']:
           print(self.recipes_list['starter'][name].__str__())
        elif name in self.recipes_list['lunch']:
           print(self.recipes_list['lunch'][name].__str__())
        else:
           print(self.recipes_list['dessert'][name].__str__())"""

    def	__str__(self):
        format_dessert = None
        format_starter = None
        format_lunch = None
        txt = f'\n\n{self.name}\n\ncreation_date : {self.creation_date}\n' \
              f'last_update : {self.last_update}\n' \
              f"- starter recipes : {self.get_format_recipe('starter')}\n" \
              f"- lunch recipes : {self.get_format_recipe('lunch')}\n" \
              f"- dessert recipes : {self.get_format_recipe('dessert')}\n"
        return txt
        """if not self.recipes_list['starter']:
            format_starter = None
        if self.recipes_list['starter']:
            # Do the get_format_recipe inside recipe class in order to return __str__ into a string
            format_starter = [recipe.get_format_recipe for recipe in self.recipes_list['starter']]
        elif not self.recipes_list['lunch']:
            format_lunch = None
        elif self.recipes_list['lunch']:
            format_lunch = None
        elif not self.recipes_list['dessert']:
            format_dessert = None
        elif self.recipes_list['dessert']:
            format_dessert = None
        return f"{self.name}\n\ncreation_date : {self.creation_date}\nlast_update: {self.last_update}\nstarters : {format_starter}\nlunch : {format_lunch}\ndessert : {format_dessert}"""

