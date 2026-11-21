"""Tests for cheap_eats."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from cheap_eats import RECIPES, can_make, format_recipe, get_recipe, under_budget  # noqa: E402


def test_get_recipe_finds_known_slug():
    assert get_recipe("rice-and-beans").name == "Rice and Beans"


def test_get_recipe_unknown_slug_raises():
    with pytest.raises(KeyError):
        get_recipe("lobster")


@pytest.mark.parametrize("max_cost", [0.5, 0.75, 1.0])
def test_under_budget_respects_limit_and_sorts(max_cost):
    results = under_budget(max_cost)
    costs = [r.cost_per_serving for r in results]
    assert all(c <= max_cost for c in costs)
    assert costs == sorted(costs)


def test_total_cost_scales_with_servings():
    recipe = get_recipe("lentil-soup")
    assert recipe.total_cost(2) == 1.20


def test_total_cost_rejects_zero_servings():
    with pytest.raises(ValueError):
        get_recipe("oatmeal").total_cost(0)


def test_can_make_with_everything_on_hand():
    matches = dict((r.slug, m) for r, m in can_make(["oats", "banana", "milk", "cinnamon"]))
    assert matches["oatmeal"] == []


def test_format_recipe_numbers_every_step():
    recipe = get_recipe("egg-fried-rice")
    text = format_recipe(recipe)
    assert f"{len(recipe.steps)}. " in text


def test_every_recipe_has_steps_and_ingredients():
    for recipe in RECIPES:
        assert recipe.steps and recipe.ingredients
