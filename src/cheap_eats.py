"""Cheap Eats: simple, low-budget recipes with step-by-step cooking instructions.

Run it:
    python src/cheap_eats.py list
    python src/cheap_eats.py list --max-cost 1.00
    python src/cheap_eats.py show rice-and-beans --servings 2
    python src/cheap_eats.py have rice eggs onion

Costs are rough US grocery estimates per serving; check your own store's prices.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Recipe:
    """A budget recipe with ingredients, steps and an estimated cost."""

    slug: str
    name: str
    servings: int
    cost_per_serving: float
    minutes: int
    ingredients: tuple[str, ...]
    steps: tuple[str, ...]

    def total_cost(self, servings: int | None = None) -> float:
        """Return the estimated cost for the given number of servings."""
        count = self.servings if servings is None else servings
        if count < 1:
            raise ValueError("servings must be at least 1")
        return round(self.cost_per_serving * count, 2)


RECIPES: tuple[Recipe, ...] = (
    Recipe(
        slug="rice-and-beans",
        name="Rice and Beans",
        servings=4,
        cost_per_serving=0.75,
        minutes=30,
        ingredients=("rice", "canned beans", "onion", "oil", "salt", "cumin"),
        steps=(
            "Rinse 1 cup rice. Simmer it in 2 cups salted water, covered, for 18 minutes.",
            "Dice half an onion and cook it in 1 tbsp oil over medium heat for 5 minutes.",
            "Add 1 can beans with their liquid and 1 tsp cumin. Simmer 10 minutes.",
            "Serve the beans over the rice. Add hot sauce if you have it.",
        ),
    ),
    Recipe(
        slug="egg-fried-rice",
        name="Egg Fried Rice",
        servings=2,
        cost_per_serving=0.90,
        minutes=15,
        ingredients=("rice", "eggs", "frozen vegetables", "soy sauce", "oil"),
        steps=(
            "Use 2 cups cooked rice, ideally a day old so it fries instead of steams.",
            "Heat 1 tbsp oil on high. Scramble 2 eggs, then push them to one side.",
            "Add 1 cup frozen vegetables and cook 3 minutes.",
            "Add the rice and 2 tbsp soy sauce. Stir-fry 4 minutes until hot.",
        ),
    ),
    Recipe(
        slug="lentil-soup",
        name="Lentil Soup",
        servings=6,
        cost_per_serving=0.60,
        minutes=40,
        ingredients=("lentils", "onion", "carrots", "canned tomatoes", "oil", "salt"),
        steps=(
            "Dice 1 onion and 2 carrots. Cook in 1 tbsp oil for 6 minutes.",
            "Add 1 cup rinsed lentils, 1 can tomatoes and 6 cups water.",
            "Simmer 30 minutes until the lentils are soft. Salt to taste.",
            "Freezes well, so cook the full pot and save half.",
        ),
    ),
    Recipe(
        slug="potato-hash",
        name="Potato and Egg Hash",
        servings=2,
        cost_per_serving=1.10,
        minutes=25,
        ingredients=("potatoes", "eggs", "onion", "oil", "salt"),
        steps=(
            "Dice 2 potatoes small. Fry in 2 tbsp oil over medium heat for 12 minutes.",
            "Add half a diced onion and cook 5 more minutes until browned.",
            "Make 2 wells, crack an egg into each, cover and cook 4 minutes.",
            "Salt and pepper, then serve straight from the pan.",
        ),
    ),
    Recipe(
        slug="bean-burritos",
        name="Bean and Rice Burritos",
        servings=4,
        cost_per_serving=1.00,
        minutes=20,
        ingredients=("tortillas", "canned beans", "rice", "cheese", "salsa"),
        steps=(
            "Mash 1 can drained beans in a pan over medium heat with a splash of water.",
            "Warm 4 tortillas in a dry pan for 20 seconds per side.",
            "Fill each with beans, cooked rice, a little cheese and salsa.",
            "Roll tight. Wrap extras in foil and freeze for quick lunches.",
        ),
    ),
    Recipe(
        slug="oatmeal",
        name="Banana Oatmeal",
        servings=1,
        cost_per_serving=0.40,
        minutes=5,
        ingredients=("oats", "banana", "milk or water", "cinnamon"),
        steps=(
            "Bring 1 cup milk or water to a simmer.",
            "Stir in 1/2 cup oats and cook 3 minutes.",
            "Mash in half a banana and a pinch of cinnamon.",
        ),
    ),
)


def get_recipe(slug: str) -> Recipe:
    """Find a recipe by its slug, raising KeyError if it doesn't exist."""
    for recipe in RECIPES:
        if recipe.slug == slug:
            return recipe
    raise KeyError(f"No recipe named '{slug}'")


def under_budget(max_cost: float) -> list[Recipe]:
    """Return recipes at or under max_cost per serving, cheapest first."""
    return sorted(
        (r for r in RECIPES if r.cost_per_serving <= max_cost),
        key=lambda r: r.cost_per_serving,
    )


PANTRY = ("oil", "salt", "cumin", "cinnamon", "soy sauce")


def can_make(on_hand: list[str], max_missing: int = 2) -> list[tuple[Recipe, list[str]]]:
    """Return recipes missing at most max_missing ingredients, with what's missing.

    Basic pantry staples (oil, salt, spices, soy sauce) are assumed on hand.
    """
    have = {item.strip().lower() for item in on_hand} | set(PANTRY)
    matches = []
    for recipe in RECIPES:
        missing = [i for i in recipe.ingredients if not any(h in i for h in have)]
        if len(missing) <= max_missing:
            matches.append((recipe, missing))
    return sorted(matches, key=lambda pair: len(pair[1]))


def format_recipe(recipe: Recipe, servings: int | None = None) -> str:
    """Return a printable card for one recipe."""
    count = recipe.servings if servings is None else servings
    lines = [
        f"{recipe.name}  ({count} servings, about ${recipe.total_cost(count):.2f}, "
        f"{recipe.minutes} min)",
        "",
        "Ingredients: " + ", ".join(recipe.ingredients),
    ]
    if count != recipe.servings:
        lines.append(f"(Amounts are for {recipe.servings}; scale by {count / recipe.servings:g}x)")
    lines.append("")
    lines += [f"{n}. {step}" for n, step in enumerate(recipe.steps, start=1)]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description="Low-budget cooking instructions")
    sub = parser.add_subparsers(dest="command", required=True)
    list_cmd = sub.add_parser("list", help="list recipes, cheapest first")
    list_cmd.add_argument("--max-cost", type=float, default=99.0)
    show_cmd = sub.add_parser("show", help="show one recipe's steps")
    show_cmd.add_argument("slug")
    show_cmd.add_argument("--servings", type=int)
    have_cmd = sub.add_parser("have", help="what can I make with what I have?")
    have_cmd.add_argument("items", nargs="+")
    args = parser.parse_args(argv)

    if args.command == "list":
        for r in under_budget(args.max_cost):
            print(f"{r.slug:<16} ${r.cost_per_serving:.2f}/serving  {r.minutes} min  {r.name}")
    elif args.command == "show":
        print(format_recipe(get_recipe(args.slug), args.servings))
    else:
        matches = can_make(args.items)
        if not matches:
            print("Nothing close yet. Rice, beans or eggs unlock the most recipes.")
        for recipe, missing in matches:
            need = f" (need: {', '.join(missing)})" if missing else " (you have everything)"
            print(f"{recipe.slug:<16} {recipe.name}{need}")


if __name__ == "__main__":
    main()
