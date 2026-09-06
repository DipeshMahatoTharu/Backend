# Day 26 — Git Collaboration & Conflict Resolution Questions

Write your answers in the designated spaces below each question.

---

### 26.1 `git merge` vs `git rebase`
**QUESTION:**
1. What is the fundamental difference between merging a feature branch into `main` vs rebasing that feature branch onto `main`?
2. What is the "Golden Rule of Rebasing"? Why should you never rebase commits that have already been pushed to a shared public branch?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 26.2 Reset Modes: `--soft` vs `--mixed` vs `--hard`
**QUESTION:**
Explain what happens to:
(a) the commit history (HEAD pointer)
(b) the Staging Area (Index)
(c) the Working Directory
when you run:
1. `git reset --soft HEAD~1`
2. `git reset --mixed HEAD~1` (default)
3. `git reset --hard HEAD~1`

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 26.3 Disaster Recovery with `git reflog`
**QUESTION:**
Suppose a developer ran `git reset --hard` by mistake and wiped out 3 commits containing critical backend code. How does `git reflog` track HEAD movements, and how can the developer recover those "lost" commits?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 26.4 Repository Hygiene & `.gitignore`
**QUESTION:**
1. Why must files like `.env`, `*.pyc`, `__pycache__/`, and `.sqlite3` always be in `.gitignore`?
2. If a developer accidentally committed and pushed a `.env` file, simply adding `.env` to `.gitignore` does not stop Git from tracking it. Why? What command removes it from tracking without deleting it from disk?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________

---

### 26.5 Conventional Commits Standard
**QUESTION:**
What is the Conventional Commits format (e.g. `feat:`, `fix:`, `refactor:`, `chore:`)? Why do enterprise backend repositories use commit linters to enforce this format in CI/CD pipelines?

**MY ANSWER:**
____________________________________________________
____________________________________________________
____________________________________________________