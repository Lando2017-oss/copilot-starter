---
description: Review Python code for bugs, security, and style
mode: ask
---

Review the code in ${selection} (or the whole of ${file} if nothing is selected). Follow the rules in .github/copilot-instructions.md.

Check for, in this order:
1. Bugs and logic errors, including edge cases (empty, None, very large input).
2. Security problems: hardcoded secrets, unsafe input handling, injection risks.
3. Error handling: bare excepts, swallowed errors, unclear messages.
4. Readability: unclear names, long functions, missing type hints or docstrings.
5. Missing or weak pytest tests.

Answer in this format:
- Summary: one or two sentences on overall quality.
- Issues: a numbered list, most serious first. For each give the line, what's wrong, why it matters, and the fixed code.
- Tests to add: test names with one line on what each checks.

Don't rewrite code that's already fine. If nothing is wrong in a category, say so in one line.
