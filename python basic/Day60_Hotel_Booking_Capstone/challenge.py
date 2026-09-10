"""
Day 60 Daily Challenge: Complete Hotel Booking & Reservation Engine

Problem:
Implement the core business engine for a Hotel Reservation Platform:
1. `search_available_rooms(check_in, check_out, room_type=None)`:
   - Finds rooms that have NO overlapping active bookings during the requested interval.
2. `book_room(customer_id, room_id, check_in, check_out)`:
   - Validates check_in < check_out.
   - Atomically locks room availability and prevents double booking.
   - Calculates total price and issues confirmed reservation.
3. `cancel_reservation(reservation_id)`:
   - Releases the room dates back into availability.
4. `generate_revenue_report()`:
   - Aggregates total completed revenue and active booking count.
"""
from datetime import date
from typing import Dict, List, Any, Optional

class HotelBookingEngine:
    def __init__(self):
        self.rooms = {
            101: {"id": 101, "number": "101", "type": "DELUXE", "nightly_rate": 150.0},
            102: {"id": 102, "number": "102", "type": "STANDARD", "nightly_rate": 100.0},
            103: {"id": 103, "number": "103", "type": "SUITE", "nightly_rate": 300.0},
        }
        self.reservations: Dict[int, Dict[str, Any]] = {}
        self.next_reservation_id = 1

    def search_available_rooms(self, check_in: date, check_out: date, room_type: Optional[str] = None) -> List[Dict[str, Any]]:
        if check_in >= check_out:
            raise ValueError("Check-out date must be after check-in date.")

        available = []
        for r_id, room in self.rooms.items():
            if room_type and room["type"] != room_type:
                continue

            # Check for conflict with active reservations
            has_conflict = False
            for res in self.reservations.values():
                if res["room_id"] == r_id and res["status"] == "CONFIRMED":
                    # Overlap: start1 < end2 and end1 > start2
                    if check_in < res["check_out"] and check_out > res["check_in"]:
                        has_conflict = True
                        break

            if not has_conflict:
                available.append(room)

        return available

    def book_room(self, customer_id: int, room_id: int, check_in: date, check_out: date) -> Dict[str, Any]:
        if check_in >= check_out:
            raise ValueError("Check-out date must be after check-in date.")
        if room_id not in self.rooms:
            raise LookupError(f"Room #{room_id} not found.")

        # Atomic double-booking check
        for res in self.reservations.values():
            if res["room_id"] == room_id and res["status"] == "CONFIRMED":
                if check_in < res["check_out"] and check_out > res["check_in"]:
                    raise ValueError(f"Double-Booking Conflict: Room #{room_id} is already booked for these dates.")

        nights = (check_out - check_in).days
        rate = self.rooms[room_id]["nightly_rate"]
        total_price = round(nights * rate * 1.10, 2)  # 10% tax included

        res_id = self.next_reservation_id
        self.next_reservation_id += 1

        reservation = {
            "id": res_id,
            "customer_id": customer_id,
            "room_id": room_id,
            "check_in": check_in,
            "check_out": check_out,
            "nights": nights,
            "total_price": total_price,
            "status": "CONFIRMED"
        }
        self.reservations[res_id] = reservation
        return reservation

    def cancel_reservation(self, reservation_id: int) -> bool:
        if reservation_id not in self.reservations:
            raise LookupError(f"Reservation #{reservation_id} not found.")
        self.reservations[reservation_id]["status"] = "CANCELLED"
        return True

    def generate_revenue_report(self) -> Dict[str, Any]:
        confirmed = [r for r in self.reservations.values() if r["status"] == "CONFIRMED"]
        total_revenue = sum(r["total_price"] for r in confirmed)
        return {
            "active_reservations": len(confirmed),
            "total_revenue": round(total_revenue, 2)
        }


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    engine = HotelBookingEngine()

    d_in = date(2026, 10, 1)
    d_out = date(2026, 10, 5)  # 4 nights

    # 1. Search initially shows all 3 rooms
    avail = engine.search_available_rooms(d_in, d_out)
    assert len(avail) == 3

    # 2. Book Room 101 for Alice
    res1 = engine.book_room(customer_id=1, room_id=101, check_in=d_in, check_out=d_out)
    assert res1["id"] == 1
    assert res1["nights"] == 4
    assert res1["total_price"] == round(4 * 150.0 * 1.10, 2)

    # 3. Room 101 is now unavailable for overlapping dates
    avail_after = engine.search_available_rooms(date(2026, 10, 3), date(2026, 10, 7))
    assert len(avail_after) == 2
    assert all(r["id"] != 101 for r in avail_after)

    # 4. Double booking attempt raises ValueError
    try:
        engine.book_room(customer_id=2, room_id=101, check_in=date(2026, 10, 2), check_out=date(2026, 10, 4))
        assert False, "Should raise ValueError on double-booking"
    except ValueError as ve:
        assert "Double-Booking Conflict" in str(ve)

    # 5. Cancellation frees up room
    engine.cancel_reservation(res1["id"])
    avail_cancelled = engine.search_available_rooms(d_in, d_out)
    assert len(avail_cancelled) == 3  # Room 101 is back!

    print("All HotelBookingEngine Capstone tests passed successfully!")
