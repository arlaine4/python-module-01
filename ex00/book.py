import sys
from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name=''):
        self.errors = []
        self.new_book = True
        self.name = name
        self.creation_date = None
        self.last_update = None
        self.set_name(name)
        self.set_last_update()
        self.set_creation_date()
        self.recipes_list = {'starter': [],
                             'lunch': [],
                             'dessert': []}
        self.verif_valid_params()

    def verif_valid_params(self):
        if len(self.errors) != 0:
            for i, error in enumerate(self.errors):
                print(f"{i} : {error}")

    def set_name(self, name):
        if not name:
            self.errors.append('Missing name for recipe book')
            return
        elif type(name) is not str:
            self.errors.append('Wrong type for book name')
            return
        self.name = name

    def set_last_update(self):
        now = datetime.now()
        self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")

    def set_creation_date(self):
        self.new_book = False
        now = datetime.now()
        self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")

    def add_recipe(self, recipe):
        if type(recipe) is Recipe:
            self.recipes_list[recipe.recipe_type].append(recipe)
            if not self.new_book:
                self.set_last_update()
        else:
            print(f'Invalid "{recipe}" for new recipe')
            sys.exit()

    def get_format_recipe(self, key):
        recipe_txt = ''
        for recipe in self.recipes_list[key]:
            recipe_txt += f'\n{recipe.__str__()}'
        return recipe_txt

    def get_recipe_by_types(self, recipe_type):
        if type(recipe_type) is str and recipe_type in self.recipes_list.keys():
            return self.get_format_recipe(recipe_type)
        else:
            print(f'\nInvalid recipe_type {recipe_type}\n\n')

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
            return recipe

    def	__str__(self):
        txt = f'\n\n{self.name}\n\ncreation_date : {self.creation_date}\n' \
              f'last_update : {self.last_update}\n' \
              f"- starter recipes : {self.get_format_recipe('starter')}\n\n" \
              f"- lunch recipes : {self.get_format_recipe('lunch')}\n\n" \
              f"- dessert recipes : {self.get_format_recipe('dessert')}\n\n"
        return txt

