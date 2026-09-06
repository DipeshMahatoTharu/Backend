"""
============================================================
DAY 26 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

TOPIC: Git Conflict Resolution & Branching Strategy Walkthrough

In technical interviews for backend roles, interviewers frequently ask
candidates to write out the exact terminal commands and steps to handle
a multi-file merge conflict, undo an accidental bad push, and deploy
safely without breaking production.

------------------------------------------------------------
1. SCENARIO STATEMENT:
------------------------------------------------------------
You are working on a feature branch named `feature/stripe-webhooks`.
Your teammate has just merged an urgent hotfix into `main`.
When you attempt to merge `main` into your feature branch before
opening your pull request:
  `git merge origin/main`
Git outputs:
  Auto-merging backend/settings.py
  CONFLICT (content): Merge conflict in backend/settings.py
  Auto-merging backend/payments/views.py
  CONFLICT (content): Merge conflict in backend/payments/views.py
  Automatic merge failed; fix conflicts and then commit the result.

------------------------------------------------------------
2. TASK & REQUIREMENTS:
------------------------------------------------------------
Without looking up documentation, write down the complete, step-by-step
procedure including the exact CLI commands and manual actions to:
1. Inspect which files are in conflict.
2. Examine the conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`).
3. Resolve the conflict safely.
4. Stage and commit the resolved files.
5. Verify the commit history is clean before pushing.
6. What command would you use if everything goes wrong and you want to abort the merge?

============================================================
MY STEP-BY-STEP PROCEDURE & COMMANDS:
============================================================
Write your complete walkthrough below:

Step 1: Check repository status and identify conflicting files
Command: ___________________________________________________

Step 2: Abort command (if you need to safely cancel and start over)
Command: ___________________________________________________

Step 3: Resolve conflicts inside files
Action explanation: _________________________________________
____________________________________________________________

Step 4: Mark resolved files as staged
Command: ___________________________________________________

Step 5: Finalize the merge commit
Command: ___________________________________________________

Step 6: Verify clean working directory and test suite pass
Command: ___________________________________________________

Step 7: Push the updated branch to remote
Command: ___________________________________________________

============================================================
BONUS WHITEBOARD QUESTION:
============================================================
If your team's policy requires a linear Git history (no merge commits),
what command would you have used instead of `git merge origin/main`?
How does resolving conflicts during a rebase differ from resolving
conflicts during a merge?

Explanation & Commands:
____________________________________________________________
____________________________________________________________
____________________________________________________________

"""