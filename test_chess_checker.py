import pytest

from chess_checker import get_next_moves


def _list_equals(list1: list[str], list2: list[str]) -> bool:
    return set(list1) == set(list2)


def test_pawn_in_lower_corner_has_one_possible_moves() -> None:
    got = get_next_moves("pawn", "a1")
    want = ["a2"]
    assert _list_equals(got, want)


def test_pawn_in_upper_corner_has_no_moves() -> None:
    got = get_next_moves("pawn", "h8")
    want: list[str] = []
    assert _list_equals(got, want)


def test_pawn_in_center_has_one_possible_move() -> None:
    got = get_next_moves("pawn", "d4")
    want = ["d5"]
    assert _list_equals(got, want)


def test_pawn_at_the_edge_has_one_possible_move() -> None:
    got = get_next_moves("pawn", "h4")
    want = ["h5"]
    assert _list_equals(got, want)


# king in the corner
@pytest.mark.parametrize(
    "piece, position, output",
    [
        ("king", "a1", ["a2", "b1", "b2"]),
        ("king", "h1", ["g1", "g2", "h2"]),
        ("king", "a8", ["a7", "b7", "b8"]),
        ("king", "h8", ["g8", "g7", "h7"]),
    ],
)
def test_king_in_the_corner_has_three_possible_moves(
    piece: str, position: str, output: list[str]
) -> None:
    got = get_next_moves(piece, position)
    want = output
    assert _list_equals(got, want)


@pytest.mark.parametrize(
    "piece, position, output",
    [
        ("king", "c3", ["b2", "b3", "b4", "c4", "d4", "d3", "d2", "c2"]),
        ("king", "e5", ["d4", "d5", "d6", "e6", "f6", "f5", "f4", "e4"]),
        ("king", "d5", ["c4", "c5", "c6", "d4", "d6", "e4", "e5", "e6"]),
        ("king", "g7", ["f8", "g8", "h8", "h7", "h6", "g6", "f6", "f7"]),
    ],
)
def test_king_in_the_middle_has_eight_possible_moves(
    piece: str, position: str, output: list[str]
) -> None:
    got = get_next_moves(piece, position)
    want = output
    assert _list_equals(got, want)


@pytest.mark.parametrize(
    "piece, position, output",
    [
        ("king", "a3", ["a2", "a4", "b4", "b3", "b2"]),
        ("king", "d1", ["c1", "c2", "d2", "e2", "e1"]),
        ("king", "h6", ["g7", "h7", "h5", "g5", "g6"]),
        ("king", "c8", ["d8", "d7", "c7", "b7", "b8"]),
    ],
)
def test_king_at_the_edge_has_five_possible_moves(
    piece: str, position: str, output: list[str]
) -> None:
    got = get_next_moves(piece, position)
    want = output
    assert _list_equals(got, want)


# queen in the corner
# queen at the edge
# queen at the center
# piece in invalid position
# invalid piece
