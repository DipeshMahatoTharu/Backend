# Day 60 — Real-World Backend Engineering Interview

These questions cover enterprise system design, high-concurrency booking architectures, and distributed transactions.

---

### Question 1: System Design — How Do You Design Airbnb / Booking.com at Global Scale?
**Interview Scenario:**
> *"How do you design a hotel booking system capable of handling 50 million hotel rooms, 50,000 search queries per second, and 5,000 simultaneous booking attempts during Black Friday without double booking?"*

#### Senior Mentor Answer & Key Points:
1. **Search vs Booking Separation (CQRS)**:
   - **Read Path (Search)**:
     - 99.9% of traffic is searching availability.
     - Store room availability bitmaps or inverted index in Redis.
     - A 365-day availability bitmap takes only 46 bytes per room!
     - ElasticSearch / Postgres GIN indexes handle geospatial location and amenity filtering.
   - **Write Path (Booking)**:
     - When a customer clicks 'Reserve', issue an atomic Redis lock (`SET lock:room:101:2026-10-01 NX EX 600`).
     - This holds a 10-minute temporary checkout reservation while the user enters payment details.
2. **Double-Booking Prevention at Database Level**:
   - In PostgreSQL, use an Exclusion Constraint with GIST index:
     ```sql
     ALTER TABLE reservations
     ADD CONSTRAINT no_overlapping_bookings
     EXCLUDE USING gist (room_id WITH =, daterange(check_in, check_out) WITH &&);
     ```
   - The database engine physically rejects any overlapping reservation with an `IntegrityError` at the storage layer, providing mathematical guarantee against double bookings!

---

### Question 2: Two-Phase Commit vs Saga Pattern in Distributed Travel Bookings
**Interview Scenario:**
> *"A user books a flight, a hotel, and a car rental in a single bundle transaction. If the flight succeeds and the hotel succeeds, but the car rental fails, how do you handle this across 3 distinct microservices?"*

#### Senior Mentor Answer & Key Points:
1. **Why Two-Phase Commit (2PC) Fails in Microservices**:
   - 2PC holds locks across all 3 third-party systems over the network. If one service is slow, all services hang, creating cascading failures.
2. **The Saga Pattern (Compensating Transactions)**:
   - Break the distributed transaction into a sequence of local transactions:
     1. Reserve Flight -> Succeeds.
     2. Reserve Hotel -> Succeeds.
     3. Reserve Car -> **FAILS!**
   - When step 3 fails, the Saga Orchestrator triggers **Compensating Transactions** in reverse order:
     - Cancel Hotel Reservation (issues refund).
     - Cancel Flight Reservation (issues refund).
   - This ensures eventual consistency across distributed heterogeneous systems without locking resources.
