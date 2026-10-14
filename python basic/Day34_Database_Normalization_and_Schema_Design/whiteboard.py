"""
============================================================
DAY 34 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Senior Database Architect — Ride-Sharing (Uber/Pathao) Schema Design

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Design a clean, normalized relational database schema for a ride-sharing service.

The system needs to support:
1. `riders`: Name, phone number (unique), email, rating.
2. `drivers`: Name, license number (unique), vehicle model, plate number, is_available.
3. `rides`: A ride requested by a rider and fulfilled by a driver.
   - Status: REQUESTED, ACCEPTED, IN_PROGRESS, COMPLETED, CANCELLED.
   - Pickup & Dropoff coordinates (or address text).
   - Distance in km, total fare, payment status.
4. `reviews`: Optional post-ride rating (1-5 stars) and comment submitted by rider or driver.

------------------------------------------------------------
2. CONSTRAINTS & REQUIREMENTS:
------------------------------------------------------------
- Write complete SQL DDL (`CREATE TABLE`) with proper data types.
- Enforce foreign keys with correct deletion policies (e.g. if driver deleted, historical ride must NOT disappear).
- Add constraints (e.g. rating must be BETWEEN 1 AND 5, fare >= 0).
- Avoid transitive dependencies (3NF).

============================================================
MY SCHEMA IMPLEMENTATION:
============================================================
"""

import sqlite3

class RideSharingSchemaManager:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # 1. Riders Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS riders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                rating REAL DEFAULT 5.0 CHECK(rating >= 1.0 AND rating <= 5.0),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # 2. Drivers Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                license_number TEXT UNIQUE NOT NULL,
                vehicle_plate TEXT UNIQUE NOT NULL,
                vehicle_model TEXT NOT NULL,
                is_available INTEGER NOT NULL DEFAULT 1,
                rating REAL DEFAULT 5.0 CHECK(rating >= 1.0 AND rating <= 5.0),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # 3. Rides Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rides (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rider_id INTEGER NOT NULL,
                driver_id INTEGER,
                status TEXT NOT NULL CHECK(status IN ('REQUESTED', 'ACCEPTED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED')),
                pickup_address TEXT NOT NULL,
                dropoff_address TEXT NOT NULL,
                distance_km REAL CHECK(distance_km >= 0.0),
                fare_amount REAL CHECK(fare_amount >= 0.0),
                requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                FOREIGN KEY (rider_id) REFERENCES riders(id) ON DELETE RESTRICT,
                FOREIGN KEY (driver_id) REFERENCES drivers(id) ON DELETE SET NULL
            );
        """)
        
        # 4. Reviews Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ride_reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ride_id INTEGER UNIQUE NOT NULL,
                rating_score INTEGER NOT NULL CHECK(rating_score BETWEEN 1 AND 5),
                comment TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ride_id) REFERENCES rides(id) ON DELETE CASCADE
            );
        """)
        self.conn.commit()
        print("[+] Ride-sharing relational schema created successfully in 3NF.")

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    manager = RideSharingSchemaManager(conn)
    manager.create_schema()
    conn.close()
