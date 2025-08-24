from chess_checker import get_next_moves


def test_pawn_in_lower_corner_has_one_possible_moves() -> None:
    got = get_next_moves("pawn", "a1")
    want = ["a2"]
    assert got == want


def test_pawn_in_upper_corner_has_no_moves() -> None:
    got = get_next_moves("pawn", "h8")
    want: list[str] = []
    assert got == want


def test_pawn_in_center_has_one_possible_move() -> None:
    got = get_next_moves("pawn", "d4")
    want = ["d5"]
    assert got == want


def test_pawn_at_the_edge_has_one_possible_move() -> None:
    got = get_next_moves("pawn", "h4")
    want = ["h5"]
    assert got == want


# king in the corner
# king on the edge
# king at the center
# queen in the corner
# queen at the edge
# queen at the center
# piece in invalid position
# invalid piece
