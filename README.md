# War Card Game - Project

Building a command-line implementation of the card game "War" German  "Bettelmann" variant focusing on:
- Object-Oriented Programming principles
- Single Responsibility Principle
- Clean, simple syntax
- Dataclass usage where appropriate
- Testable components
- Collaborative development workflow

> [!NOTE]
> - 2-player card game
> - 32-card deck (7, 8, 9, 10, J, Q, K, A in ♠️, ♦️, ♣️, ♥️)
> - Cards rank: A (high) → 7 (low)
> - Each player gets 16 cards face down
> - Players reveal cards simultaneously
> - Higher card wins the round
> - Tied cards trigger additional draws until someone wins
> - Won cards go to winner's stash (not replayable)
> - Most cards in stash wins

<br><br>

## Development Strategy

> [!TIP]
> View **[Roadmap.md](/ROADMAP.md)** for more context and project development flow.

- Each milestone has dedicated branch `<milestone-name>`
- Issues branch from milestone: `<milestone-name>/<issue-n-name>`
- Pull requests required for merging
- Code review before merge
- Unit tests for completed modules

**Project directory structure:**
*(ubject to change during development)*
```
└── src
    └── actor
        └── __init__.py
        └── Player.py
    └── item
        └── __init__.py
        └── Card.py
        └── Deck.py
        └── ItemTemplate.py
    └── itemcontainer
        └── __init__.py
        └── Inventory.py
        └── PlayerInventory.py
    └── __init__.py
└── tests
└── .gitignore
└── LICENSE
└── ROADMAP.md
└── README.md
└── war.py
```

<br><br>

## Collaboration instructions

#### 1. Go to `<your project directory>` and open a terminal *(cmd, shell, bash...)

#### 2. Clone `dev` branch from git repository using:

Use the following **git-bash** command template to chekout an issue-specific branch (found on each issue/ticket page)

```bash
git clone -b <branch_name> --single-branch <https://github.com/theaprox/card-war.git>
```

This will create a new folder in your project directory called "card-war".

> [!IMPORTANT]
> You'll need to replace `<branch_name>` with a dedicated branch for each "issue" in [issues](https://github.com/theaprox/card-war/issues). You can find connected branches in issue description
>
> **EXAMPLE:**
> To work on "issue #2" you'd need to pull an "issues/2-deck-module" branch.

#### 3. Work on the dedicated branch

-   **step 1:** Asign yourself or ask to be asigned to an open/todo ticket before starting any work.

-   **step 2:** Develop a feature/issue on your dedicated branch and push it (the branch) to git repository.

-   **step 3:** Create a *Pull Request* asking to merge your `issue...` branch to `dev`.
> [!CAUTION]
> You **DO NOT** need to review, fix or confirm pull requests, only submit them.

#### 4. Completion

Before submitting a PR mark a ☑️ for each segment/step complete in the *issue* you work on. Only submit a PR if you managed to resolve an entire ticket. After review and merge it will be marked as `done` in the [project backlog](theaprox/projects/4/views/1) view.

Once done (your hour of programming is over) - go through with a 5-10 min stand-up regarding your work.
