from praktikum.bun import Bun
from praktikum.database import Database
from data import TestConfig

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == len(TestConfig.BUNS)

        for i, bun in enumerate(buns):
            assert bun.name == TestConfig.BUNS[i]["name"]
            assert bun.price == TestConfig.BUNS[i]["price"]

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == len(TestConfig.INGREDIENTS)

        for i, ingredient in enumerate(ingredients):
            assert ingredient.get_type() == TestConfig.INGREDIENTS[i]["type"]
            assert ingredient.get_name() == TestConfig.INGREDIENTS[i]["name"]
            assert ingredient.get_price() == TestConfig.INGREDIENTS[i]["price"]
