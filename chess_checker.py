import sys


def _get_row_and_column_from_position(position: str) -> tuple[str, str]:
    return position[0], position[1]


def get_next_moves(piece: str, current_position: str) -> list[str]:
    column, row = _get_row_and_column_from_position(current_position)
    next_moves: list[str] = []
    next_row = chr(min(ord(row) + 1, ord("8")))
    next_move = f"{column}{next_row}"
    if next_move != current_position:
        next_moves.append(next_move)
    return next_moves


if __name__ == "__main__":
    moves = get_next_moves(*sys.argv[1:])
    print(",".join(moves))
