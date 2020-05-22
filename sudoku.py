import argparse as arg
import sys

from mz_python_puzzles.sudoku.algos import solve_sudoku
from mz_python_puzzles.sudoku.puzzle import parse_puzzle

if __name__ == '__main__':
    arg_parser = arg.ArgumentParser(
        formatter_class=arg.ArgumentDefaultsHelpFormatter
    )

    arg_parser.add_argument(
        '-t', '--text',
        help='Path to text representation of puzzle to solve (stdin default)'
    )

    args = arg_parser.parse_args()

    if args.text:
        puzzle_file = open(args.text)
    else:
        puzzle_file = sys.stdin

    solution = solve_sudoku(parse_puzzle(puzzle_file.read()))
    if solution:
        print(solution.render())
    else:
        print('Could not solve this Sudoku')

    if args.text:
        puzzle_file.close()
