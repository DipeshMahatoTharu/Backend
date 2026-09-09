"""
============================================================
DAY 32 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: High-Concurrency User Repository & Thread-Safe Connection Pool

In high-traffic production services (Django, FastAPI, Gunicorn),
backend repositories must checkout connections from a shared pool,
execute parameterized queries, and guarantee the connection is returned
to the pool even if database errors or application crashes occur.

============================================================
REQUIREMENTS:
============================================================
1. Class `ThreadSafeConnectionPool`:
   - `__init__(self, max_connections: int = 5)`:
     Initializes an internal queue/list of connections.
   - `get_connection(self, timeout: float = 2.0)`:
     Checks out an available connection. If all connections are in use,
     waits up to `timeout` seconds before raising `TimeoutError("Connection pool exhausted")`.
   - `release_connection(self, conn)`:
     Rolls back any uncommitted dirty transactions and returns the connection
     to the pool.
   - `active_count` property: returns number of connections currently checked out.

2. Class `UserRepository`:
   - `__init__(self, pool: ThreadSafeConnectionPool)`:
   - `create_user(self, username: str, email: str, password_hash: str) -> dict`:
     Inserts a user, commits, and returns the newly created user record.
   - `get_user_by_id(self, user_id: int) -> dict | None`:
     Fetches user by primary key.
   - `batch_register(self, user_list: list[tuple[str, str, str]]) -> int`:
     Inserts multiple users in a single atomic transaction.
   - CRITICAL REQUIREMENT: Every single method MUST return the connection
     to the pool in a `finally` block!
"""

import sqlite3
import queue
import time
from typing import Optional, Any


class ThreadSafeConnectionPool:
    def __init__(self, max_connections: int = 5):
        self.max_connections = max_connections
        self._pool: queue.Queue = queue.Queue(maxsize=max_connections)
        self._checked_out: int = 0

        for _ in range(max_connections):
            # Create in-memory DB connections configured with dict row factory
            conn = sqlite3.connect(":memory:", check_same_thread=False)
            conn.row_factory = self._dict_factory
            self._init_schema(conn)
            self._pool.put(conn)

    @staticmethod
    def _dict_factory(cursor, row):
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

    @staticmethod
    def _init_schema(conn):
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()

    def get_connection(self, timeout: float = 2.0) -> sqlite3.Connection:
        """Checks out a connection from the pool."""
        try:
            conn = self._pool.get(block=True, timeout=timeout)
            self._checked_out += 1
            return conn
        except queue.Empty:
            raise TimeoutError("Connection pool exhausted: no connections available")

    def release_connection(self, conn: sqlite3.Connection) -> None:
        """Rolls back any dangling transaction and returns connection to pool."""
        try:
            conn.rollback()
        except Exception:
            pass
        self._checked_out = max(0, self._checked_out - 1)
        self._pool.put(conn)

    @property
    def active_count(self) -> int:
        return self._checked_out


class UserRepository:
    def __init__(self, pool: ThreadSafeConnectionPool):
        self.pool = pool

    def create_user(self, username: str, email: str, password_hash: str) -> dict[str, Any]:
        """Creates a new user safely using a connection from the pool."""
        # TODO: Implement checkout, parameterized insert, commit, and guaranteed release
        pass

    def get_user_by_id(self, user_id: int) -> Optional[dict[str, Any]]:
        """Fetches user by id, guaranteeing connection is returned to pool."""
        # TODO: Implement checkout, select, and guaranteed release
        pass

    def batch_register(self, user_list: list[tuple[str, str, str]]) -> int:
        """Batch registers users atomically."""
        # TODO: Implement atomic batch insert using executemany
        pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing High-Concurrency User Repository & Pool...")
    db_pool = ThreadSafeConnectionPool(max_connections=3)
    repo = UserRepository(db_pool)

    print(f"Initial active connections in pool: {db_pool.active_count}")

    # Test 1: User creation
    u1 = repo.create_user("dipesh_backend", "dipesh@gmail.com", "argon2_hash_xyz")
    print(f"Test 1 (Created User): {u1}")
    print(f"Active connections after request (Must be 0!): {db_pool.active_count}")

    # Test 2: User fetch
    fetched = repo.get_user_by_id(1)
    print(f"Test 2 (Fetched User): {fetched}")
    print(f"Active connections after fetch (Must be 0!): {db_pool.active_count}")

    # Test 3: Error handling & connection leak prevention
    try:
        # Attempting to insert duplicate email should raise IntegrityError
        repo.create_user("duplicate_user", "dipesh@gmail.com", "hash")
    except Exception as e:
        print(f"Test 3 (Caught expected duplicate error): {type(e).__name__}")
    print(f"Active connections after exception (Must STILL be 0!): {db_pool.active_count}")

    # Test 4: Pool exhaustion test
    conns = [db_pool.get_connection() for _ in range(3)]
    print(f"Checked out all 3 connections. Active count: {db_pool.active_count}")
    try:
        db_pool.get_connection(timeout=0.5)
        print("ERROR: Should have timed out!")
    except TimeoutError:
        print("Test 4 (Pool timeout verified on exhaustion: OK)")

    # Release checked out connections
    for c in conns:
        db_pool.release_connection(c)
    print(f"Active count after releasing: {db_pool.active_count}")

    print("\nAll User Repository & Connection Pool tests passed successfully!")