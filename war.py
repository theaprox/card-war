"""
The main program interface.
Functional file to execute desired program using available objects and methods.
"""

import click
from src.logger import Logger
from src.actor.player import Player
from src.minigame.card_war import CardWar
from src.prompt import confirm


@click.command()
@click.option("-p1", "--player1", type=str, help="Name 'Player 1'", default=None)
@click.option("-p2", "--player2", type=str, help="Name 'Player 2'", default=None)
def main(player1, player2):
    """Start program with optional player names."""
    player1 = Player(player1 or "Player 1")
    player2 = Player(player2 or "Player 2")
    game = CardWar(player1, player2)
    
    while game:
        game.play()
        if not confirm("Play again?"):
            game = None
        else:
            print("\033[2J\033[H")
            game.restart()


if __name__ == "__main__":
    Logger.setup()
    main()
