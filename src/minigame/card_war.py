
from rich import print
from random import sample
from typing import List
from dataclasses import dataclass
from src.actor.player import Player
from src.item.deck import Deck
from src.item.card import Card
from src.factory_method import deck_factory
from src.prompt import confirm_prompt


@dataclass
class PlayerState:
    """Per-player helper class to manage player state."""
    player: Player
    cards: List[Card]
    score: int = 0


class CardWar:

    def __init__(self, player1: Player, player2: Player, deck_size: int = 32):
        """Constructor for CardWar game object and its dependencies."""
        self._deck_size = deck_size
        self.deck: Deck = deck_factory(deck_size)
        self.player1 = PlayerState(player1, [])
        self.player2 = PlayerState(player2, [])

    def play(self):
        """Play the game."""
        stack = 0
        player1 = self.player1
        player2 = self.player2

        if self.deck.size >= 2:
            self.deal_deck()
        else:
            print("Not enough cards in deck!")
            return

        if len(player1.cards) != len(self.player2.cards):
            print("Player deck sizes do not match!")
            return

        cards_left = len(player1.cards)  # should match player2 card count

        for _ in range(cards_left):
            p1_card = player1.cards.pop()
            p2_card = player2.cards.pop()
            winner, p1_msg, p2_msg, split_msg = None, None, None, None

            if p1_card.value > p2_card.value:
                winner = player1
            elif p1_card.value < p2_card.value:
                winner = player2
            else:
                stack += 1

            if winner is player1:
                p1_msg = f"[bold blue]{player1.player}'s {p1_card}[/bold blue]"
                split_msg = f"<-"
                player1.score += stack + 1
                stack = 0
            elif winner is player2:
                p2_msg = f"[bold blue]{p2_card} {player2.player}'s[/bold blue]"
                split_msg = f"->"
                player2.score += stack + 1
                stack = 0
            else:
                p1_msg = f"[bold yellow]{player1.player}'s {p1_card}[/bold yellow]"
                p2_msg = f"[bold yellow]{p2_card} {player2.player}'s[/bold yellow]"
                split_msg = f"({stack})"

            print(self.draw_info(p1_card, p2_card, p1_msg, p2_msg, split_msg), end="")
            self.interrupt(msg="Play next round...")


        if player1.score == player2.score:
            winner_msg = "[bold yellow]Draw![/bold yellow]"
        else:
            winner = player1.player if player1.score > player2.score else player2.player
            winner_msg = f"{winner} wins!"

        print(f"\n[bold yellow]{winner_msg}[/bold yellow]\n")

    def draw_info(self, p1c: Card, p2c: Card, p1m: str, p2m: str, splitm: str) -> str:
        """Return string of drwa information for the turn."""
        p1 = self.player1
        p2 = self.player2
        p1m = p1m or f"{p1.player}'s [bold]{p1c}[/bold]"
        p2m = p2m or f"[bold]{p2c}[/bold] {p2.player}'s"
        return f"({p1.score}) {p1m}[italic dim]{splitm.center(8)}[/italic dim]{p2m} ({p2.score})"

    def interrupt(self, msg: str) -> None:
        """Interrupt the game."""
        print(f"[dim] \[ENTER] {msg}[/dim]", end="")
        input()

    def deal_deck(self) -> None:
        """Deal a deck of cards to two players."""
        size = self.deck.size
        shuffled_deck = sample(self.deck.cards, (size - (size % 2)))
        self.player1.cards = shuffled_deck[:len(shuffled_deck)//2]
        self.player2.cards = shuffled_deck[len(shuffled_deck)//2:]

    def restart(self) -> None:
        """Restart the game."""
        self.__init__(self.player1.player, self.player2.player, self._deck_size)
