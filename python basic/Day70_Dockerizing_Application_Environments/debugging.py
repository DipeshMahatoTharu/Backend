"""
Day 57: Dockerizing Application Environments — Debugging
Diagnose and fix 3 critical Docker and containerization errors.
"""
from typing import List, Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Running as Root User Inside Container
# Problem: A Dockerfile did not define a USER directive.
# An attacker exploiting a file upload vulnerability gained root privileges!
# Fix: Create and switch to a non-privileged user.
# ---------------------------------------------------------------------
def get_dockerfile_user_directive(use_non_root: bool) -> str:
    # BUGGY VERSION:
    # return "" # Default root!

    # FIXED VERSION:
    if use_non_root:
        return "RUN useradd -u 1000 appuser\\nUSER appuser"
    return ""


# ---------------------------------------------------------------------
# Bug 2: Missing `.dockerignore` Leaking Virtual Environments and Secrets
# Problem: `COPY . /app` copied local `.env` with production keys and `venv/`
# with Windows DLLs into a Linux container, crashing Python!
# Fix: Ensure `.dockerignore` filters out local environments and secrets.
# ---------------------------------------------------------------------
def filter_dockerignore_entries(files_to_copy: List[str], ignored_patterns: set) -> List[str]:
    # BUGGY VERSION:
    # return files_to_copy

    # FIXED VERSION:
    return [f for f in files_to_copy if f not in ignored_patterns and not any(f.endswith(ext) for ext in [".pyc", ".env"])]


# ---------------------------------------------------------------------
# Bug 3: Ephemeral PostgreSQL Data Without Docker Volume
# Problem: When `docker compose down` was run, all production database tables
# and customer records disappeared!
# Fix: Mount PostgreSQL data to a named Docker volume.
# ---------------------------------------------------------------------
def validate_postgres_volume_mount(volumes: List[str]) -> bool:
    # BUGGY VERSION: Allowed containers without persistent volume mounts
    # return True

    # FIXED VERSION:
    return any("/var/lib/postgresql/data" in v for v in volumes)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    directive = get_dockerfile_user_directive(True)
    assert "USER appuser" in directive

    # Test Bug 2 fix
    all_files = ["manage.py", "app.py", ".env", "venv", "test.pyc"]
    copied = filter_dockerignore_entries(all_files, {"venv"})
    assert ".env" not in copied
    assert "venv" not in copied
    assert "test.pyc" not in copied
    assert "manage.py" in copied

    # Test Bug 3 fix
    assert validate_postgres_volume_mount(["pgdata:/var/lib/postgresql/data"]) is True
    assert validate_postgres_volume_mount(["/tmp:/tmp"]) is False

    print("All Day 57 debugging fixes verified successfully!")
