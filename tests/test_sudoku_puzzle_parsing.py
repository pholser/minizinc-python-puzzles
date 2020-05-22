from mz_python_puzzles.sudoku.puzzle import parse_puzzle


def test_parse_small_problem():
    with open('tests/data/sudoku1') as f:
        puzzle = parse_puzzle(f.read())

        assert 9 == puzzle.size
        assert [
            [None, None, None, 4, 6, 9, None, 2, None],
            [5, 9, None, None, 3, None, 7, None, None],
            [None, None, 4, None, 5, None, None, None, 6],
            [None, 2, 7, None, 4, 6, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, 5, 2, None, 1, 6, None],
            [7, None, None, None, 1, None, 6, None, None],
            [None, None, 1, None, 8, None, None, 7, None],
            [None, 8, None, 9, 7, 5, None, None, None]
        ] == puzzle.grid
        assert [
            [0, 3, 4], [0, 4, 6], [0, 5, 9], [0, 7, 2],
            [1, 0, 5], [1, 1, 9], [1, 4, 3], [1, 6, 7],
            [2, 2, 4], [2, 4, 5], [2, 8, 6],
            [3, 1, 2], [3, 2, 7], [3, 4, 4], [3, 5, 6],
            [5, 3, 5], [5, 4, 2], [5, 6, 1], [5, 7, 6],
            [6, 0, 7], [6, 4, 1], [6, 6, 6],
            [7, 2, 1], [7, 4, 8], [7, 7, 7],
            [8, 1, 8], [8, 3, 9], [8, 4, 7], [8, 5, 5]
        ] == list(puzzle.known_cells())


def test_render_small_problem():
    with open('tests/data/sudoku1') as f:
        puzzle = parse_puzzle(f.read())

        assert "\n".join([
            '_ _ _ 4 6 9 _ 2 _',
            '5 9 _ _ 3 _ 7 _ _',
            '_ _ 4 _ 5 _ _ _ 6',
            '_ 2 7 _ 4 6 _ _ _',
            '_ _ _ _ _ _ _ _ _',
            '_ _ _ 5 2 _ 1 6 _',
            '7 _ _ _ 1 _ 6 _ _',
            '_ _ 1 _ 8 _ _ 7 _',
            '_ 8 _ 9 7 5 _ _ _'
        ]) == puzzle.render()
