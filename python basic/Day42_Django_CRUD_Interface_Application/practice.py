"""
Day 42: Django CRUD Interface Application — Practice
Hands-on exercises covering the PRG pattern, flash message lifecycle, and CRUD state transitions.
"""
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Task 1: Flash Messages Queue Simulator
# ---------------------------------------------------------------------
class FlashMessages:
    def __init__(self):
        self._messages: List[Dict[str, str]] = []

    def add(self, level: str, text: str):
        self._messages.append({"level": level, "text": text})

    def get_and_clear(self) -> List[Dict[str, str]]:
        """Consumes messages once (popping them from session)."""
        msgs = list(self._messages)
        self._messages.clear()
        return msgs


# ---------------------------------------------------------------------
# Task 2: Post/Redirect/Get Controller Simulator
# ---------------------------------------------------------------------
class PRGResponse:
    def __init__(self, status_code: int, location: Optional[str] = None, content: Optional[str] = None):
        self.status_code = status_code
        self.location = location
        self.content = content

class MockTicketService:
    def __init__(self):
        self.tickets = {}
        self.next_id = 1
        self.flash = FlashMessages()

    def handle_request(self, method: str, data: Optional[Dict[str, Any]] = None) -> PRGResponse:
        if method == "POST":
            # 1. Mutate state
            if not data or "title" not in data:
                return PRGResponse(400, content="Invalid payload")
            tid = self.next_id
            self.next_id += 1
            self.tickets[tid] = {"id": tid, "title": data["title"], "status": "OPEN"}
            self.flash.add("success", f"Ticket #{tid} created!")
            # 2. Redirect (PRG)
            return PRGResponse(302, location=f"/tickets/{tid}/")
        elif method == "GET":
            # Read state
            return PRGResponse(200, content=f"Listing {len(self.tickets)} tickets")
        return PRGResponse(405)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 42 Practice Tests ---")

    # Test Task 1
    queue = FlashMessages()
    queue.add("success", "Profile updated")
    assert len(queue.get_and_clear()) == 1
    assert len(queue.get_and_clear()) == 0  # Consumed!

    # Test Task 2
    svc = MockTicketService()
    # Safe GET
    res_get = svc.handle_request("GET")
    assert res_get.status_code == 200

    # Non-idempotent POST returns 302 Redirect
    res_post = svc.handle_request("POST", {"title": "Fix database connection leak"})
    assert res_post.status_code == 302
    assert res_post.location == "/tickets/1/"

    # Messages consumed
    msgs = svc.flash.get_and_clear()
    assert len(msgs) == 1
    assert "Ticket #1 created" in msgs[0]["text"]

    print("All Day 42 practice assertions passed successfully!")
