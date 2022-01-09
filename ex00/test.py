from recipe import Recipe
from book import Book
import time

if __name__ == "__main__":
	recipe1 = Recipe('NULL VALUE', 2, 20, ['qhoj'], '', 'lunch')
	#print(recipe1)
	book = Book('Mon livre')
	book.add_recipe(recipe1)
	recipe2 = Recipe("Cake", 2, 15, ['farine', 'ble'], '', 'dessert')
	recipe3 = Recipe("Elliot", 5, 60, ['Valo', 'Fortnite', 'Dofus', 'un peu de salt'], 'enorme pd', 'dessert')
	time.sleep(1)
	book.add_recipe(recipe2)
	book.add_recipe(recipe3)
	book.get_recipe_by_types('dessert')
	#time.sleep(3)
	#print(book)
	#book.get_recipe_by_name('bonsoir')
