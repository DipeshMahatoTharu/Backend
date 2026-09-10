"""
============================================================
DAY 40 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Expression Tree Evaluator for Composite `Q` Filters

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement an evaluator `eval_q_tree(expression_dict: dict, record: dict) -> bool`
that evaluates nested logical boolean trees against a database record dictionary.

The expression tree supports:
- Direct conditions: `{"field": "price", "op": "lt", "val": 100}`
- Logical AND: `{"and": [expr1, expr2]}`
- Logical OR: `{"or": [expr1, expr2]}`
- Logical NOT: `{"not": expr}`

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Recursively evaluate nested clauses.
- Support operators: 'eq', 'gt', 'lt', 'contains'.

============================================================
MY APPROACH:
============================================================
1. If "and" in dict: return all(eval_q_tree(sub, record) for sub in dict["and"]).
2. If "or" in dict: return any(eval_q_tree(sub, record) for sub in dict["or"]).
3. If "not" in dict: return not eval_q_tree(dict["not"], record).
4. Otherwise evaluate leaf condition using field, op, and val.
"""
from typing import Dict, Any

def eval_q_tree(expr: Dict[str, Any], record: Dict[str, Any]) -> bool:
    if "and" in expr:
        return all(eval_q_tree(sub, record) for sub in expr["and"])
    if "or" in expr:
        return any(eval_q_tree(sub, record) for sub in expr["or"])
    if "not" in expr:
        return not eval_q_tree(expr["not"], record)

    # Leaf condition
    field = expr["field"]
    op = expr["op"]
    val = expr["val"]
    rec_val = record.get(field)

    if op == "eq":
        return rec_val == val
    elif op == "gt":
        return rec_val > val
    elif op == "lt":
        return rec_val < val
    elif op == "contains":
        return str(val).lower() in str(rec_val).lower()

    return False


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    # Expression: (status == 'active') AND (price < 50 OR category == 'books')
    tree = {
        "and": [
            {"field": "status", "op": "eq", "val": "active"},
            {
                "or": [
                    {"field": "price", "op": "lt", "val": 50},
                    {"field": "category", "op": "eq", "val": "books"}
                ]
            }
        ]
    }

    # Match: active and price < 50
    assert eval_q_tree(tree, {"status": "active", "price": 30, "category": "tech"}) is True

    # Match: active and category == 'books' (even if price >= 50)
    assert eval_q_tree(tree, {"status": "active", "price": 100, "category": "books"}) is True

    # No match: inactive
    assert eval_q_tree(tree, {"status": "inactive", "price": 20, "category": "books"}) is False

    print("Whiteboard Day 40 challenge passed successfully!")
