"""
============================================================
DAY 35 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: High-Throughput Job Queue Worker with SKIP LOCKED

In enterprise architectures (Celery, BullMQ, Sidekiq), multiple worker
servers read from a central database queue of background jobs.
If workers use standard SELECT, they lock the whole queue or block each other.
Using PostgreSQL's `SELECT ... FOR UPDATE SKIP LOCKED` allows workers 
to concurrently fetch tasks with ZERO blocking latency!

Your challenge:
Implement `DistributedJobQueue`:
1. `enqueue(job_type: str, payload: str, priority: int) -> int`
2. `claim_next_job(worker_id: str) -> Optional[dict]`
3. `complete_job(job_id: int)`
4. Simulate 5 concurrent worker threads processing 50 jobs with zero collisions!
"""

import sqlite3
import threading
import time
from typing import Optional, Dict, Any

class DistributedJobQueue:
    def __init__(self, db_path: str = "job_queue.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_queue (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_type TEXT NOT NULL,
                payload TEXT NOT NULL,
                priority INTEGER DEFAULT 1,
                status TEXT NOT NULL CHECK(status IN ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED')),
                claimed_by TEXT DEFAULT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_status_priority ON job_queue (status, priority DESC, id ASC);")
        conn.commit()
        conn.close()

    def enqueue(self, job_type: str, payload: str, priority: int = 1) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO job_queue (job_type, payload, priority, status)
            VALUES (?, ?, ?, 'PENDING');
        """, (job_type, payload, priority))
        conn.commit()
        job_id = cursor.lastrowid
        conn.close()
        return job_id

    def claim_next_job(self, worker_id: str) -> Optional[Dict[str, Any]]:
        """
        Simulates the SKIP LOCKED worker pattern.
        Atomically finds the top PENDING job and locks/claims it for worker_id.
        """
        conn = sqlite3.connect(self.db_path, timeout=10.0)
        cursor = conn.cursor()
        
        # In SQLite, we do atomic update of the first matching PENDING job:
        cursor.execute("""
            UPDATE job_queue
            SET status = 'PROCESSING', claimed_by = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = (
                SELECT id FROM job_queue
                WHERE status = 'PENDING'
                ORDER BY priority DESC, id ASC
                LIMIT 1
            );
        """, (worker_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            cursor.execute("SELECT id, job_type, payload, priority FROM job_queue WHERE claimed_by = ? AND status = 'PROCESSING' ORDER BY updated_at DESC LIMIT 1;", (worker_id,))
            row = cursor.fetchone()
            conn.close()
            if row:
                return {"id": row[0], "job_type": row[1], "payload": row[2], "priority": row[3]}
        conn.close()
        return None

    def complete_job(self, job_id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE job_queue SET status = 'COMPLETED', updated_at = CURRENT_TIMESTAMP WHERE id = ?;", (job_id,))
        conn.commit()
        conn.close()


def run_worker_simulation():
    db_file = "queue_simulation.db"
    queue = DistributedJobQueue(db_file)
    
    # Enqueue 30 jobs
    print("[*] Enqueueing 30 background jobs...")
    for i in range(1, 31):
        queue.enqueue(job_type="SEND_EMAIL", payload=f"user_{i}@example.com", priority=(i % 3) + 1)
        
    processed_by_worker = {f"Worker-{w}": [] for w in range(1, 4)}
    
    def worker_loop(w_id):
        while True:
            job = queue.claim_next_job(w_id)
            if not job:
                break
            processed_by_worker[w_id].append(job["id"])
            time.sleep(0.005) # simulate work
            queue.complete_job(job["id"])
            
    # Launch 3 concurrent worker threads
    threads = []
    for w in range(1, 4):
        t = threading.Thread(target=worker_loop, args=(f"Worker-{w}",))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print("[+] Processing complete across all 3 concurrent workers:")
    all_processed = []
    for w, jobs in processed_by_worker.items():
        print(f"  {w} processed {len(jobs)} jobs: {jobs[:5]}...")
        all_processed.extend(jobs)
        
    assert len(all_processed) == 30, f"Expected 30 total jobs, got {len(all_processed)}"
    assert len(set(all_processed)) == 30, "Duplicate job execution detected! Race condition in queue!"
    print("[+] ZERO duplicate job claims! 100% queue integrity verified.")


if __name__ == "__main__":
    run_worker_simulation()
