from enum import Enum


class Suit(Enum):
    """Card suit enumerator class"""
    SPADES = { "name": "Spades", "symbol": "♠️" }
    DIAMONDS = { "name": "Diamonds", "symbol": "♦️" }
    CLUBS = { "name": "Clubs", "symbol": "♣️" }
    HEARTS = { "name": "Hearts", "symbol": "♥️" }

class CardRank(Enum):
    """Card rank enumerator class"""
    ACE = { "name": "Ace", "symbol": "A", "value": 14 }
    KING = { "name": "King", "symbol": "K", "value": 13 }
    QUEEN = { "name": "Queen", "symbol": "Q", "value": 12 }
    JACK = { "name": "Jack", "symbol": "J", "value": 11 }
    TEN = { "name": "10", "symbol": "10", "value": 10 }
    NINE = { "name": "9", "symbol": "9", "value": 9 }
    EIGHT = { "name": "8", "symbol": "8", "value": 8 }
    SEVEN = { "name": "7", "symbol": "7", "value": 7 }
    SIX = { "name": "6", "symbol": "6", "value": 6 }
    FIVE = { "name": "5", "symbol": "5", "value": 5 }
    FOUR = { "name": "4", "symbol": "4", "value": 4 }
    THREE = { "name": "3", "symbol": "3", "value": 3 }
    TWO = { "name": "2", "symbol": "2", "value": 2 }