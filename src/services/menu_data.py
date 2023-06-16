import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        df = pd.read_csv(source_path)
        self.dishes = set()

        grouped_dishes = df.groupby(["dish", "price"]).apply(
            lambda df: list(zip(df["ingredient"], df["recipe_amount"]))
        )

        for curr_dish, dish_ingredients in grouped_dishes.items():
            dish_name, dish_price = curr_dish
            dish = Dish(dish_name, dish_price)

            for ingredient in dish_ingredients:
                ingredient_name, ingredient_amount = ingredient
                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), ingredient_amount
                )

            self.dishes.add(dish)
