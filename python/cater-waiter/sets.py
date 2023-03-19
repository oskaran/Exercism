"""Functions for compiling dishes and ingredients for a catering company."""

from typing import List, Tuple, Union, Set, Optional

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

Dish = Tuple[str, Union[List[str], Set[str]]]

def clean_ingredients(dish_name: str, dish_ingredients: List[str]) -> Tuple[str, set]:
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return dish_name, set(dish_ingredients)


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    return f'{drink_name} Cocktail' if ALCOHOLS & set(drink_ingredients) else f'{drink_name} Mocktail'


def categorize_dish(dish_name: str, dish_ingredients: List[str]) -> Optional[str]:
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    categories =  (('VEGAN', VEGAN), ('VEGETARIAN', VEGETARIAN), ('KETO', KETO), ('PALEO', PALEO)\
                   , ('OMNIVORE', OMNIVORE))
    dish_ingredients_set = set(dish_ingredients)
    for category, CATEGORY in categories:
        if dish_ingredients_set <= CATEGORY:
            return f'{dish_name}: {category}'
    return None

def tag_special_ingredients(dish: Dish) -> Tuple[str, set]:
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special
    note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need
    to be tracked are in the SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    return dish[0], SPECIAL_INGREDIENTS.intersection(set(dish[1]))


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    return set.union(*dishes)


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: List[Set[str]], intersection: Set[str]) -> Set[str]:
    """Determine which `dishes` have a singleton ingredient (an ingredient that
        only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants
        imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.
+
    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category.
    `<CATEGORY>` can be any one of: (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    return set.union(*dishes) - intersection
