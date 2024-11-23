"""
PlayerInventory class.
Specific InventoryType to be associated with Player.
Holds player Items of all propper (implemented) types, like Card, Stash, etc
"""

from dataclasses import dataclass
from typing import List, Any
from src.itemcontainer.Inventory import Inventory


@dataclass
class PlayerInventory(Inventory):
    _items: List[Any]

    def __init__(self):
        ...

    ...
