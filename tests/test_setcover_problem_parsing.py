from mz_python_puzzles.setcover.problem import parse_problem, CostedSet


def test_parse_small_problem():
    with open('tests/data/sc_6_1') as f:
        problem = parse_problem(f.read())

        assert set(range(9)) == problem.universe
        assert problem.sets == [
            CostedSet(0, 1, [0, 3]),
            CostedSet(1, 1, [0, 1, 2, 5, 6, 8]),
            CostedSet(2, 1, [1, 2, 5, 6, 8]),
            CostedSet(3, 1, [6, 7, 8]),
            CostedSet(4, 1, [0, 3, 4, 5, 6]),
            CostedSet(5, 1, [1, 2, 7, 8])
        ]
