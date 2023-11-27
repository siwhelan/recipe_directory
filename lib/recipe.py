class Recipe:
    def __init__(self, recipe_name, cooking_time, rating):
        self.recipe_name = recipe_name
        self.cooking_time = cooking_time
        self.rating = rating

    def __repr__(self):
        return f"Recipe: {self.recipe_name}, Cooking Time: {self.cooking_time} mins, Rating: {self.rating}"
