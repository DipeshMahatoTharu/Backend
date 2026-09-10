"""
Day 57: Dockerizing Application Environments — Practice
Hands-on exercises covering Dockerfile linting, container readiness loops, and compose service mapping.
"""
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Task 1: Dockerfile Best-Practice Linter
# ---------------------------------------------------------------------
def lint_dockerfile(dockerfile_content: str) -> List[str]:
    """
    Inspects Dockerfile instructions and returns security and optimization warnings.
    """
    warnings = []
    lines = [line.strip() for line in dockerfile_content.splitlines() if line.strip() and not line.startswith("#")]

    has_user_directive = any(l.startswith("USER ") for l in lines)
    if not has_user_directive:
        warnings.append("SECURITY: Running as root! Add a non-root USER directive.")

    for l in lines:
        if "apt-get install" in l and "--no-install-recommends" not in l:
            warnings.append("OPTIMIZATION: apt-get install should include --no-install-recommends.")
        if "pip install" in l and "--no-cache-dir" not in l and "wheel" not in l:
            warnings.append("OPTIMIZATION: pip install should use --no-cache-dir to minimize image size.")

    return warnings


# ---------------------------------------------------------------------
# Task 2: Database Readiness Retry Loop Simulator
# ---------------------------------------------------------------------
def wait_for_database_ready(poll_fn, max_retries: int = 5, interval_seconds: float = 0.05) -> bool:
    """
    Simulates entrypoint.sh polling database readiness before running migrations.
    """
    for attempt in range(1, max_retries + 1):
        if poll_fn():
            return True
    return False


# ---------------------------------------------------------------------
# Task 3: Compose Service Dependency Graph Resolver
# ---------------------------------------------------------------------
def get_startup_order(services: Dict[str, List[str]]) -> List[str]:
    """
    Resolves startup order of Docker compose services based on dependencies.
    """
    ordered = []
    visited = set()

    def visit(service):
        if service in visited:
            return
        for dep in services.get(service, []):
            visit(dep)
        visited.add(service)
        ordered.append(service)

    for s in services:
        visit(s)

    return ordered


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 57 Practice Tests ---")

    # Test Task 1
    bad_df = """
    FROM python:3.11
    RUN apt-get update && apt-get install python3-dev
    RUN pip install -r requirements.txt
    CMD ["python", "manage.py", "runserver"]
    """
    warns = lint_dockerfile(bad_df)
    assert len(warns) == 3

    # Test Task 2
    attempts = [0]
    def mock_db_check():
        attempts[0] += 1
        return attempts[0] >= 3

    ready = wait_for_database_ready(mock_db_check, max_retries=5)
    assert ready is True
    assert attempts[0] == 3

    # Test Task 3
    compose_deps = {
        "web": ["db", "redis"],
        "celery": ["db", "redis"],
        "db": [],
        "redis": []
    }
    order = get_startup_order(compose_deps)
    assert order.index("db") < order.index("web")
    assert order.index("redis") < order.index("web")

    print("All Day 57 practice assertions passed successfully!")
