"""
Day 39: Django Database Models — Debugging
Diagnose and fix 3 critical model design and migration traps.
"""
from typing import Dict, Any, Optional

# ---------------------------------------------------------------------
# Bug 1: `auto_now` vs `auto_now_add` on Manual Backfills
# Problem: An engineer migrating historical user records found that setting
# `created_at = models.DateTimeField(auto_now_add=True)` overrode their historical
# timestamps with the current timestamp upon `.save()`.
# Fix: Allow custom timestamp assignment when provided.
# ---------------------------------------------------------------------
import datetime

class AuditedRecord:
    def __init__(self, created_at: Optional[datetime.datetime] = None):
        # BUGGY VERSION:
        # self.created_at = datetime.datetime.now(datetime.timezone.utc) # Always overwrites!

        # FIXED VERSION:
        # If explicitly passed (e.g. historical migration), preserve it; otherwise set now
        self.created_at = created_at or datetime.datetime.now(datetime.timezone.utc)


# ---------------------------------------------------------------------
# Bug 2: `null=True` on CharField Causing Duplicate Empty Records
# Problem: A model has `email = models.CharField(max_length=255, null=True, blank=True, unique=True)`.
# In PostgreSQL, multiple rows with `NULL` are allowed in a unique column,
# but multiple rows with `""` raise IntegrityError!
# Fix: Ensure empty submissions save as NULL rather than empty string.
# ---------------------------------------------------------------------
def sanitize_unique_string(value: Optional[str]) -> Optional[str]:
    # BUGGY VERSION:
    # return value or "" # Saves "" which collides with existing "" rows!

    # FIXED VERSION:
    if not value or value.strip() == "":
        return None  # NULL in SQL allows multiple unique entries in PostgreSQL
    return value.strip()


# ---------------------------------------------------------------------
# Bug 3: Mutating Field Defaults In-Place (Mutable Default Bug)
# Problem: An engineer wrote `metadata = models.JSONField(default={})`.
# In Python, the default dictionary `{}` is shared across all model instances!
# Fix: Use a callable default (e.g. `default=dict`).
# ---------------------------------------------------------------------
class UserSettings:
    # BUGGY VERSION:
    # default_dict = {}
    # def __init__(self, preferences=default_dict): ...

    # FIXED VERSION:
    def __init__(self, preferences: Optional[Dict[str, Any]] = None):
        # Fresh dictionary per instance
        self.preferences = dict(preferences) if preferences is not None else {}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    past_time = datetime.datetime(2020, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    rec = AuditedRecord(created_at=past_time)
    assert rec.created_at == past_time

    # Test Bug 2 fix
    assert sanitize_unique_string("") is None
    assert sanitize_unique_string("  ") is None
    assert sanitize_unique_string("dipesh@example.com") == "dipesh@example.com"

    # Test Bug 3 fix
    s1 = UserSettings()
    s2 = UserSettings()
    s1.preferences["dark_mode"] = True
    assert "dark_mode" not in s2.preferences  # Isolated!

    print("All Day 39 debugging fixes verified successfully!")
