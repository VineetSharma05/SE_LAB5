| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Mutable default arg** | Bug (Pylint) | 7 | `logs=[]` is a mutable default. It gets shared across all calls to `addItem`. | Change the default to `None` and initialize `logs = []` inside the function if it's `None`. |
| **Broad exception** | Bug (Pylint) | 16 | `except:` catches all possible exceptions, which is bad practice and can hide bugs. | Change `except:` to the specific `except KeyError:` to only catch errors when the item isn't in the dictionary. |
| **Use of `eval`** | Security (Bandit) | 57 | `eval()` is a high-severity security risk because it can run arbitrary code. | Remove the entire line: `eval("print('eval used')")`. |
| **Unsafe file handling** | Bug (Pylint) | 24, 29 | `open()` is used without `with`. If an error happens, `f.close()` might not be called, causing a resource leak. | Rewrite `loadData` and `saveData` to use the `with open(...) as f:` syntax, which handles closing the file automatically. |
| **Unused import** | Style (Flake8) | 2 | `import logging` is present, but the `logging` module is never actually used in the code. | Remove the entire line `import logging` to clean up the code. |

1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest: Definitely deleting the eval() line. Bandit said it was bad, and it wasn't needed, so it was just one click.
Hardest: The mutable default argument (logs=[]). It's a weird Python-specific quirk that doesn't look like a bug. I had to stop and think about why it was sharing the same list before I remembered the right fix (None-as-default).

2. Did the static analysis tools report any false positives? If so, describe one example.

No, not really. Everything it flagged was a real issue. The closest thing was Pylint complaining about "Missing module docstring" on such a small script. It felt like annoying noise when I was focused on bugs, but it's not wrong—good code should always have comments.

3. How would you integrate static analysis tools into your actual software development workflow?

I'd use them in two places:
One I would locally set up a "pre-commit hook." This would automatically run Flake8 before Git even lets me make a commit, catching silly mistakes fast.
Other in Cloud I'd use GitHub Actions to run the full set (Pylint, Bandit, Flake8) on every pull request. This is like the final checkpoint to make sure no bad code gets merged into the main branch.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code is hugely improved:
It's Safer: Removing eval() closed a major security hole.
It's More Stable: Fixing the except: and logs=[] bugs means the program won't crash unexpectedly or behave strangely.
It's Actually Readable: Before, it was a mystery. Now, with proper function names and docstrings, anyone (including my future self) can understand what the code is supposed to do.