# Day 26 Practice — Git Workflows, Conflict Resolution & Repository Hygiene

import re

# =====================================================================
# TASK 1: Conventional Commit Message Linter
# =====================================================================
# In professional backend repositories, CI/CD pipelines reject commits
# that don't follow the Conventional Commits specification.
# Format: `<type>(<scope optional>): <description>`
# Valid types: feat, fix, docs, style, refactor, perf, test, chore
# Description must start with a lowercase letter and must not end with a period.
#
# INSTRUCTIONS:
# 1. Complete `lint_commit_message(msg: str) -> tuple[bool, str]`:
#    - If valid, return (True, "Valid commit message").
#    - If invalid, return (False, "<Specific error explanation>").

VALID_TYPES = {"feat", "fix", "docs", "style", "refactor", "perf", "test", "chore"}

def lint_commit_message(msg: str) -> tuple[bool, str]:
    # TODO: Implement validation against Conventional Commits specification
    pass


# =====================================================================
# TASK 2: Merge Conflict Marker Parser
# =====================================================================
# When a merge conflict occurs, Git writes conflict markers directly into the file:
# <<<<<<< HEAD
# <ours_content>
# =======
# <theirs_content>
# >>>>>>> branch_name
#
# INSTRUCTIONS:
# 1. Complete `extract_conflict_blocks(file_content: str) -> list[dict]`:
#    - Returns a list of dictionaries for every conflict in the file:
#      `[{"ours": str, "theirs": str, "branch": str}]`
#    - Strip trailing whitespaces/newlines from extracted blocks.

def extract_conflict_blocks(file_content: str) -> list[dict]:
    # TODO: Extract conflict blocks from file_content
    pass


# =====================================================================
# TASK 3: Automated Conflict Resolver (Strategy: "ours" vs "theirs")
# =====================================================================
# Often during deployments or hotfixes, an automated script needs to resolve
# conflicts by favoring one branch's changes.
#
# INSTRUCTIONS:
# 1. Complete `resolve_conflicts(file_content: str, strategy: str) -> str`:
#    - `strategy` must be either "ours" or "theirs".
#    - Replaces every conflict block with either the "ours" content or "theirs" content.
#    - Removes all Git conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

def resolve_conflicts(file_content: str, strategy: str = "ours") -> str:
    # TODO: Replace conflict markers with chosen branch's content
    pass


# =====================================================================
# TASK 4: Gitignore Pattern Matcher
# =====================================================================
# Build a simple pattern checker to verify if a sensitive file should be ignored.
#
# INSTRUCTIONS:
# 1. Complete `is_ignored(filename: str, ignore_patterns: list[str]) -> bool`:
#    - If filename matches an exact pattern (e.g. ".env"), return True.
#    - If filename ends with an extension wildcard (e.g. "*.pyc"), return True.
#    - If pattern is a directory (ends with "/"), and filename starts with that directory, return True.

def is_ignored(filename: str, ignore_patterns: list[str]) -> bool:
    # TODO: Implement ignore rule matching
    pass


# =====================================================================
# VERIFICATION SUITE
# =====================================================================
if __name__ == "__main__":
    print("--- Running Day 26 Practice Tasks ---")

    # Test Task 1
    c1, m1 = lint_commit_message("feat(auth): add jwt refresh token endpoint")
    c2, m2 = lint_commit_message("Fixed stuff.")
    print(f"Task 1 valid: {c1} - {m1}")
    print(f"Task 1 invalid: {c2} - {m2}")

    # Test Task 2 & 3
    sample_conflict = """# Backend Config
DEBUG = False
<<<<<<< HEAD
DATABASE_PORT = 5432
=======
DATABASE_PORT = 5433
>>>>>>> feature/docker-setup
SECRET_KEY = "xyz"
"""
    conflicts = extract_conflict_blocks(sample_conflict)
    print(f"Task 2 extracted conflicts count: {len(conflicts)}")
    if conflicts:
        print(f"Ours: {conflicts[0]['ours']}, Theirs: {conflicts[0]['theirs']}")

    resolved_ours = resolve_conflicts(sample_conflict, strategy="ours")
    print("Task 3 Resolved with 'ours':")
    print(resolved_ours.strip())

    # Test Task 4
    rules = [".env", "*.pyc", "__pycache__/", "*.sqlite3"]
    print(f"Task 4 (.env ignored): {is_ignored('.env', rules)}")
    print(f"Task 4 (app.pyc ignored): {is_ignored('app.pyc', rules)}")
    print(f"Task 4 (models.py ignored): {is_ignored('models.py', rules)}")