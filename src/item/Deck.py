"""
Main deck object, holds cards and can be shuffled
"""

import random
from dataclasses import dataclass
from src.item.card import Card
from typing import List

@dataclass
class Deck:
    
    def __init__(self, cards: List[Card]):
        """Constructor for Deck object."""
        self._cards = cards
        
    @property
    def cards(self) -> list:
        """Return the list of cards in the deck."""
        return self._cards
    
    @property
    def size(self) -> int:
        """Return the number of cards in the deck."""
        return len(self._cards)
    
        
    