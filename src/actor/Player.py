"""
Player instance class and operations.
Controls and manages Player instance actions and inventory
"""

from src.itemcontainer import PlayerInventory
from src.itemcontainer import Inventory


class Player:
    _name: str
    _inventory: PlayerInventory

    def __init__(self, name: str):
        self.name = name.strip().capitalize()
        self.inventory = self._inventory

    def get(cls, name: str):
        return cls(name)

    @property
    def name(self):
        return self._name

    @property
    def inventory(self):
        return self._inventory

    @name.setter
    def name(self, name: str):
        self._name = name

    @inventory.setter
    def inventory(self, inventory: Inventory):
        self._inventory = inventory

    ...
