from datetime import timedelta
from importlib.resources import path
from minizinc import Instance, Model, Solver

from mz_python_puzzles.sudoku.puzzle import Puzzle


def solve_sudoku(puzzle):
    with path('mz_python_puzzles.sudoku.mz', 'sudoku.mzn') as model_path:
        model = Model(model_path)
    solver = Solver.lookup('org.gecode.gecode')

    instance = Instance(solver, model)
    instance['UNIT'] = puzzle.unit
    fixed_points = list(puzzle.known_cells())
    instance['FIXED'] = len(fixed_points)
    instance['fixed_points'] = list(
        map(lambda rcv: [rcv[0] + 1, rcv[1] + 1, rcv[2]], fixed_points)
    )

    result = instance.solve(timeout=timedelta(seconds=5))

    if result.status.has_solution():
        solution = Puzzle(puzzle.unit)
        for r in range(puzzle.size):
            for c in range(puzzle.size):
                solution[r][c] = result.solution.grid[r][c]
        return solution

    return None
