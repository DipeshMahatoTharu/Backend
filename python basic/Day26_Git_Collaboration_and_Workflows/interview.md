# Day 26 — Real-World Backend Engineering Interview

These questions test your understanding of version control incident response, enterprise team collaboration workflows, and debugging production regressions.

---

### Question 1: Handling Leaked Production Credentials in Git
**Interview Scenario:**
> *"A developer on your team accidentally committed a `.env` file containing live production database credentials and an AWS secret key to a public GitHub repository. They quickly push a new commit deleting the `.env` file. Is the issue resolved? What exact protocol must the team follow?"*

#### Senior Mentor Answer & Key Points:
1. **The Critical Mistake**:
   - Deleting the file in a new commit does **NOT** remove it from Git history! Anyone can inspect previous commits in the repository history (`git checkout HEAD~1` or view commit diffs on GitHub) and extract the raw credentials.
   - GitHub scrapers and automated bots index newly pushed public commits in sub-second time.
2. **Immediate Protocol**:
   - **Step 1: Revoke & Rotate Immediately**: Assume the secret is compromised. Immediately invalidate the database password and AWS secret key in AWS IAM / database console and rotate new ones. This is the only guaranteed security mitigation.
   - **Step 2: Scrub Git History**:
     * Use tools like `git-filter-repo` or BFG Repo-Cleaner to permanently purge the `.env` file from the entire commit tree history:
       `git filter-repo --invert-paths --path .env`
     * Force-push the rewritten history: `git push origin --force --all`.
   - **Step 3: Invalidate GitHub Caches**: Contact GitHub support to clear dangling cached commit views if the repo is public.
   - **Step 4: Prevention**: Implement pre-commit hooks (e.g. `detect-secrets`, `gitleaks`) that scan diffs and abort commits if entropy matches API keys or passwords.

---

### Question 2: Merge Strategies: Squash vs Rebase vs Merge Commit
**Interview Scenario:**
> *"When merging pull requests into `main`, what are the trade-offs between 'Create a merge commit', 'Squash and merge', and 'Rebase and merge'?"*

#### Senior Mentor Answer & Key Points:
1. **Squash and Merge**:
   - Combines all commits from the feature branch into a single commit on `main`.
   - **Pros**: Keeps `main`'s git log clean, concise, and easy to revert (1 commit = 1 complete feature).
   - **Cons**: Erases granular commit history and intermediate debugging context from the feature branch. Best for short-lived feature branches.
2. **Rebase and Merge**:
   - Replays individual commits from the branch on top of `main` without creating a merge commit.
   - **Pros**: Perfectly linear history; preserves individual commit descriptions.
   - **Cons**: If a branch has 20 messy WIP commits ("fixed typo", "wip"), all 20 clutter the main history.
3. **Merge Commit (`git merge --no-ff`)**:
   - Creates a 2-parent merge commit tying the branch to `main`.
   - **Pros**: Complete fidelity of who merged what and when; easy to see branch topology in visual graphs.
   - **Cons**: Cluttered graph ("railroad tracks") in large teams with dozens of concurrent branches.

---

### Question 3: Pinpointing Production Regressions with `git bisect`
**Interview Scenario:**
> *"A critical regression was discovered in production. You know the app worked fine at tag `v2.4.0` (100 commits ago), but is broken on `main`. How would you find the offending commit quickly without testing 100 commits manually?"*

#### Senior Mentor Answer & Key Points:
1. **The Power of Binary Search**:
   - `git bisect` performs a binary search through the commit history. For 100 commits, it finds the bug in at most `log2(100) ≈ 7` checks.
2. **Execution Steps**:
   ```bash
   # Start the bisect session
   git bisect start

   # Mark current state as broken
   git bisect bad

   # Mark the known good commit
   git bisect good v2.4.0

   # Git automatically checks out the midpoint commit (~commit 50)
   # Run your test suite:
   pytest tests/test_payment.py

   # If it passes:
   git bisect good
   # If it fails:
   git bisect bad

   # Repeat until Git outputs: "<commit hash> is the first bad commit"
   # Reset back to your original branch:
   git bisect reset
   ```
3. **Automated Bisect**:
   - If you have an automated test script, you can run: `git bisect run pytest tests/test_payment.py`, and Git will run the entire binary search automatically in seconds!