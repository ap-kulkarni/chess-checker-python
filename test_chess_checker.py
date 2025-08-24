import pytest

from chess_checker import get_next_moves


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


# queen in the corner
# queen at the edge
# queen at the center
# piece in invalid position
# invalid piece
