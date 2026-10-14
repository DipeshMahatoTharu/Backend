"""
Day 57 Daily Challenge: Multi-Container Docker Compose & Entrypoint Orchestrator

Problem:
Implement a simulation of a container orchestrator and entrypoint script:
1. `ContainerManager`:
   - Manages container lifecycles (`db`, `redis`, `web`, `worker`).
   - Simulates healthchecks (e.g. PostgreSQL takes 2 seconds to warm up).
2. `EntrypointScript`:
   - Waits for database health before proceeding.
   - Executes database migrations (`python manage.py migrate`).
   - Launches application web server only after migrations succeed.
   - Aborts container startup if database does not become ready within timeout.
"""
from typing import Dict, Any, List

class Container:
    def __init__(self, name: str, warm_up_ticks: int = 0):
        self.name = name
        self.warm_up_ticks = warm_up_ticks
        self.current_ticks = 0
        self.is_running = False

    def start(self):
        self.is_running = True

    def tick(self):
        if self.is_running:
            self.current_ticks += 1

    def is_healthy(self) -> bool:
        return self.is_running and self.current_ticks >= self.warm_up_ticks


class EntrypointOrchestrator:
    def __init__(self, db_container: Container, max_wait_ticks: int = 5):
        self.db = db_container
        self.max_wait_ticks = max_wait_ticks
        self.migrations_applied = False
        self.server_started = False

    def run(self) -> bool:
        # Step 1: Wait for database readiness
        waited = 0
        while not self.db.is_healthy():
            if waited >= self.max_wait_ticks:
                raise TimeoutError("Database connection timed out in entrypoint.sh!")
            self.db.tick()
            waited += 1

        # Step 2: Apply migrations
        self.migrations_applied = True

        # Step 3: Exec application server
        self.server_started = True
        return True


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Case 1: Healthy startup
    db = Container("postgres", warm_up_ticks=3)
    db.start()

    orchestrator = EntrypointOrchestrator(db, max_wait_ticks=5)
    success = orchestrator.run()
    assert success is True
    assert orchestrator.migrations_applied is True
    assert orchestrator.server_started is True

    # Test Case 2: Database failure / timeout
    broken_db = Container("postgres", warm_up_ticks=10)  # Takes too long!
    broken_db.start()

    broken_orch = EntrypointOrchestrator(broken_db, max_wait_ticks=3)
    try:
        broken_orch.run()
        assert False, "Should raise TimeoutError"
    except TimeoutError:
        pass

    assert broken_orch.migrations_applied is False
    assert broken_orch.server_started is False

    print("All Container Orchestrator challenge tests passed successfully!")
