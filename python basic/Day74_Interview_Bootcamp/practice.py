"""
Day 59: Technical Interview Bootcamp — Practice
Rapid-fire coding interview challenges covering algorithms, data structures, and concurrency.
"""
from typing import List, Dict, Any, Optional, Tuple

# ---------------------------------------------------------------------
# Task 1: Find First Non-Repeating Character in a String (O(N) Time, O(1) Space)
# ---------------------------------------------------------------------
def first_unique_char(s: str) -> Optional[str]:
    counts: Dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in s:
        if counts[char] == 1:
            return char
    return None


# ---------------------------------------------------------------------
# Task 2: Merge Overlapping Intervals (Classic Scheduling Challenge)
# ---------------------------------------------------------------------
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    # Sort by start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]

    for current in sorted_intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:
            # Overlap: merge by expanding end time
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged


# ---------------------------------------------------------------------
# Task 3: In-Memory Two-Sum Algorithm (O(N) Time Complexity)
# ---------------------------------------------------------------------
def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen: Dict[int, int] = {}  # complement -> index
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], idx)
        seen[num] = idx
    return None


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 59 Practice Tests ---")

    # Test Task 1
    assert first_unique_char("swiss") == "w"
    assert first_unique_char("aabb") is None

    # Test Task 2
    raw = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merged = merge_intervals(raw)
    assert merged == [[1, 6], [8, 10], [15, 18]]

    # Test Task 3
    pair = two_sum([2, 7, 11, 15], 9)
    assert pair == (0, 1)

    print("All Day 59 practice assertions passed successfully!")
