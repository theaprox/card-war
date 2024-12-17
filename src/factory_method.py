from src.item.deck import Deck
from src.item.card import Card
from src.enum.card_info import CardRank, Suit

def deck_factory(card_count: int) -> Deck:
    """Factory method for creating a deck of cards."""
    min_cards = 2 # hard limit minimum card count to not break stuff...
    max_cards = len(CardRank) * len(Suit)
    card_count = max(min(card_count, max_cards), min_cards)
    cards_list = []

    for rank in CardRank:
        for suit in Suit:
            cards_list.append(card_factory(rank, suit))

    return Deck(cards_list[:card_count])

def card_factory(rank: CardRank, suit: Suit) -> Card:
    """Fetch a card object by description."""
    return Card(rank, suit)