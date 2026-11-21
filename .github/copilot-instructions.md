# Copilot Instructions

## Project
- Language: Python 3.12
- Describe the project here in one or two sentences (what it does, who it's for).

## Code style
- Follow PEP 8 and format with Black (line length 88).
- Use type hints on every function and method.
- Write a short docstring for every public function, class, and module.
- Prefer clear names over comments; comment only the why, not the what.
- Keep functions small and focused, under about 40 lines.
- Use f-strings for formatting and pathlib for file paths.

## Structure
- Source code lives in src/, tests in tests/.
- One responsibility per module; avoid circular imports.
- Put settings in a config module; read secrets from environment variables.

## Safety
- Never hardcode passwords, tokens, or API keys.
- Validate all user input and handle errors with specific exceptions, never a bare except.
- Only suggest packages that exist on PyPI and are widely used; say when one needs installing.

## Testing
- Write pytest tests for new or changed code.
- Cover the normal case, edge cases (empty, None, large input), and failures.
- Name tests test_<function>_<what_it_checks>.

## How to answer me
- For bigger tasks, give a short plan before writing code.
- Show complete, runnable code, not fragments, unless I ask for a snippet.
- Explain changes in plain language, briefly, after the code.
- If something is unclear, ask one question instead of guessing.
- When fixing a bug, say what caused it.
