from datetime import timedelta
from importlib.resources import path
from minizinc import Instance, Model, Solver

from mz_python_puzzles.setcover.problem import Cover


def minimum_set_cover_mz(problem):
    with path('mz_python_puzzles.setcover.mz', 'setcover.mzn') as model_path:
        model = Model(model_path)
    solver = Solver.lookup('org.minizinc.mip.coin-bc')

    instance = Instance(solver, model)
    instance['N'] = len(problem.universe)
    instance['M'] = len(problem.sets)
    instance['cost'] = list(map(lambda s: s.cost, problem.sets))
    instance['items_covered'] = (
        list(map(lambda s: set(map(lambda i: i + 1, s.items)), problem.sets))
    )

    result = instance.solve(timeout=timedelta(seconds=5))

    if result.status.has_solution():
        return Cover(
            result.objective,
            [problem.sets[i] for i, s in enumerate(result.solution.chosen)
                if s == 1]
        )
    return None
