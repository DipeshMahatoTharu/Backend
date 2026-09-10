# Day 60 — The Grand Capstone: Hotel Room Reservation & Booking Backend

## 🎯 Learning Objectives
- Design and build the complete, production-grade **Hotel Room Reservation & Booking Backend System**.
- Implement interval overlapping date math to query real-time room availability.
- Prevent **Double-Booking** under high concurrency using atomic database transactions and pessimistic row locking (`select_for_update()`).
- Implement dynamic pricing rules: Weekend surges, seasonal multipliers, and cleaning fees.
- Build clean REST API endpoints for searching, booking, cancelling, and viewing reservation analytics.

---

## 📚 System Architecture & Domain Model

### 1. Database Schema
```text
┌─────────────────┐       ┌──────────────────────┐       ┌──────────────────┐
│     Customer    │       │     Reservation      │       │       Room       │
├─────────────────┤       ├──────────────────────┤       ├──────────────────┤
│ id (PK)         │1     *│ id (PK)              │*     1│ id (PK)          │
│ name            ├───────┤ customer_id (FK)     ├───────┤ room_number      │
│ email           │       │ room_id (FK)         │       │ room_type        │
└─────────────────┘       │ check_in_date        │       │ base_price_night │
                          │ check_out_date       │       │ is_active        │
                          │ status (BOOKED/...)  │       └──────────────────┘
                          │ total_price          │
                          └──────────────────────┘
```

### 2. Preventing Double-Booking with Concurrency Control
```python
from django.db import transaction

def reserve_room(customer, room_id, check_in, check_out):
    with transaction.atomic():
        # 1. Lock the room row to serialize concurrent booking attempts
        room = Room.objects.select_for_update().get(id=room_id)

        # 2. Check for overlapping active bookings:
        # Overlap rule: (start1 < end2) AND (end1 > start2)
        conflict = Reservation.objects.filter(
            room=room,
            status='BOOKED',
            check_in_date__lt=check_out,
            check_out_date__gt=check_in
        ).exists()

        if conflict:
            raise ValidationError("Room is already reserved for the selected dates.")

        # 3. Create Reservation
        return Reservation.objects.create(...)
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review hotel reservation domain models, double-booking prevention, and answer [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build interval intersection algorithms in [`practice.py`](practice.py), and fix booking traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Complete Hotel Booking Capstone Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
