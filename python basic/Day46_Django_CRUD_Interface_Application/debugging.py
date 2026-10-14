"""
Day 42: Django CRUD Interface Application — Debugging
Diagnose and fix 3 common CRUD interface bugs and form submission traps.
"""
from typing import Dict, Any, Optional

# ---------------------------------------------------------------------
# Bug 1: Missing PRG Redirect (The Refresh Bug)
# Problem: A view creates an order and calls `render(request, 'success.html')`.
# When the user refreshes, another order is placed!
# Fix: Return `redirect()` instead of `render()`.
# ---------------------------------------------------------------------
def handle_checkout(request_method: str, form_is_valid: bool, order_id: int) -> Dict[str, Any]:
    # BUGGY VERSION:
    # if request_method == 'POST' and form_is_valid:
    #     return {"action": "render", "template": "success.html"}

    # FIXED VERSION:
    if request_method == "POST" and form_is_valid:
        return {"action": "redirect", "url": f"/orders/{order_id}/confirmation/"}
    return {"action": "render", "template": "checkout.html"}


# ---------------------------------------------------------------------
# Bug 2: Mutating Object Without Calling `save()`
# Problem: An update view changes `ticket.status = 'CLOSED'` but forgets `.save()`.
# Changes are lost as soon as the request ends!
# Fix: Ensure `.save()` is called.
# ---------------------------------------------------------------------
class TicketEntity:
    def __init__(self, status: str = "OPEN"):
        self.status = status
        self.is_persisted = False

    def save(self):
        self.is_persisted = True

def close_ticket(ticket: TicketEntity):
    # BUGGY VERSION:
    # ticket.status = "CLOSED"

    # FIXED VERSION:
    ticket.status = "CLOSED"
    ticket.save()


# ---------------------------------------------------------------------
# Bug 3: Using GET for State Deletion
# Problem: An engineer added `<a href="/tickets/4/delete">Delete</a>`.
# Google Web Crawler clicked every link on the page and wiped out the entire database!
# Fix: Require POST method for all deletion endpoints.
# ---------------------------------------------------------------------
def delete_endpoint_guard(method: str) -> bool:
    # BUGGY VERSION:
    # return True # Allowed GET requests to delete!

    # FIXED VERSION:
    if method.upper() != "POST":
        raise PermissionError("HTTP POST method required to execute deletions.")
    return True


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    checkout_res = handle_checkout("POST", True, 42)
    assert checkout_res["action"] == "redirect"
    assert checkout_res["url"] == "/orders/42/confirmation/"

    # Test Bug 2 fix
    t = TicketEntity()
    close_ticket(t)
    assert t.status == "CLOSED"
    assert t.is_persisted is True

    # Test Bug 3 fix
    try:
        delete_endpoint_guard("GET")
        assert False, "GET method should be rejected"
    except PermissionError:
        pass
    assert delete_endpoint_guard("POST") is True

    print("All Day 42 debugging fixes verified successfully!")
