from lib.recipe import Recipe


class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            item = Recipe(row["recipe_name"], row["cooking_time"], row["rating"])
            recipes.append(item)
        return recipes

    def find(self, recipe_name):
        rows = self._connection.execute(
            "SELECT * from recipes WHERE recipe_name = %s", [recipe_name]
        )
        # Throw an error if the recipe does not exist
        if not rows:
            raise ValueError(f"Recipe with name '{recipe_name}' does not exist.")

        row = rows[0]
        return Recipe(row["recipe_name"], row["cooking_time"], row["rating"])
