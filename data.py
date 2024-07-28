from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient


class Data:
    BUN_NAME = 'Bun'
    BUN_PRICE = 200
    INGREDIENT_1_NAME = 'ingredient_1'
    INGREDIENT_1_PRICE = 100
    INGREDIENT_1_TYPE = INGREDIENT_TYPE_SAUCE
    INGREDIENT_2_NAME = 'Ingredient_2'
    INGREDIENT_2_PRICE = 50
    INGREDIENT_2_TYPE = INGREDIENT_TYPE_FILLING

class TestConfig:
    BUNS = [
        {"name": "black bun", "price": 100},
        {"name": "white bun", "price": 200},
        {"name": "red bun", "price": 300},
    ]
    
    INGREDIENTS = [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
    ]

