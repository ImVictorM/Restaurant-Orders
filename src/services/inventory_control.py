from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, recipe: Recipe):
        for required_ingredient, require_amount in recipe.items():
            if not (
                required_ingredient in self.inventory
                and require_amount <= self.inventory[required_ingredient]
            ):
                return False
        return True

    def consume_recipe(self, recipe: Recipe) -> None:
        can_make_recipe = self.check_recipe_availability(recipe)
        if can_make_recipe:
            for recipe_ingredient, recipe_amount in recipe.items():
                self.inventory[recipe_ingredient] -= recipe_amount
        else:
            raise ValueError("Some ingredients are not available!")
