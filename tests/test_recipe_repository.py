from lib.recipe_repository import *
import pytest


# test find all recipes in repository
def test_list_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)

    recipes = repo.all()

    assert recipes[0].recipe_name == "Spaghetti Carbonara"
    assert recipes[0].cooking_time == 30
    assert recipes[0].rating == 4

    assert recipes[1].recipe_name == "Chicken Kiev"
    assert recipes[1].cooking_time == 45
    assert recipes[1].rating == 5


# test find() returns the correct recipe by searching name
def test_find_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)
    recipe = repo.find("Spaghetti Carbonara")
    assert recipe.recipe_name == "Spaghetti Carbonara"
    recipe2 = repo.find("Chicken Kiev")
    assert recipe2.recipe_name == "Chicken Kiev"


# Test for non-existing recipe
def test_exception_raised_when_recipe_does_not_exist(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repo = RecipeRepository(db_connection)
    with pytest.raises(ValueError) as err:
        repo.find("Non-Existent Recipe")
    assert "does not exist" in str(err.value)
