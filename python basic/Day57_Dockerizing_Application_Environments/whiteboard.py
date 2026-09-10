"""
============================================================
DAY 57 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Multi-Container Dependency Startup DAG & Healthcheck Loop

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
In Docker Compose, services depend on one another:
`dependencies = {"web": ["db", "redis"], "db": [], "redis": []}`

Implement `simulate_compose_startup(dependencies: dict, health_status: dict) -> list`
that:
1. Returns a valid linear startup order using topological sorting.
2. If all dependencies of a service are healthy, the service starts.
3. If a circular dependency exists, raise `ValueError("Circular dependency detected")`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Pure Python without external packages.

============================================================
MY APPROACH:
============================================================
1. Kahn's algorithm or DFS topological sort.
2. Build in-degree map based on dependency counts.
3. Queue services with 0 dependencies, process and append to startup sequence.
"""
from typing import Dict, List
from collections import deque, defaultdict

def simulate_compose_startup(dependencies: Dict[str, List[str]], health_status: Dict[str, bool]) -> List[str]:
    # Check if any dependencies are unhealthy
    for svc, deps in dependencies.items():
        for dep in deps:
            if not health_status.get(dep, False):
                raise RuntimeError(f"Cannot start '{svc}': dependency '{dep}' is unhealthy!")

    # Topological Sort
    in_degree = {s: len(deps) for s, deps in dependencies.items()}
    dependents = defaultdict(list)
    for s, deps in dependencies.items():
        for dep in deps:
            dependents[dep].append(s)

    queue = deque([s for s, deg in in_degree.items() if deg == 0])
    startup_order = []

    while queue:
        curr = queue.popleft()
        startup_order.append(curr)

        for dep_svc in dependents[curr]:
            in_degree[dep_svc] -= 1
            if in_degree[dep_svc] == 0:
                queue.append(dep_svc)

    if len(startup_order) != len(dependencies):
        raise ValueError("Circular dependency detected")

    return startup_order


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    deps = {
        "web": ["db", "redis"],
        "worker": ["db", "redis"],
        "db": [],
        "redis": []
    }
    health = {"db": True, "redis": True, "web": True, "worker": True}

    order = simulate_compose_startup(deps, health)
    assert order.index("db") < order.index("web")
    assert order.index("redis") < order.index("web")
    assert order.index("db") < order.index("worker")

    # Unhealthy dependency case
    try:
        simulate_compose_startup(deps, {"db": False, "redis": True})
        assert False, "Should raise RuntimeError"
    except RuntimeError:
        pass

    # Circular dependency case
    try:
        simulate_compose_startup({"A": ["B"], "B": ["A"]}, {"A": True, "B": True})
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    print("Whiteboard Day 57 challenge passed successfully!")
