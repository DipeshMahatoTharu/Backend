"""
============================================================
DAY 42 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Optimistic Locking with Version Fields

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement an optimistic concurrency lock updater `update_record_optimistic(db_table: dict, record_id: int, new_data: dict, current_version: int) -> bool`
that prevents two users from overwriting each other's edits simultaneously.

The record schema is: `{"id": 1, "title": "...", "version": 1}`.
When updating:
- The update succeeds only if the in-database record's `version` equals `current_version`.
- If it matches, update fields, increment `version` by 1, and return `True`.
- If it does not match (someone else updated first), raise `StaleObjectError`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Simulate atomic DB update: `UPDATE table SET title = ..., version = version + 1 WHERE id = 1 AND version = 1;`
- Raise custom `StaleObjectError` on version mismatch.

============================================================
MY APPROACH:
============================================================
1. Look up record by `record_id`.
2. Compare `record["version"]` with `current_version`.
3. If mismatch, raise `StaleObjectError`.
4. Update dictionary values, increment `version`, and return True.
"""
from typing import Dict, Any

class StaleObjectError(Exception):
    pass

def update_record_optimistic(
    db_table: Dict[int, Dict[str, Any]],
    record_id: int,
    new_data: Dict[str, Any],
    current_version: int
) -> bool:
    if record_id not in db_table:
        raise KeyError(f"Record {record_id} does not exist.")

    record = db_table[record_id]

    if record["version"] != current_version:
        raise StaleObjectError(
            f"Record #{record_id} was modified by another transaction. "
            f"Expected version {current_version}, found version {record['version']}."
        )

    # Apply updates and increment version
    for k, v in new_data.items():
        if k not in ("id", "version"):
            record[k] = v

    record["version"] += 1
    return True


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    db = {
        1: {"id": 1, "title": "Original Title", "version": 1}
    }

    # User A reads record version 1
    # User B reads record version 1

    # User A updates successfully
    res_a = update_record_optimistic(db, 1, {"title": "User A Title"}, current_version=1)
    assert res_a is True
    assert db[1]["title"] == "User A Title"
    assert db[1]["version"] == 2

    # User B attempts update with stale version 1
    try:
        update_record_optimistic(db, 1, {"title": "User B Title"}, current_version=1)
        assert False, "Should raise StaleObjectError"
    except StaleObjectError:
        pass

    # Record was NOT overwritten by User B
    assert db[1]["title"] == "User A Title"

    print("Whiteboard Day 42 challenge passed successfully!")
