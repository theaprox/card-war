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
> - Players reveal cards simultaneously (one at a time)
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
├── src/
│   ├── __init__.py
│   ├── actor/
│   │   ├── __init__.py
│   │   └── Player.py               # Milestone 3, Issue 3.1
│   ├── item/
│   │   ├── __init__.py
│   │   ├── ItemTemplate.py         # Milestone 1, Issue 1.1
│   │   ├── Card.py                 # Milestone 2, Issue 2.1
│   │   └── Deck.py                 # Milestone 2, Issue 2.2
│   └── itemcontainer/
│       ├── __init__.py
│       ├── Inventory.py            # Milestone 1, Issue 1.2
│       └── PlayerInventory.py      # Milestone 1, Issue 1.2
├── tests/                          # Unit tests, Milestone 4...
├── .gitignore
├── LICENSE
├── README.md                       # Update per milestone
├── ROADMAP.md                      # Update per milestone
├── roadmap.md                      # Created & update per milestone
└── war.py                          # Milestone 3, Issue 3.2 & Milestone 4, Issue 4.1
```

<br><br>

## Collaboration instructions

Before proceeding with any of the steps bellow, please read through the entire section.

Then view [project page](https://github.com/users/theaprox/projects/4/views/1) to see which tickets are available (marked with `ready` status). Pick one ticket and read through the issue docs - there you'll find all necessary information regarding how and what is expected to be done.

#### 1. Go to `<your project directory>` and open a terminal *(cmd, shell, bash...)*

#### 2. Clone `dev` branch from git repository using:

Use the following command template to chekout an issue-specific branch (found on each issue/ticket page)

```bash
git clone -b <branch_name> --single-branch https://github.com/theaprox/card-war.git
```

This will create a new folder in your project directory called "card-war".
From this point any `git` commands should be run from within the **card-war** directory.

> [!IMPORTANT]
> You'll need to replace `<branch_name>` with a dedicated branch for each "issue" in [issues](https://github.com/theaprox/card-war/issues). You can find connected branches in issue description
>
> **EXAMPLE:**
> To work on "Issue 1.1" you'd need to pull an "milestone/1-core/issue-1-item-template" branch.

#### 3. Sync changes from `Dev` to `<issue_branch>`

before doing any actual work you should fetch and sync any and all changes from the `dev` branch to your locally cloned issue-specific branch.

**You can do so in a few steps**

1. Fetch `dev` branch for syncing:
```bash
git fetch origin dev:dev
```

2. Make sure you are on the specific issue branch `<branch_name>`:
```bash
git checkout <branch_name>
```

3. Merge from `dev` to `<branch_name>`:
```bash
git merge dev
```
> [!CAUTION]
> If you encounter merge conflicts during step 3, please:
> - Stop the process immediately
> - DO NOT push any changes
> - Contact the project maintainer

4. Sync updated `<branch_name>` to remote *(origin)*:
```bash
git push origin HEAD
```

5. Remove `dev` branch from local repo to avoid confusion and errors:
```bash
git branch -d dev
```

#### 4. Work on the dedicated branch

-   **step 1:** Asign yourself or ask to be asigned to an open/todo ticket before starting any work.

-   **step 2:** Develop a feature/issue on your dedicated branch and push it (the branch) to git repository.

-   **step 3:** Create a *Pull Request* asking to merge your `issue...` branch to `dev`.
> [!CAUTION]
> You **DO NOT** need to review, fix or confirm pull requests, only submit them.

#### 5. Completion

Mark a ☑️ for each segment/step complete in the *issue* you work on. Only submit a PR if you managed to resolve an entire ticket. After review and merge it will be marked as `done` in the [project backlog](theaprox/projects/4/views/1) view.

Once done (your hour of programming is over) - go through with a 5-10 min stand-up regarding your work.
