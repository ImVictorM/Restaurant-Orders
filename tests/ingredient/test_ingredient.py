from src.models.ingredient import Ingredient


def test_ingredient():
    bacon = Ingredient("bacon")
    farinha = Ingredient("farinha")

    # test_ingredient_name
    assert bacon.name == "bacon"
    assert farinha.name == "farinha"

    # test_invalid_ingredient_has_no_restrictions
    invalid_ingredient = Ingredient("invalid_ingredient")
    assert invalid_ingredient.restrictions == set()

    # test_method__eq__
    assert farinha != bacon
    assert bacon == bacon

    # test_method__repr__
    assert repr(farinha) == "Ingredient('farinha')"
    assert repr(bacon) == "Ingredient('bacon')"

    # test_method__hash__
    assert hash(Ingredient("bacon")) == hash(Ingredient("bacon"))
    assert hash(Ingredient("bacon")) != hash(Ingredient("farinha"))
