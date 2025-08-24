import sys

MAX_ROW = "8"
MIN_ROW = "1"
MIN_COLUMN = "a"
MAX_COLUMN = "h"


def _get_column_and_row_from_position(position: str) -> tuple[str, str]:
    return position[0], position[1]


def _get_row_with_offset(row: str, offset: int) -> str:
    offset_row = chr(ord(row) + offset)
    offset_row = MIN_ROW if offset_row < MIN_ROW else offset_row
    offset_row = MAX_ROW if offset_row > MAX_ROW else offset_row
    return offset_row


def _get_column_with_offset(row: str, offset: int) -> str:
    offset_column = chr(ord(row) + offset)
    offset_column = MIN_COLUMN if offset_column < MIN_COLUMN else offset_column
    offset_column = MAX_COLUMN if offset_column > MAX_COLUMN else offset_column
    return offset_column


def _get_next_move_with_offsets(
    current_position: str, row_offset: int, column_offset: int
):
    column, row = _get_column_and_row_from_position(current_position)
    next_possible_row = _get_row_with_offset(row, row_offset)
    next_possible_column = _get_column_with_offset(column, column_offset)
    return f"{next_possible_column}{next_possible_row}"


def _update_moves_list_with_next_move(
    moves_list: list[str], next_move: str, current_position: str
) -> None:
    if next_move not in moves_list and next_move != current_position:
        moves_list.append(next_move)


def _get_next_moves_for_pawn(current_position: str) -> list[str]:
    possible_moves: list[str] = []
    next_move = _get_next_move_with_offsets(current_position, 1, 0)
    _update_moves_list_with_next_move(possible_moves, next_move, current_position)
    return possible_moves


def _get_next_moves_for_king(current_position: str) -> list[str]:
    possible_moves: list[str] = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            next_move = _get_next_move_with_offsets(current_position, i, j)
            _update_moves_list_with_next_move(
                possible_moves, next_move, current_position
            )
    return possible_moves


def get_next_moves(piece: str, current_position: str) -> list[str]:
    if piece == "pawn":
        return _get_next_moves_for_pawn(current_position)
    if piece == "king":
        return _get_next_moves_for_king(current_position)
    return []


if __name__ == "__main__":
    moves = get_next_moves(*sys.argv[1:])
    print(",".join(moves))
