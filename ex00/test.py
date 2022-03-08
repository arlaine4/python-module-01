from recipe import Recipe
from book import Book
import time

if __name__ == "__main__":
    # ------------ Error test ----------- #
    # e_recipe = Recipe()
    # e_recipe = Recipe(1, '1', '0', (), 1)
    # book = Book()
    # book = Book(1)
    # ----------------------------------- #

    # ------------ Valid test ----------- #
    book = Book('Mon livre')
    recipe_1 = Recipe('frites', 1, 15, ['huile', 'patates'], 'des bonnes frites maison', 'lunch')
    recipe_2 = Recipe('omelette', 1, 5, ['oeufs'], 'une omelette', 'lunch')
    time.sleep(1)
    book.add_recipe(recipe_1)
    book.add_recipe(recipe_2)
    print(book.get_recipe_by_types('dessert'))
    """book = Book('Mon livre')
    print(book)
    recipe_1 = Recipe('frites', 1, 15, ['huile', 'patates'], 'des bonnes frites maison', 'lunch')
    # time.sleep(2)
    book.add_recipe(recipe_1)
    # print(book)
    recipe_2 = Recipe('gateau', 3, 60, ['farine', 'oeufs', 'levure', 'lait'], 'un bon gateau', 'dessert')
    # time.sleep(2)
    book.add_recipe(recipe_2)
    # print(book)
    # ---------------------------------- #"""
