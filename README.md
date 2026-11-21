# copilot-starter: Cheap Eats

A small Python app that gives step-by-step cooking instructions for meals that cost about $0.40 to $1.10 a serving. It also holds my GitHub Copilot setup (custom instructions plus /review and /tests prompt files).

## Run it

```bash
python src/cheap_eats.py list                    # all recipes, cheapest first
python src/cheap_eats.py list --max-cost 0.75    # only recipes under 75 cents a serving
python src/cheap_eats.py show lentil-soup        # full cooking steps
python src/cheap_eats.py show rice-and-beans --servings 2
python src/cheap_eats.py have rice eggs onion    # what can I make with what I have?
```

## Test it

```bash
pip install pytest
pytest
```

## Recipes

Banana Oatmeal, Lentil Soup, Rice and Beans, Egg Fried Rice, Bean and Rice Burritos, Potato and Egg Hash. Costs are rough US grocery estimates.

## Copilot setup

- `.github/copilot-instructions.md`: project rules Copilot follows (Python 3.12, Black, type hints, pytest)
- `.github/prompts/review.prompt.md`: type `/review` in Copilot Chat
- `.github/prompts/tests.prompt.md`: type `/tests` in Copilot Chat
