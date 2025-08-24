import pytest

from chess_checker import get_next_moves
from exceptions import InvalidPieceException, InvalidPositionException


def _list_equals(list1: list[str], list2: list[str]) -> bool:
    return set(list1) == set(list2)


@pytest.mark.parametrize(
    "position, want",
    [
        ("a1", ["a2"]),
        ("h1", ["h2"]),
        ("d4", ["d5"]),
        ("h4", ["h5"]),
    ],
)
def test_pawn_moves_in_vertical_forward_direction(
    position: str, want: list[str]
) -> None:
    got = get_next_moves("pawn", position)
    assert _list_equals(got, want)


@pytest.mark.parametrize(
    "position",
    [
        ("a8"),
        ("c8"),
        ("e8"),
        ("h8"),
    ],
)
def test_pawn_in_upper_edge_has_no_moves(position: str) -> None:
    got = get_next_moves("pawn", position)
    assert _list_equals(got, [])


@pytest.mark.parametrize(
    "position, want",
    [
        ("a1", ["a2", "b1", "b2"]),
        ("h1", ["g1", "g2", "h2"]),
        ("a8", ["a7", "b7", "b8"]),
        ("h8", ["g8", "g7", "h7"]),
    ],
)
def test_king_in_the_corner_has_three_possible_moves(
    position: str, want: list[str]
) -> None:
    got = get_next_moves("king", position)
    assert _list_equals(got, want)


@pytest.mark.parametrize(
    "position, want",
    [
        ("c3", ["b2", "b3", "b4", "c4", "d4", "d3", "d2", "c2"]),
        ("e5", ["d4", "d5", "d6", "e6", "f6", "f5", "f4", "e4"]),
        ("d5", ["c4", "c5", "c6", "d4", "d6", "e4", "e5", "e6"]),
        ("g7", ["f8", "g8", "h8", "h7", "h6", "g6", "f6", "f7"]),
    ],
)
def test_king_in_the_middle_has_eight_possible_moves(
    position: str, want: list[str]
) -> None:
    got = get_next_moves("king", position)
    assert _list_equals(got, want)


@pytest.mark.parametrize(
    "position, want",
    [
        ("a3", ["a2", "a4", "b4", "b3", "b2"]),
        ("d1", ["c1", "c2", "d2", "e2", "e1"]),
        ("h6", ["g7", "h7", "h5", "g5", "g6"]),
        ("c8", ["d8", "d7", "c7", "b7", "b8"]),
    ],
)
def test_king_at_the_edge_has_five_possible_moves(
    position: str, want: list[str]
) -> None:
    got = get_next_moves("king", position)
    assert _list_equals(got, want)


# fmt: off
@pytest.mark.parametrize(
    "position, want",
    [   
        ("a1", ["a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]),
        ("a8", ["a7", "a6", "a5", "a4", "a3", "a2", "a1", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]),
        ("h1", ["h2", "h3", "h4", "h5", "h6", "h7", "h8", "a1", "b1", "c1", "d1", "e1", "f1", "g1", "g2", "f3", "e4", "d5", "c6", "b7", "a8"])
    ],
)
# fmt: on
def test_queen_in_the_corner_has_twenty_one_possible_moves(position: str, want: list[str]) -> None:
    got = get_next_moves("queen", position)
    assert _list_equals(got, want)

# fmt: off
@pytest.mark.parametrize(
    "position, want",
    [   
        ("e4", ["a4", "b4", "c4", "d4", "f4", "g4", "h4", "e1", "e2", "e3", "e5", "e6", "e7", "e8", "a8", "b7", "c6", "d5", "f3", "g2", "h1", "b1", "c2", "d3", "f5", "g6", "h7"]),
        ("b7", ["a7", "c7", "d7", "e7", "f7", "g7", "h7", "b1", "b2", "b3", "b4", "b5", "b6", "b8", "a8", "c6", "d5", "e4", "f3", "g2", "h1", "a6", "c8"])
    ],
)
# fmt: on
def test_queen_in_the_middle(position: str, want: list[str]) -> None:
    got = get_next_moves("queen", position)
    assert _list_equals(got, want)


def test_invalid_piece_raises_error() -> None:
    with pytest.raises(InvalidPieceException):
        get_next_moves("kueen", "a1")


@pytest.mark.parametrize("position", ["z1", "abc", "a"])
def test_invalid_current_position_raises_error(position: str) -> None:
    with pytest.raises(InvalidPositionException):
        get_next_moves("king", position)
