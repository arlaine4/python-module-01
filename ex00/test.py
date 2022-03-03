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
    print(book)
    recipe_1 = Recipe('frites', 1, 15, ['huile', 'patates'], 'des bonnes frites maison', 'lunch')
    # time.sleep(2)
    book.add_recipe(recipe_1)
    # print(book)
    recipe_2 = Recipe('gateau', 3, 60, ['farine', 'oeufs', 'levure', 'lait'], 'un bon gateau', 'dessert')
    # time.sleep(2)
    book.add_recipe(recipe_2)
    # print(book)
    # ---------------------------------- #

    # save_recipe = book.get_recipe_by_name(1)
    save_recipe = book.get_recipe_by_name('frites')

    # book.get_recipe_by_types('t')
    book.get_recipe_by_types('dessert')