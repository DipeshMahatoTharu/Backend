"""
============================================================
DAY 35 PRACTICE — CONCURRENCY, LOST UPDATES & ROW LOCKS
============================================================

Demonstrate the classic "Lost Update" race condition when two concurrent 
threads attempt to decrement inventory or account balance without locking, 
and then implement locking to achieve 100% thread-safe atomic updates.
"""

import sqlite3
import threading
import time

def setup_inventory_db(db_path: str = "concurrency_practice.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS inventory;")
    cursor.execute("""
        CREATE TABLE inventory (
            id INTEGER PRIMARY KEY,
            item_name TEXT NOT NULL,
            stock INTEGER NOT NULL CHECK(stock >= 0)
        );
    """)
    # Start with exactly 10 units in stock
    cursor.execute("INSERT INTO inventory (id, item_name, stock) VALUES (1, 'PlayStation 5', 10);")
    conn.commit()
    conn.close()


# =====================================================================
# TASK 1: The "Lost Update" Race Condition (Without Locking)
# =====================================================================
def uncoordinated_buy_item(db_path: str, buyer_name: str, quantity: int = 1):
    """
    Simulates a naive, uncoordinated web request:
    1. Read stock from database.
    2. Sleep 10ms (simulating business logic / payment gateway call).
    3. Calculate new stock and write back.
    WITHOUT locking, this causes LOST UPDATES!
    """
    conn = sqlite3.connect(db_path, timeout=10.0)
    cursor = conn.cursor()
    
    # Read current stock
    cursor.execute("SELECT stock FROM inventory WHERE id = 1;")
    current_stock = cursor.fetchone()[0]
    
    # Simulate processing delay
    time.sleep(0.01)
    
    if current_stock >= quantity:
        new_stock = current_stock - quantity
        cursor.execute("UPDATE inventory SET stock = ? WHERE id = 1;", (new_stock,))
        conn.commit()
        
    conn.close()


# =====================================================================
# TASK 2: Atomic Update / Locking Strategy
# =====================================================================
# In SQL, an atomic update statement performs read and write inside the engine's row lock:
# UPDATE inventory SET stock = stock - 1 WHERE id = 1 AND stock >= 1;
#
# In PostgreSQL, you can also use:
# SELECT stock FROM inventory WHERE id = 1 FOR UPDATE;

def atomic_buy_item(db_path: str, buyer_name: str, quantity: int = 1) -> bool:
    """
    Thread-safe atomic decrement directly inside SQLite / PostgreSQL.
    Returns True if purchase succeeded, False if sold out.
    """
    conn = sqlite3.connect(db_path, timeout=10.0)
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE inventory 
        SET stock = stock - ? 
        WHERE id = 1 AND stock >= ?;
    """, (quantity, quantity))
    conn.commit()
    
    success = cursor.rowcount > 0
    conn.close()
    return success


def run_race_condition_test():
    db_path = "concurrency_test.db"
    setup_inventory_db(db_path)
    
    print("[*] Launching 10 concurrent uncoordinated buyers for 10 items...")
    threads = []
    for i in range(10):
        t = threading.Thread(target=uncoordinated_buy_item, args=(db_path, f"Buyer-{i}"))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    conn = sqlite3.connect(db_path)
    final_stock = conn.cursor().execute("SELECT stock FROM inventory WHERE id = 1;").fetchone()[0]
    conn.close()
    print(f"[!] Without Atomic Locking: Final stock is {final_stock} (Expected 0! Race condition occurred!)")
    
    # Now run atomic test
    setup_inventory_db(db_path)
    print("\n[*] Launching 10 concurrent ATOMIC buyers...")
    threads = []
    successful_purchases = []
    
    def worker(i):
        if atomic_buy_item(db_path, f"Buyer-{i}"):
            successful_purchases.append(i)
            
    for i in range(10):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    conn = sqlite3.connect(db_path)
    atomic_stock = conn.cursor().execute("SELECT stock FROM inventory WHERE id = 1;").fetchone()[0]
    conn.close()
    print(f"[+] With Atomic Execution: Final stock is {atomic_stock} (Expected 0) | Successful purchases: {len(successful_purchases)}")


if __name__ == "__main__":
    run_race_condition_test()
