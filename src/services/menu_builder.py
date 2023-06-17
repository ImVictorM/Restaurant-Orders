import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from collections import defaultdict

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        dish_table = defaultdict(list)

        for dish in self.menu_data.dishes:
            dish_restrictions = dish.get_restrictions()
            dish_ingredients = dish.get_ingredients()
            ingredients_are_available = (
                self.inventory.check_recipe_availability(dish.recipe)
            )

            if (
                restriction not in dish_restrictions
                and ingredients_are_available
            ):
                dish_table["dish_name"].append(dish.name)
                dish_table["price"].append(dish.price)
                dish_table["ingredients"].append(dish_ingredients)
                dish_table["restrictions"].append(dish_restrictions)

        return pd.DataFrame(dish_table)
