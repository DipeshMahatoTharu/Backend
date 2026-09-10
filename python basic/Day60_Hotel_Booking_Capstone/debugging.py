"""
Day 60: Hotel Booking Capstone — Debugging
Diagnose and fix 3 critical reservation and booking system bugs.
"""
from datetime import date
from typing import Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Off-by-One Turnover Error in Date Overlap
# Problem: A developer used `<= and >=` for interval check. This blocked a new guest
# from checking in on the same day the previous guest checked out!
# Fix: Use `< and >` to allow same-day turnover.
# ---------------------------------------------------------------------
def check_overlap_safe(start1: date, end1: date, start2: date, end2: date) -> bool:
    # BUGGY VERSION:
    # return start1 <= end2 and end1 >= start2 # Blocked same-day turnover!

    # FIXED VERSION:
    return start1 < end2 and end1 > start2


# ---------------------------------------------------------------------
# Bug 2: Missing Validation on Checkout Before Check-in
# Problem: A client passed check_in=2026-10-05 and check_out=2026-10-01.
# The calculation did `(1 - 5) = -4 nights`, resulting in negative billings!
# Fix: Validate check_in < check_out.
# ---------------------------------------------------------------------
def validate_booking_dates(check_in: date, check_out: date) -> int:
    # BUGGY VERSION:
    # return (check_out - check_in).days # Can be negative!

    # FIXED VERSION:
    if check_out <= check_in:
        raise ValueError("Check-out date must be strictly after check-in date.")
    return (check_out - check_in).days


# ---------------------------------------------------------------------
# Bug 3: Double Refund on Multiple Cancellation Requests
# Problem: A user double-clicked 'Cancel Reservation'. Both requests processed,
# issuing a double refund to the user's credit card!
# Fix: Ensure cancellation is idempotent (only transition once from CONFIRMED).
# ---------------------------------------------------------------------
class ReservationRecord:
    def __init__(self, status: str = "CONFIRMED"):
        self.status = status

def process_cancellation_refund(record: ReservationRecord) -> bool:
    # BUGGY VERSION:
    # issue_refund() # Executed regardless of current status!

    # FIXED VERSION:
    if record.status != "CONFIRMED":
        return False  # Already cancelled or processed; no-op!
    record.status = "CANCELLED"
    return True


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    d1_out = date(2026, 10, 5)
    d2_in = date(2026, 10, 5)
    assert check_overlap_safe(date(2026, 10, 1), d1_out, d2_in, date(2026, 10, 10)) is False

    # Test Bug 2 fix
    try:
        validate_booking_dates(date(2026, 10, 5), date(2026, 10, 1))
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    assert validate_booking_dates(date(2026, 10, 1), date(2026, 10, 5)) == 4

    # Test Bug 3 fix
    rec = ReservationRecord("CONFIRMED")
    assert process_cancellation_refund(rec) is True
    assert process_cancellation_refund(rec) is False  # Second attempt ignored!

    print("All Day 60 debugging fixes verified successfully!")
