from recipe import Recipe
from book import Book

if __name__ == "__main__":
	recipe1 = Recipe('test', 2, 20, ['qhoj'], '', 'starter')
	print(recipe)
	book = Book('Mon livre')
	book.add_recipe(recipe1)
	print(book) 
