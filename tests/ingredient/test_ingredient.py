from src.models.ingredient import Ingredient
import pytest


@pytest.fixture
def bacon():
    return Ingredient("bacon")


@pytest.fixture
def farinha():
    return Ingredient("farinha")


def test_ingredient_name(bacon, farinha):
    assert bacon.name == "bacon"
    assert farinha.name == "farinha"


def test_ingredient_equality(bacon, farinha):
    assert farinha != bacon
    assert bacon == bacon


def test_ingredient_representation(bacon, farinha):
    assert repr(farinha) == "Ingredient('farinha')"
    assert repr(bacon) == "Ingredient('bacon')"


def test_ingredient_hashing(bacon, farinha):
    assert hash(bacon) == hash(bacon)
    assert hash(bacon) != hash(farinha)


def test_invalid_ingredient_has_no_restrictions():
    invalid_ingredient = Ingredient("invalid_ingredient")
    assert invalid_ingredient.restrictions == set()
