"""
Day 40: Django ORM Queries — Practice
Hands-on exercises covering Q object logic, F expression simulation, and query lookups.
"""
from typing import Dict, Any, List, Callable

# ---------------------------------------------------------------------
# Task 1: Field Lookup Matcher
# ---------------------------------------------------------------------
def match_field_lookup(record_value: Any, lookup_expr: str, target_value: Any) -> bool:
    """
    Simulates Django field lookups:
    - 'exact': ==
    - 'iexact': case-insensitive string ==
    - 'contains': substring in string
    - 'icontains': case-insensitive substring
    - 'gt': >
    - 'gte': >=
    - 'lt': <
    - 'lte': <=
    - 'in': record_value in target_value list
    """
    if lookup_expr == "exact":
        return record_value == target_value
    elif lookup_expr == "iexact":
        return str(record_value).lower() == str(target_value).lower()
    elif lookup_expr == "contains":
        return str(target_value) in str(record_value)
    elif lookup_expr == "icontains":
        return str(target_value).lower() in str(record_value).lower()
    elif lookup_expr == "gt":
        return record_value > target_value
    elif lookup_expr == "gte":
        return record_value >= target_value
    elif lookup_expr == "lt":
        return record_value < target_value
    elif lookup_expr == "lte":
        return record_value <= target_value
    elif lookup_expr == "in":
        return record_value in target_value
    return False


# ---------------------------------------------------------------------
# Task 2: Q Object Simulator
# ---------------------------------------------------------------------
class Q:
    def __init__(self, **kwargs):
        self.conditions = kwargs
        self.negated = False
        self.children: List[Tuple[str, Q]] = []  # ('AND'/'OR', child_q)

    def __invert__(self):
        new_q = Q(**self.conditions)
        new_q.negated = not self.negated
        new_q.children = list(self.children)
        return new_q

    def __or__(self, other: 'Q') -> 'Q':
        combined = Q()
        combined.children = [("OR", self), ("OR", other)]
        return combined

    def __and__(self, other: 'Q') -> 'Q':
        combined = Q()
        combined.children = [("AND", self), ("AND", other)]
        return combined

    def evaluate(self, record: Dict[str, Any]) -> bool:
        if self.children:
            # Evaluate composite Q
            op = self.children[0][0]
            if op == "OR":
                res = any(child.evaluate(record) for _, child in self.children)
            else:
                res = all(child.evaluate(record) for _, child in self.children)
            return not res if self.negated else res

        # Evaluate direct conditions
        for k, v in self.conditions.items():
            parts = k.split("__")
            fname = parts[0]
            lookup = parts[1] if len(parts) > 1 else "exact"
            rec_val = record.get(fname)
            if not match_field_lookup(rec_val, lookup, v):
                return self.negated  # False (or True if negated)
        return not self.negated      # True (or False if negated)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 40 Practice Tests ---")

    # Test Task 1
    assert match_field_lookup("Django ORM", "icontains", "django") is True
    assert match_field_lookup(100, "gte", 100) is True
    assert match_field_lookup(100, "gt", 100) is False
    assert match_field_lookup("pending", "in", ["pending", "processing"]) is True

    # Test Task 2
    row1 = {"id": 1, "status": "active", "price": 45.0}
    row2 = {"id": 2, "status": "draft", "price": 10.0}

    q_active = Q(status="active")
    assert q_active.evaluate(row1) is True
    assert q_active.evaluate(row2) is False

    q_negated = ~Q(status="active")
    assert q_negated.evaluate(row1) is False
    assert q_negated.evaluate(row2) is True

    # OR query: status=='active' OR price < 15.0
    q_complex = Q(status="active") | Q(price__lt=15.0)
    assert q_complex.evaluate(row1) is True
    assert q_complex.evaluate(row2) is True
    assert q_complex.evaluate({"status": "archived", "price": 50.0}) is False

    print("All Day 40 practice assertions passed successfully!")
