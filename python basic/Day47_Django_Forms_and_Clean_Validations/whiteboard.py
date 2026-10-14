"""
============================================================
DAY 43 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Multi-Field Schedule Validation with Conflict Detection

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a cross-field appointment validator function
`validate_appointment(existing_appointments: list, start_time: int, end_time: int) -> dict`
that:
1. Validates `start_time < end_time` (raises `ValueError("Start time must precede end time")`).
2. Validates appointment duration does not exceed 180 minutes (raises `ValueError("Duration exceeds maximum 180 minutes")`).
3. Detects schedule overlaps against existing appointments `[(start, end)]`:
   - Two intervals [A, B] and [C, D] overlap if `max(A, C) < min(B, D)`.
   - If an overlap exists, raise `ValueError("Time slot conflicts with an existing appointment")`.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return cleaned schedule dictionary: `{"start": start_time, "end": end_time, "duration": duration}`.

============================================================
MY APPROACH:
============================================================
1. Check start < end.
2. Check end - start <= 180.
3. Check overlap against each existing appointment interval.
4. Return validated dictionary.
"""
from typing import List, Tuple, Dict, Any

def validate_appointment(
    existing_appointments: List[Tuple[int, int]],
    start_time: int,
    end_time: int
) -> Dict[str, Any]:
    if start_time >= end_time:
        raise ValueError("Start time must precede end time.")

    duration = end_time - start_time
    if duration > 180:
        raise ValueError("Duration exceeds maximum 180 minutes.")

    # Overlap detection: max(start1, start2) < min(end1, end2)
    for exist_start, exist_end in existing_appointments:
        if max(start_time, exist_start) < min(end_time, exist_end):
            raise ValueError("Time slot conflicts with an existing appointment.")

    return {"start": start_time, "end": end_time, "duration": duration}


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    existing = [(60, 90), (120, 150)]  # In minutes from midnight

    # 1. Valid non-conflicting
    res = validate_appointment(existing, start_time=95, end_time=115)
    assert res["duration"] == 20

    # 2. Invalid start >= end
    try:
        validate_appointment(existing, 100, 90)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # 3. Exceeds max duration
    try:
        validate_appointment(existing, 200, 400)  # 200 mins
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    # 4. Overlaps with (60, 90)
    try:
        validate_appointment(existing, 80, 100)
        assert False, "Should raise ValueError on conflict"
    except ValueError:
        pass

    print("Whiteboard Day 43 challenge passed successfully!")
