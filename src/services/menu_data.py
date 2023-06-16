import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        df = pd.read_csv(source_path)
        self.dishes = set()

        grouped_df = (
            df.groupby(["dish", "price"])
            .apply(lambda df: list(zip(df["ingredient"], df["recipe_amount"])))
        )

        print(grouped_df)


MenuData("data/menu_base_data.csv")
