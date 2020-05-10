from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import composite, integers, lists, sampled_from

from mz_python_puzzles.setcover.algos import minimum_set_cover_mz
from mz_python_puzzles.setcover.problem import Problem, CostedSet


@composite
def problem(draw):
    universe_as_list = list(
        range(0, draw(integers(min_value=1, max_value=101)))
    )
    universe = set(universe_as_list)

    candidates = []
    coverage = set()
    set_id = 0
    while coverage != universe:
        next_candidate = draw(
            lists(sampled_from(universe_as_list), min_size=1, unique=True)
        )

        candidates.append(
            CostedSet(
                set_id,
                draw(integers(min_value=1, max_value=10)),
                next_candidate)
        )
        coverage = coverage | set(next_candidate)
        set_id += 1

    return Problem(universe, candidates)


@given(problem())
@settings(
    deadline=None,
    suppress_health_check=[
        HealthCheck.too_slow,
        HealthCheck.data_too_large
    ])
def test_cover_consists_of_sets_we_started_with(problem):
    cover = minimum_set_cover_mz(problem)

    assert all(s in problem.sets for s in cover.sets)


@given(problem())
@settings(
    deadline=None,
    suppress_health_check=[
        HealthCheck.too_slow,
        HealthCheck.data_too_large
    ])
def test_cover_really_covers_universe(problem):
    cover = minimum_set_cover_mz(problem)

    assert (
        items_covered_by(cover)
        ==
        problem.universe
    )


@given(problem())
@settings(
    deadline=None,
    suppress_health_check=[
        HealthCheck.too_slow,
        HealthCheck.data_too_large
    ])
def test_cover_cost_matches_sum_of_chosen_set_costs(problem):
    cover = minimum_set_cover_mz(problem)

    assert cover.cost == sum(s.cost for s in cover.sets)


@given(problem())
@settings(
    deadline=None,
    suppress_health_check=[
        HealthCheck.too_slow,
        HealthCheck.data_too_large
    ])
def test_cover_is_maximal(problem):
    cover = minimum_set_cover_mz(problem)

    assert all(
        items_covered_by(cover, minus=s) != problem.universe
        for s in cover.sets)


def items_covered_by(cover, minus=None):
    items_covered = set()
    for s in cover.sets:
        if s != minus:
            items_covered = items_covered | set(s.items)
    return items_covered
