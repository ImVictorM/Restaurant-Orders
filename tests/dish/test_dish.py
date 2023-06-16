from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


@pytest.fixture
def dish():
    dish_name = "bacon and eggs"
    dish_price = 10
    return Dish(dish_name, dish_price)


def test_dish(dish):
    # def test_dish_instantiation(dish):
    assert dish.name == "bacon and eggs"
    assert dish.price == 10
    assert repr(dish) == "Dish('bacon and eggs', R$10.00)"

    # def test_dish_equality(dish):
    assert dish == dish
    assert dish != Dish("other_dish", 4)

    # def test_dish_hashing(dish):
    other_dish = Dish("other_dish", 4)

    assert hash(dish) == hash(dish)
    assert hash(dish) != hash(other_dish)

    # def test_dish_ingredients(dish):
    bacon = Ingredient("bacon")
    egg = Ingredient("ovo")

    dish.add_ingredient_dependency(bacon, 2)
    dish.add_ingredient_dependency(egg, 1)

    assert dish.recipe.get(bacon) == 2
    assert dish.recipe.get(egg) == 1
    assert dish.get_ingredients() == {bacon, egg}

    # def test_dish_restrictions(dish):
    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    # def test_dish_invalid_price():
    with pytest.raises(TypeError):
        Dish("invalid price", "here")

    # def test_dish_negative_price():
    with pytest.raises(ValueError):
        Dish("negative price", -4)
