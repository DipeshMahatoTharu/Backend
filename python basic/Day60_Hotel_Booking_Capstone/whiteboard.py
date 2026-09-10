"""
============================================================
DAY 60 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Hotel Room Scheduling & Overlap Conflict Detector

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement `find_room_conflicts(existing_reservations: list, candidate_check_in: int, candidate_check_out: int) -> list`
where dates are represented as integers (day of year: 1 to 365).

Input:
existing_reservations = [
    {"room_id": 101, "check_in": 10, "check_out": 15},
    {"room_id": 102, "check_in": 12, "check_out": 20},
    {"room_id": 101, "check_in": 25, "check_out": 30}
]

Candidate stay: check_in = 14, check_out = 18.

Output:
Returns a list of `room_id`s that have conflicts with the candidate interval.
Room 101 has conflict with stay 10-15 (since 14 < 15 and 18 > 10).
Room 102 has conflict with stay 12-20 (since 14 < 20 and 18 > 12).
Output: `[101, 102]`

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Distinct sorted list of conflicting room IDs.
- Follow hotel semantics: checkout day == checkin day does not conflict.

============================================================
MY APPROACH:
============================================================
1. Iterate over reservations.
2. For each, check overlap: `candidate_in < res_out and candidate_out > res_in`.
3. Collect matching `room_id`s into a set.
4. Return sorted list.
"""
from typing import List, Dict, Any

def find_room_conflicts(
    existing_reservations: List[Dict[str, Any]],
    candidate_check_in: int,
    candidate_check_out: int
) -> List[int]:
    conflicting_rooms = set()

    for res in existing_reservations:
        res_in = res["check_in"]
        res_out = res["check_out"]

        # Overlap rule: start1 < end2 and end1 > start2
        if candidate_check_in < res_out and candidate_check_out > res_in:
            conflicting_rooms.add(res["room_id"])

    return sorted(list(conflicting_rooms))


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    reservations = [
        {"room_id": 101, "check_in": 10, "check_out": 15},
        {"room_id": 102, "check_in": 12, "check_out": 20},
        {"room_id": 101, "check_in": 25, "check_out": 30},
        {"room_id": 103, "check_in": 15, "check_out": 18}  # Starts exactly when candidate stay ends -> No conflict!
    ]

    # Candidate: [14, 18]
    conflicts = find_room_conflicts(reservations, candidate_check_in=14, candidate_check_out=15)
    assert conflicts == [101, 102]

    # Candidate: [15, 20] (Room 101 checked out on day 15, so 101 is NOT conflicted)
    conflicts_turnover = find_room_conflicts(reservations, candidate_check_in=15, candidate_check_out=20)
    assert 101 not in conflicts_turnover
    assert 102 in conflicts_turnover
    assert 103 in conflicts_turnover

    print("Whiteboard Day 60 challenge passed successfully!")
