"""
============================================================
DAY 35 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Senior Concurrency Engineer — Concert Ticket Reservation Lock Engine

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
A concert has 10,000 available seats. During a flash sale, 200,000 concurrent
users hit the checkout API to book seats.
If two users select Seat #42 simultaneously, exactly ONE user must succeed,
and the other user must receive a "Seat already reserved" notice.
Under NO circumstance can a seat be double-booked!

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
1. Design the `seats` table schema with appropriate status and locking constraints.
2. Implement a Python reservation manager `SeatReservationEngine` with method:
   `reserve_seat(seat_number: int, user_id: int) -> bool`
3. The method must:
   - Begin a transaction.
   - Use row-level locking semantics (or atomic conditional update with rowcount check).
   - If available, mark status = 'RESERVED', set user_id, and commit.
   - If already reserved, rollback cleanly and return False.
   - Prevent race conditions even under concurrent threads.

============================================================
MY IMPLEMENTATION:
============================================================
"""

import sqlite3
import threading

class SeatReservationEngine:
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seats (
                seat_number INTEGER PRIMARY KEY,
                status TEXT NOT NULL CHECK(status IN ('AVAILABLE', 'RESERVED', 'SOLD')),
                user_id INTEGER DEFAULT NULL,
                reserved_at TIMESTAMP DEFAULT NULL
            );
        """)
        # Initialize 100 test seats
        cursor.execute("DELETE FROM seats;")
        for i in range(1, 101):
            cursor.execute("INSERT INTO seats (seat_number, status) VALUES (?, 'AVAILABLE');", (i,))
        conn.commit()
        conn.close()

    def reserve_seat(self, seat_number: int, user_id: int) -> bool:
        """
        Atomically attempts to claim an AVAILABLE seat for user_id.
        In PostgreSQL, this corresponds to:
        SELECT * FROM seats WHERE seat_number = ? AND status = 'AVAILABLE' FOR UPDATE;
        followed by UPDATE.
        """
        conn = sqlite3.connect(self.db_path, timeout=10.0)
        cursor = conn.cursor()
        
        # Atomic test-and-set:
        cursor.execute("""
            UPDATE seats 
            SET status = 'RESERVED', user_id = ?, reserved_at = CURRENT_TIMESTAMP
            WHERE seat_number = ? AND status = 'AVAILABLE';
        """, (user_id, seat_number))
        conn.commit()
        
        # If rowcount is 1, we won the lock and claimed the seat!
        # If rowcount is 0, someone else claimed it before us.
        claimed = cursor.rowcount > 0
        conn.close()
        return claimed


if __name__ == "__main__":
    db_file = "ticket_whiteboard.db"
    engine = SeatReservationEngine(db_file)
    
    # Simulate 50 concurrent users trying to book the EXACT SAME SEAT (#42)
    successful_claimant = []
    
    def attempt_booking(user_id):
        if engine.reserve_seat(seat_number=42, user_id=user_id):
            successful_claimant.append(user_id)
            
    threads = []
    for uid in range(1, 51):
        t = threading.Thread(target=attempt_booking, args=(uid,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Total successful bookings for Seat 42: {len(successful_claimant)}")
    print(f"Winning User ID: {successful_claimant[0]}")
    assert len(successful_claimant) == 1, "Race condition! Seat was double booked!"
    print("[+] Concurrency test passed: Zero double-booking occurred under 50 concurrent threads.")
