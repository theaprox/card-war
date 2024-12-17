"""
Player instance class and operations.
Controls and manages Player instance actions and inventory
"""

from dataclasses import dataclass

@dataclass
class Player:

    def __init__(self, name: str):
        self._name = name.strip().capitalize()

    def __str__(self):
        return f"{self._name}"
    
    def __repr__(self):
        return f"{self._name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name
        