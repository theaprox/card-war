"""
Main deck object, holds cards and can be shuffled
"""

from dataclasses import dataclass
from typing import List, Any

@dataclass
class Deck:
    _cards: List[Any]
    
    def __init__(self):
        self.cards = self._cards
        
    def shuffle(self):
        import random
        random.shuffle(self.cards)
        
    