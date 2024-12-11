"""
Main Card object, card name, holds card rank, card suit, card value.
"""

from src.enum.card_info import CardRank, Suit

from dataclasses import dataclass


@dataclass
class Card:
    """Main card object, holds card rank, card suit, card value. Handles all card operations and behabior."""
    suit: Suit
    rank: CardRank
    
    def __init__(self, suit: Suit, rank: CardRank) -> None:
        """Constructor for Card object."""
        # primary arguments
        self._suit = suit.value
        self._rank = rank.value
        
    @property
    def name(self) -> str:
        """Card name getter."""
        return f"{self.rank} of {self.suit}"
    
    @property
    def rank(self) -> str:
        """Card name getter."""
        return self._rank["name"]
    
    @property
    def rank_symbol(self) -> str:
        """Card rank symbol getter."""
        return self._rank["symbol"]
    
    @property
    def suit(self) -> str:
        """Card suit getter."""
        return self._suit["name"]
        
    @property
    def suit_symbol(self) -> str:
        """Card suit symbol getter."""
        return self._suit["symbol"]
    
    @property
    def value(self) -> int:
        """Card value getter."""
        return self._rank["value"]
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"{self.suit} of {self.rank}"