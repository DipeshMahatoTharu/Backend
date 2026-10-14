"""
============================================================
DAY 36 DEBUGGING — JSON TYPE TRAPS & CORRUPT SERIALIZATION
============================================================

Diagnose two major real-world JSON/PostgreSQL bugs:
1. Double Serialization Trap (Storing JSON as double-quoted string).
2. Unsanitized Key Path Injection.
"""

import json
import sqlite3

def demonstrate_double_serialization_bug():
    """
    BUG SCENARIO 1:
    A developer already had a Python dictionary and dumped it to JSON string,
    then passed it to a driver that automatically serializes dictionaries, 
    or accidentally called json.dumps() twice!
    The database stores: "\"{\\\"user\\\": 101}\""
    JSON extract functions return NULL or fail to parse keys!
    """
    data = {"role": "DEVELOPER", "skills": ["Python", "PostgreSQL"]}
    
    # Buggy double dump:
    first_dump = json.dumps(data)
    accidental_double_dump = json.dumps(first_dump) # DANGEROUS!
    
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE config (id INTEGER PRIMARY KEY, meta JSON);")
    cursor.execute("INSERT INTO config VALUES (1, ?);", (accidental_double_dump,))
    conn.commit()
    
    cursor.execute("SELECT json_extract(meta, '$.role') FROM config WHERE id = 1;")
    extracted = cursor.fetchone()[0]
    conn.close()
    return extracted # Returns None! Query broken due to double serialization!


def fixed_json_serialization():
    """
    CORRECTED SCENARIO:
    Dump JSON string exactly once or let ORM/driver handle native serialization.
    """
    data = {"role": "DEVELOPER", "skills": ["Python", "PostgreSQL"]}
    clean_dump = json.dumps(data)
    
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE config (id INTEGER PRIMARY KEY, meta JSON);")
    cursor.execute("INSERT INTO config VALUES (1, ?);", (clean_dump,))
    conn.commit()
    
    cursor.execute("SELECT json_extract(meta, '$.role') FROM config WHERE id = 1;")
    extracted = cursor.fetchone()[0]
    conn.close()
    return extracted # Returns 'DEVELOPER' cleanly!


if __name__ == "__main__":
    broken_result = demonstrate_double_serialization_bug()
    print(f"Double serialization extraction: {broken_result} (Failed as expected!)")
    clean_result = fixed_json_serialization()
    print(f"Clean serialization extraction:  {clean_result} (Success!)")
    assert clean_result == "DEVELOPER"
