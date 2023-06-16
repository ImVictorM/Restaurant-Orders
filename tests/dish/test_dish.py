from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


@pytest.fixture
def bacon_and_eggs():
    dish_name = "bacon and eggs"
    dish_price = 10
    return Dish(dish_name, dish_price)


@pytest.fixture
def other_dish():
    dish_name = "other_dish"
    dish_price = 4
    return Dish(dish_name, dish_price)


def test_dish(bacon_and_eggs, other_dish):
    # def test_dish_instantiation(dish):
    assert bacon_and_eggs.name == "bacon and eggs"
    assert bacon_and_eggs.price == 10
    assert repr(bacon_and_eggs) == "Dish('bacon and eggs', R$10.00)"

    # def test_dish_equality(dish):
    assert bacon_and_eggs == bacon_and_eggs
    assert bacon_and_eggs != other_dish

    # def test_dish_hashing(dish, other_dish):
    assert hash(bacon_and_eggs) == hash(bacon_and_eggs)
    assert hash(bacon_and_eggs) != hash(other_dish)

    # def test_dish_ingredients(dish):
    bacon = Ingredient("bacon")
    egg = Ingredient("ovo")

    bacon_and_eggs.add_ingredient_dependency(bacon, 2)
    bacon_and_eggs.add_ingredient_dependency(egg, 1)

    assert bacon_and_eggs.recipe.get(bacon) == 2
    assert bacon_and_eggs.recipe.get(egg) == 1
    assert bacon_and_eggs.get_ingredients() == {bacon, egg}

    # def test_dish_restrictions(dish):
    assert bacon_and_eggs.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    # def test_dish_invalid_price():
    with pytest.raises(TypeError):
        Dish("invalid price", "here")

    # def test_dish_negative_price():
    with pytest.raises(ValueError):
        Dish("negative price", -4)
