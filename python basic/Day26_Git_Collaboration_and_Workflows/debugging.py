# Day 26 Debugging — Git Disasters, Leaked Secrets & Conflict Bugs

# =====================================================================
# BUGGY SCENARIO 1: Merge Conflict Markers Left in Source Code
# =====================================================================
# Goal: Run the production application entry point.
# Problem: A developer accepted both changes during a merge conflict
# but forgot to delete the Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
# When Python runs this file, it immediately crashes with:
# `SyntaxError: invalid syntax` on the first marker line.

"""
def get_database_url():
<<<<<<< HEAD
    return "postgresql://postgres:pass@localhost:5432/main_db"
=======
    return "postgresql://postgres:pass@db-cluster.internal:5432/main_db"
>>>>>>> feature/cloud-db
"""

# ---------------------------------------------------------------------
# QUESTION: Why do conflict markers cause instant syntax crashes in Python?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Write clean, syntactically valid Python code that chooses the cloud database URL.
# ---------------------------------------------------------------------
def fixed_get_database_url() -> str:
    pass


# =====================================================================
# BUGGY SCENARIO 2: Committing Sensitive Production Secrets (.env)
# =====================================================================
# Problem: A developer added an `.env` file containing live Stripe and
# database credentials, staged it with `git add .`, committed it, and
# pushed it to a public GitHub repository.
# Realizing their mistake, they added `.env` to `.gitignore`.
# However, Git continues tracking `.env` on every subsequent commit!

# ---------------------------------------------------------------------
# QUESTION: Why does adding a file to .gitignore AFTER it has been committed
# fail to stop Git from tracking it?
#
# MY ANSWER:
# _____________________________________________________________________
#
# COMMAND SEQUENCE TO RESOLVE:
# Write the exact Git terminal commands required to:
# 1. Stop tracking .env without deleting the developer's local copy.
# 2. Commit the removal.
# 3. What security step MUST be performed with the leaked credentials immediately?
#
# 1. git ...
# 2. git ...
# 3. Security action: ...
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 3: The Accidental 'git reset --hard' Loss
# =====================================================================
# Problem: A developer meant to unstage files, but accidentally typed:
# `git reset --hard HEAD~2`
# Two days of committed backend work disappeared from `git log`!
# The developer is in panic thinking the code is destroyed permanently.

# ---------------------------------------------------------------------
# QUESTION: Is the code permanently lost? How does Git's internal garbage
# collection and `git reflog` mechanism protect committed snapshots?
#
# MY ANSWER:
# _____________________________________________________________________
#
# COMMAND SEQUENCE TO RESTORE:
# Write the exact Git commands to inspect the reflog and restore HEAD
# to the lost commit:
# 1. git ...
# 2. git ...
# ---------------------------------------------------------------------