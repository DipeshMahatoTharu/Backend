"""
Day 41: Django Relationships & Prefetching — Debugging
Diagnose and fix 3 common database relationship flaws and N+1 performance bugs.
"""
from typing import List, Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Dangerous CASCADE Deleting Financial Records
# Problem: Deleting a inactive user triggered cascade deletion of all historical
# invoices, corrupting tax records.
# Fix: Enforce PROTECT or SET_NULL.
# ---------------------------------------------------------------------
class ProtectedError(Exception):
    pass

def delete_user_account(user_id: int, invoices: List[Dict[str, Any]], policy: str = "CASCADE") -> bool:
    user_invoices = [inv for inv in invoices if inv.get("user_id") == user_id]

    # BUGGY VERSION:
    # if policy == 'CASCADE':
    #     invoices.clear() # Deleted invoices!

    # FIXED VERSION:
    if policy == "PROTECT" and user_invoices:
        raise ProtectedError(f"Cannot delete user {user_id}: active invoices exist.")
    return True


# ---------------------------------------------------------------------
# Bug 2: Missing `related_name` Collision
# Problem: Two foreign keys on the same model pointing to User (author and editor)
# collide if related_name is not explicitly set.
# Fix: Provide distinct, meaningful related names.
# ---------------------------------------------------------------------
class ArticleFieldConfig:
    def __init__(self, author_related: str, editor_related: str):
        # BUGGY VERSION:
        # if author_related == editor_related: allowed...

        # FIXED VERSION:
        if author_related == editor_related:
            raise ValueError(f"Reverse accessor collision: both fields use '{author_related}'.")
        self.author_related = author_related
        self.editor_related = editor_related


# ---------------------------------------------------------------------
# Bug 3: Using `select_related` on Many-to-Many Relationships
# Problem: Passing a ManyToMany field to `select_related()` raises:
# "Invalid field name(s) given in select_related: 'tags'. Choices are: (none)"
# Fix: Redirect ManyToMany fields to `prefetch_related()`.
# ---------------------------------------------------------------------
def optimize_query_plan(field_name: str, is_many_to_many: bool) -> str:
    # BUGGY VERSION:
    # return "select_related"

    # FIXED VERSION:
    if is_many_to_many:
        return "prefetch_related"
    return "select_related"


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    invs = [{"id": 1, "user_id": 42, "amount": 500.0}]
    try:
        delete_user_account(42, invs, policy="PROTECT")
        assert False, "Should raise ProtectedError"
    except ProtectedError:
        pass

    # Test Bug 2 fix
    try:
        ArticleFieldConfig("articles", "articles")
        assert False, "Should raise ValueError on collision"
    except ValueError:
        pass
    cfg = ArticleFieldConfig("authored_articles", "edited_articles")
    assert cfg.author_related == "authored_articles"

    # Test Bug 3 fix
    assert optimize_query_plan("author", is_many_to_many=False) == "select_related"
    assert optimize_query_plan("tags", is_many_to_many=True) == "prefetch_related"

    print("All Day 41 debugging fixes verified successfully!")
