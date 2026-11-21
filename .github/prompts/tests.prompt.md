---
description: Write pytest tests for the selected Python code
mode: edit
---

Write pytest tests for ${selection} (or every public function in ${file} if nothing is selected). Follow the rules in .github/copilot-instructions.md.

Requirements:
1. Put the tests in tests/test_<module name>.py, creating it if needed.
2. For each function, cover the normal case, edge cases (empty, None, zero, very large input), and expected errors with pytest.raises.
3. Use pytest.mark.parametrize when several inputs test the same behavior.
4. Use fixtures for shared setup, and tmp_path for files. Mock network calls, databases, and the clock; never hit real services.
5. Name tests test_<function>_<what_it_checks>, with a one-line docstring each.
6. Keep each test focused on one behavior.

After the code, list anything you couldn't test and why, and any bug the tests suggest in the original code.
