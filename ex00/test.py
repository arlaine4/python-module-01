from recipe import Recipe
from book import Book
import time

if __name__ == "__main__":
    book = Book('livre 1')
    # recipe_bad = Recipe('', -2, 0, [], 15, 'bonsoir')
    recipe_frite = Recipe('frites', 1, 15, ['huile', 'patates'], 'des bonnes frites maison', 'lunch')
    time.sleep(1)
    book.add_recipe(recipe_frite)
    recipe_gateau = Recipe('gateau', 2, 60, ['oeuf', 'lait', 'farine', 'levure'], 'un bon gateau', 'dessert')
    time.sleep(1)
    book.add_recipe(recipe_gateau)
    print(book)
