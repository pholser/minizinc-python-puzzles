from mz_python_puzzles.sudoku.algos import solve_sudoku
from mz_python_puzzles.sudoku.puzzle import parse_puzzle


def test_mz_sudoku():
    with open('tests/data/sudoku1') as f:
        puzzle = parse_puzzle(f.read())

        solution = solve_sudoku(puzzle)

        assert [
            [3, 7, 8, 4, 6, 9, 5, 2, 1],
            [5, 9, 6, 1, 3, 2, 7, 8, 4],
            [2, 1, 4, 8, 5, 7, 9, 3, 6],
            [1, 2, 7, 3, 4, 6, 8, 5, 9],
            [8, 6, 5, 7, 9, 1, 3, 4, 2],
            [4, 3, 9, 5, 2, 8, 1, 6, 7],
            [7, 5, 3, 2, 1, 4, 6, 9, 8],
            [9, 4, 1, 6, 8, 3, 2, 7, 5],
            [6, 8, 2, 9, 7, 5, 4, 1, 3]
        ] == solution.grid
