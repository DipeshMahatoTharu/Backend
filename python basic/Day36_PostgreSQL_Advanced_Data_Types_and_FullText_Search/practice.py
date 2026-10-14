"""
============================================================
DAY 36 PRACTICE — JSONB, ARRAYS & FULL-TEXT SEARCH
============================================================

Explore semi-structured JSON querying and inverted index search mechanics.
In SQLite (which mirrors PostgreSQL JSON functions via `json_extract`),
we learn how to query nested keys and build an Inverted Index (GIN simulation).
"""

import sqlite3
import json
import re
from typing import List, Dict, Any, Set

def setup_json_db(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS event_logs;")
    cursor.execute("""
        CREATE TABLE event_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_name TEXT NOT NULL,
            payload JSON NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Seed semi-structured JSON payloads:
    events = [
        ("auth_service", json.dumps({"user_id": 101, "role": "ADMIN", "ip": "192.168.1.1", "meta": {"browser": "Chrome", "os": "Linux"}})),
        ("payment_service", json.dumps({"user_id": 102, "amount": 149.99, "currency": "USD", "gateway": "STRIPE", "status": "SUCCESS"})),
        ("auth_service", json.dumps({"user_id": 103, "role": "MEMBER", "ip": "10.0.0.4", "meta": {"browser": "Safari", "os": "macOS"}})),
        ("payment_service", json.dumps({"user_id": 101, "amount": 49.00, "currency": "USD", "gateway": "PAYPAL", "status": "FAILED"})),
    ]
    cursor.executemany("INSERT INTO event_logs (service_name, payload) VALUES (?, ?);", events)
    conn.commit()


# =====================================================================
# TASK 1: Query Nested JSON Keys (PostgreSQL ->> and json_extract)
# =====================================================================
def query_admins_from_json(conn: sqlite3.Connection) -> List[tuple]:
    """
    In PostgreSQL:
    SELECT id, payload->>'user_id', payload->'meta'->>'os' 
    FROM event_logs 
    WHERE payload->>'role' = 'ADMIN';
    
    In SQLite: json_extract(payload, '$.role') = 'ADMIN'
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, json_extract(payload, '$.user_id'), json_extract(payload, '$.meta.os')
        FROM event_logs
        WHERE json_extract(payload, '$.role') = 'ADMIN';
    """)
    return cursor.fetchall()


# =====================================================================
# TASK 2: Build an Inverted Index (GIN Simulation)
# =====================================================================
class InvertedIndexEngine:
    """
    Simulates how a PostgreSQL GIN (Generalized Inverted Index) works:
    Instead of mapping Document -> Words, it maps Word -> Set(Document IDs)!
    """
    def __init__(self):
        self.index: Dict[str, Set[int]] = {}
        self.documents: Dict[int, str] = {}

    def _tokenize(self, text: str) -> List[str]:
        # Basic normalization and tokenization (stemming simulation)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        stop_words = {"the", "and", "for", "with", "from", "this"}
        return [w for w in words if w not in stop_words]

    def add_document(self, doc_id: int, text: str) -> None:
        self.documents[doc_id] = text
        tokens = self._tokenize(text)
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(doc_id)

    def search_and(self, keywords: List[str]) -> List[int]:
        """Performs boolean AND search using set intersection (instant O(1) per word)."""
        tokens = [k.lower() for k in keywords]
        matching_sets = [self.index.get(token, set()) for token in tokens]
        if not matching_sets:
            return []
        # Intersect all matching doc ID sets:
        result = set.intersection(*matching_sets)
        return sorted(list(result))


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    setup_json_db(conn)
    
    admins = query_admins_from_json(conn)
    print("--- JSON Query Results (Admins) ---")
    for adm in admins:
        print(f"Log ID: {adm[0]}, User ID: {adm[1]}, OS: {adm[2]}")
    assert len(admins) == 1
    assert admins[0][1] == 101
    
    print("\n--- Inverted Index (GIN) Search Simulation ---")
    engine = InvertedIndexEngine()
    engine.add_document(1, "PostgreSQL high performance database with B-Tree and GIN indexes")
    engine.add_document(2, "Django REST framework building high-speed JSON APIs with Python")
    engine.add_document(3, "Optimizing slow SQL queries in PostgreSQL and database performance")
    
    matches = engine.search_and(["postgresql", "performance"])
    print(f"Documents matching 'postgresql' AND 'performance': {matches}")
    assert matches == [1, 3]
    print("[+] Inverted index lookup passed with O(1) set intersection!")
    conn.close()
