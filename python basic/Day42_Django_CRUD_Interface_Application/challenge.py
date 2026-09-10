"""
Day 42 Daily Challenge: Full-Featured Ticket Management CRUD Controller

Problem:
Implement a full CRUD controller for an Issue/Ticket tracking system:
1. `list_tickets(request)`: Returns all active tickets.
2. `create_ticket(request)`: On POST, creates ticket, queues success message, and redirects to detail.
3. `detail_ticket(request, pk)`: Returns ticket or raises 404 if missing.
4. `update_ticket(request, pk)`: On POST, updates fields, queues message, and redirects.
5. `delete_ticket(request, pk)`: On POST, marks status as 'DELETED', queues message, and redirects to list.
"""
from typing import Dict, Any, Optional, List

class Http404(Exception):
    pass

class TicketCRUDController:
    def __init__(self):
        self._db: Dict[int, Dict[str, Any]] = {
            1: {"id": 1, "title": "Memory leak in worker", "priority": "HIGH", "status": "OPEN"},
            2: {"id": 2, "title": "Add dark mode toggle", "priority": "LOW", "status": "CLOSED"},
        }
        self._next_id = 3
        self.flash_messages: List[str] = []

    def get_object_or_404(self, pk: int) -> Dict[str, Any]:
        if pk not in self._db or self._db[pk]["status"] == "DELETED":
            raise Http404(f"Ticket #{pk} not found")
        return self._db[pk]

    def list(self) -> List[Dict[str, Any]]:
        return [t for t in self._db.values() if t["status"] != "DELETED"]

    def create(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        if not post_data.get("title"):
            raise ValueError("Title is required")
        new_id = self._next_id
        self._next_id += 1
        ticket = {
            "id": new_id,
            "title": post_data["title"],
            "priority": post_data.get("priority", "MEDIUM"),
            "status": "OPEN"
        }
        self._db[new_id] = ticket
        self.flash_messages.append(f"Ticket #{new_id} created successfully!")
        return {"status": 302, "redirect_url": f"/tickets/{new_id}/"}

    def detail(self, pk: int) -> Dict[str, Any]:
        return self.get_object_or_404(pk)

    def update(self, pk: int, post_data: Dict[str, Any]) -> Dict[str, Any]:
        ticket = self.get_object_or_404(pk)
        if "title" in post_data:
            ticket["title"] = post_data["title"]
        if "priority" in post_data:
            ticket["priority"] = post_data["priority"]
        if "status" in post_data:
            ticket["status"] = post_data["status"]

        self.flash_messages.append(f"Ticket #{pk} updated successfully!")
        return {"status": 302, "redirect_url": f"/tickets/{pk}/"}

    def delete(self, pk: int) -> Dict[str, Any]:
        ticket = self.get_object_or_404(pk)
        ticket["status"] = "DELETED"
        self.flash_messages.append(f"Ticket #{pk} deleted.")
        return {"status": 302, "redirect_url": "/tickets/"}


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    controller = TicketCRUDController()

    # 1. List active
    tickets = controller.list()
    assert len(tickets) == 2

    # 2. Create Ticket
    res = controller.create({"title": "Fix database deadlock", "priority": "URGENT"})
    assert res["status"] == 302
    assert res["redirect_url"] == "/tickets/3/"
    assert controller.detail(3)["priority"] == "URGENT"

    # 3. Update Ticket
    res_upd = controller.update(3, {"status": "RESOLVED"})
    assert res_upd["status"] == 302
    assert controller.detail(3)["status"] == "RESOLVED"

    # 4. Delete Ticket
    res_del = controller.delete(3)
    assert res_del["status"] == 302
    assert res_del["redirect_url"] == "/tickets/"

    # 5. Verify 404 after deletion
    try:
        controller.detail(3)
        assert False, "Deleted ticket should raise Http404"
    except Http404:
        pass

    assert len(controller.list()) == 2

    print("All TicketCRUDController challenge tests passed successfully!")
