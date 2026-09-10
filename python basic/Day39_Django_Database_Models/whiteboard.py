"""
============================================================
DAY 39 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Migration Dependency Graph & Topological Execution Order

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Django migrations form a Directed Acyclic Graph (DAG) where migration B may depend on migration A.
Implement a topological sort function `resolve_migration_order(dependencies: dict) -> list`
that calculates the safe, deterministic execution order for applying database migrations.

Input:
{
    "auth_0002": ["auth_0001"],
    "auth_0001": [],
    "shop_0001": ["auth_0001"],
    "shop_0002": ["shop_0001", "auth_0002"]
}

Output:
A valid linear order, e.g. ["auth_0001", "auth_0002", "shop_0001", "shop_0002"]

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Detect circular dependencies and raise `ValueError("Circular dependency detected")`.
- Every migration must appear after all migrations listed in its dependency array.

============================================================
MY APPROACH:
============================================================
1. Kahn's Algorithm (in-degree resolution) or DFS cycle detection.
2. Build an adjacency graph and calculate in-degree (number of unmet prerequisites).
3. Enqueue migrations with in-degree 0.
4. Process queue, append to execution order, decrement prerequisite counts for dependents.
5. If processed count < total migrations, a cycle exists.
"""
from typing import Dict, List
from collections import deque, defaultdict

def resolve_migration_order(dependencies: Dict[str, List[str]]) -> List[str]:
    # Invert to: dependency -> list of migrations waiting on it
    dependents = defaultdict(list)
    in_degree = {mig: 0 for mig in dependencies}

    for mig, prereqs in dependencies.items():
        in_degree[mig] = len(prereqs)
        for prereq in prereqs:
            dependents[prereq].append(mig)

    queue = deque([m for m, deg in in_degree.items() if deg == 0])
    execution_order = []

    while queue:
        curr = queue.popleft()
        execution_order.append(curr)

        for dependent in dependents[curr]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    if len(execution_order) != len(dependencies):
        raise ValueError("Circular dependency detected")

    return execution_order


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    deps = {
        "auth_0002": ["auth_0001"],
        "auth_0001": [],
        "shop_0001": ["auth_0001"],
        "shop_0002": ["shop_0001", "auth_0002"]
    }

    order = resolve_migration_order(deps)
    assert order.index("auth_0001") < order.index("auth_0002")
    assert order.index("auth_0001") < order.index("shop_0001")
    assert order.index("shop_0001") < order.index("shop_0002")
    assert order.index("auth_0002") < order.index("shop_0002")

    # Cycle test
    cycle_deps = {
        "A": ["B"],
        "B": ["A"]
    }
    try:
        resolve_migration_order(cycle_deps)
        assert False, "Should raise ValueError on circular dependency"
    except ValueError:
        pass

    print("Whiteboard Day 39 challenge passed successfully!")
