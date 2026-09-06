# Day 26 — Git Collaboration, Branching & Conflict Resolution

## 🎯 Learning Objectives
- Master professional Git branching workflows (feature branches, GitHub Flow, trunk-based development).
- Understand the mechanics of merge conflicts and how to resolve `<<<<<<< HEAD` markers safely.
- Learn the critical differences between `git merge` vs `git rebase`, and `git reset` vs `git revert`.
- Master repository hygiene: `.gitignore`, cleaning tracked files with `git rm --cached`, and writing Conventional Commits.
- Learn disaster recovery techniques in Git using `git reflog` and `git bisect`.

---

## 📚 Core Backend Concepts

### 1. Branching Workflows in Backend Teams
In professional engineering teams, developers never push directly to `main`. Every feature or bug fix lives on an isolated branch:
```bash
# Create and switch to a feature branch
git checkout -b feature/auth-jwt-refresh

# Pull latest main changes using rebase to maintain a linear history
git fetch origin
git rebase origin/main
```

### 2. Anatomy of a Merge Conflict
A conflict occurs when two branches modify the exact same lines of code:
```text
<<<<<<< HEAD (Current branch / main)
DATABASE_PORT = 5432
=======
DATABASE_PORT = 5433
>>>>>>> feature/auth-jwt-refresh (Incoming branch)
```
To resolve:
1. Open the file and decide which version is correct (or combine both).
2. Delete the markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Stage the resolved file: `git add <filename>`.
4. Finalize the merge or rebase: `git commit` or `git rebase --continue`.

### 3. Merge vs Rebase
- **`git merge`**: Preserves exact chronological commit history and creates a merge commit. Non-destructive, but creates messy "railroad track" commit histories in large teams.
- **`git rebase`**: Moves the entire feature branch to begin on the tip of `main`, resulting in a perfectly linear history. **Golden Rule of Rebase**: *Never rebase a public shared branch!*

### 4. Git Security & Hygiene: Secrets in Repositories
Never commit API keys, `.env` files, or database credentials.
If a secret is accidentally committed:
```bash
# Untrack without deleting the local file:
git rm --cached .env

# Commit the removal and add to .gitignore:
echo ".env" >> .gitignore
git add .gitignore
git commit -m "chore: stop tracking .env secret file"
```
*(Note: If pushed to public remote, the secret must be immediately rotated and revoked!)*

---

## 📅 Today's 3-Hour Structure

- **HOUR 1 — LEARN + CONCEPT DRILLS (60 min)**:
  - 40 min: Review Git workflows, rebase vs merge, and disaster recovery commands.
  - 20 min: Complete conceptual analysis in **[`questions.md`](file:///d:/Backend/python%20basic/Day26/questions.md)**.

- **HOUR 2 — CODING PRACTICE & DEBUGGING (60 min)**:
  - 35 min: Implement the Git simulation tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day26/practice.py)**.
  - 25 min: Diagnose real Git disasters in **[`debugging.py`](file:///d:/Backend/python%20basic/Day26/debugging.py)**.

- **HOUR 3 — INTERVIEW & PORTFOLIO CHALLENGE (60 min)**:
  - 20 min: Study production Git incident handling in **[`interview.md`](file:///d:/Backend/python%20basic/Day26/interview.md)**.
  - 20 min: Solve the merge conflict whiteboard walkthrough in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day26/whiteboard.py)**.
  - 20 min: Build the Conflict Resolution Simulator in **[`challenge.py`](file:///d:/Backend/python%20basic/Day26/challenge.py)**.

---

## 🏁 Completion Checklist
- [ ] Read concepts and answered **[`questions.md`](file:///d:/Backend/python%20basic/Day26/questions.md)**
- [ ] Completed all 4 tasks in **[`practice.py`](file:///d:/Backend/python%20basic/Day26/practice.py)**
- [ ] Fixed all 3 bug scenarios in **[`debugging.py`](file:///d:/Backend/python%20basic/Day26/debugging.py)**
- [ ] Solved conflict resolution challenge in **[`whiteboard.py`](file:///d:/Backend/python%20basic/Day26/whiteboard.py)**
- [ ] Built conflict parser in **[`challenge.py`](file:///d:/Backend/python%20basic/Day26/challenge.py)**
- [ ] Studied backend interview answers in **[`interview.md`](file:///d:/Backend/python%20basic/Day26/interview.md)**