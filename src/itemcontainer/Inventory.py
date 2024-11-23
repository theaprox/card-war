"""
Inventory class, handle inventory operations and foundational structure
"""

from typing import List, Any


class Inventory:
    """Base Inventory class, extended via specific inventory types (eg. PlayerInventory)"""
    _items: List[Any]

    def __init__(self) -> None:
        self.items = List[Any] = []

    def get(cls):
        """Create a new empty inventory instance"""
        return cls()

    @property
    def items(self) -> List[Any]:
        """Return the list of items in the inventory"""
        return self._items

    def add_item(self, item: Any):
        """Add an item to inventory"""
        self._items.append(item)

    def get_item(self, item: Any):
        """Get and return a specific item from inventory"""
        ...

    def remove_item(self, item):
        """Remove a specific item from inventory"""
        ...

    ...
