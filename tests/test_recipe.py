from lib.recipe import Recipe


# test recipe construction
# should initialise with `recipe_name`, `cooking_time`, `rating`
def test_recipe_creation():
    recipe = Recipe("Chicken Soup", 30, 4)
    assert recipe.recipe_name == "Chicken Soup"
    assert recipe.cooking_time == 30
    assert recipe.rating == 4
