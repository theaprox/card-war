## Milestone 1: Core Infrastructure
Branch: `<milestone-core>`

### Issue 1.1: Base Template Implementation
**Branch name:** `milestone/1-core/issue-1-item-template`
#### TODO:
- [ ] Create ItemTemplate class with:
  - [ ] Properties: _id, _type, _name
  - [ ] Basic getters/setters
  - [ ] Type checking methods
- [ ] Add docstrings and type hints
- [ ] Implement basic validation

> [!NOTE]
> Target files:
> `./src/item/ItemTemplate.py`

### Issue 1.2: Container Base Classes
**Branch name:** `milestone/1-core/issue-2-containers`
#### TODO:
- [ ] Create base Inventory class:
  - [ ] Methods: add, remove, get
  - [ ] Type validation
  - [ ] Basic error handling
- [ ] Create PlayerInventory class:
  - [ ] Extend base Inventory
  - [ ] Implement play stack container
  - [ ] Implement stash container

> [!NOTE]
> Target files:
> `./src/itemcontainer/Inventory.py`
> `./src/itemcontainer/PlayerInventory.py`

## Milestone 2: Game Components
Branch: `<milestone-components>`

### Issue 2.1: Card Implementation
**Branch name:** `milestone/2-components/issue-1-cards`
#### TODO:
- [ ] Create Suit dataclass
- [ ] Implement Card class:
  - [ ] Extend ItemTemplate
  - [ ] Properties: rank, suit, name, value
  - [ ] Factory method Card.get()
  - [ ] Comparison methods

> [!NOTE]
> Target files:
> `./src/item/Card.py`

### Issue 2.2: Deck Implementation
**Branch name:** `milestone/2-components/issue-2-deck`
#### TODO:
- [ ] Create Deck class:
  - [ ] Generate 32-card deck
  - [ ] Shuffle method
  - [ ] Deal method
- [ ] Add validation for card uniqueness

> [!NOTE]
> Target files:
> `./src/item/Deck.py`

## Milestone 3: Game Logic
Branch: `<milestone-gamelogic>`

### Issue 3.1: Player Implementation
**Branch name:** `milestone/3-gamelogic/issue-1-player` 
#### TODO:
- [ ] Build a Player class:
  - [ ] Properties: id, name, inventory (cards and stash)
  - [ ] Methods: draw_card, add_to_stash
  - [ ] Score calculation

> [!NOTE]
> Target files:
> `./src/actor/Player.py.py`

### Issue 3.2: Core Game Loop
**Branch name:** `milestone/3-gamelogic/issue-2-gameloop`
#### TODO:
- [ ] Implement main game logic:
  - [ ] Add support for optional command-line arguments to set player names
  (using `argparse` library)
  - [ ] Player initialization
  Initialize 2 players (with given or default names "Player 1" and "Player 2")
  - [ ] Card dealing
  Create a deck, shuffle, and "deal" cards to player inventories.
  Initiate gameplay (one-click per draw for both players)
  - [ ] Tie handling
  Continuous card drawing on Tied
  - [ ] Round resolution
  Logic for tie/win/loose, stash won cards to winner
  - [ ] Victory conditions
  When players are out of cards, take score and declare winner and looser

> [!NOTE]
> Target files:
> `./war.py` (main program file)

## Milestone 4: Final Implementation
Branch: `<milestone-final>`

### Issue 4.1: CLI Interface
**Branch name:** `milestone/4-finale/issue-1-cli`
#### TODO:
- [ ] Implement command line interface:
  - [ ] Player name input
  - [ ] Game state display
  - [ ] Round results
  - [ ] Final score

> [!NOTE]
> Target files:
> `./war.py` (main program file)

### Issue 4.2: Testing & Documentation
**Branch name:** `milestone/4-finale/issue-2-testing` 
#### TODO:
- [ ] Create unit tests for:
  - [ ] Card operations
  - [ ] Deck operations
  - [ ] Game logic
  - [ ] Player actions
- [ ] Update documentation
- [ ] Add usage examples

> [!NOTE]
> Target files:
> `./tests/*`
> `./README.md`

## Next Steps
After completing each milestone:
1. Review code quality
2. Run tests
3. Update documentation
4. Merge to main branch
5. Plan next milestone implementation