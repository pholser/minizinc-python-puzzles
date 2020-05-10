from mz_python_puzzles.setcover.algos import minimum_set_cover_mz
from mz_python_puzzles.setcover.problem import parse_problem, Cover


def test_mz_small_problem():
    with open('tests/data/sc_6_1') as f:
        problem = parse_problem(f.read())

        solution = minimum_set_cover_mz(problem)

        assert Cover(
            2,
            [problem.sets[i] for i in [4, 5]]
        ) == solution


def test_mz_larger_problem():
    with open('tests/data/sc_1000_11') as f:
        problem = parse_problem(f.read())

        solution = minimum_set_cover_mz(problem)

        assert Cover(
            146,
            [problem.sets[i]
                for i in [0, 1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 16, 19, 20, 21,
                          23, 24, 25, 26, 28, 33, 35, 43, 46, 47, 50, 53, 59,
                          60, 61, 63, 70, 77, 83, 102, 104]]
        ) == solution
