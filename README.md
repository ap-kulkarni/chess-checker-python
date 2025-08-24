# Chess Next Move Checker

Given a chess piece and its position on board, this program gives list of possible moves

To keep things simple, the piece names and positions have been kept in lower case letters.

Python version used is 3.13 and the project has been set up with `uv`.
To run the tests, make sure `pytest` is installed in python environment and simply run `pytest`

To set up environment using `uv`, checkout the project and execute following commands after navigating to the directory where files have been checked out in terminal
``` python
uv venv
uv sync
source .venv/bin/activate # or other appropriate script for your SHELL
```

Usage:
```python
python chess_checker.py king a1
```