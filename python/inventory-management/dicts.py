"""Functions to keep track and alter inventory."""

from typing import List, Dict, Tuple

def create_inventory(items: List[str]) -> Dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in set(items)}


def add_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    inv_update = create_inventory(items)
    for item in inv_update.keys():
        inventory[item] = inventory.get(item, 0) + inv_update.get(item, 0)

    return inventory


def decrement_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    inv_update = create_inventory(items)
    for item in inv_update.keys():
        inventory[item] = \
            ((inventory[item] - inv_update[item] if inventory[item] >= inv_update[item] else 0))

    return inventory


def remove_item(inventory: Dict[str, int], item: str) -> Dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: Dict[str, int]) -> List[Tuple[str, int]]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(k, v) for k, v in inventory.items() if v > 0]
