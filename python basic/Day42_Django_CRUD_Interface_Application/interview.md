# Day 42 — Real-World Backend Engineering Interview

These questions test your mastery of web form mechanics, duplicate submission prevention, and concurrency.

---

### Question 1: How Does the Post/Redirect/Get Pattern Prevent Financial Double Charges?
**Interview Scenario:**
> *"If an e-commerce checkout view simply returns `render(request, 'order_complete.html')`, what happens when the customer refreshes their browser or presses the browser back button?"*

#### Senior Mentor Answer & Key Points:
1. **The Form Resubmission Trap**:
   - When a browser renders an HTML page from a `POST` response, hitting Refresh (`F5`) instructs the browser to re-transmit the exact same HTTP `POST` request payload.
   - If the user clicks 'Confirm Form Resubmission', a duplicate order is created and their card is charged twice!
2. **The PRG Fix**:
   - The server must respond with HTTP `302 Found` or `303 See Other` with a `Location: /orders/42/confirmation/` header.
   - The browser automatically issues a `GET /orders/42/confirmation/`.
   - Subsequent refreshes only re-execute the idempotent `GET` request.

---

### Question 2: Optimistic Locking vs Pessimistic Locking in High-Traffic CRUD
**Interview Scenario:**
> *"Two customer service agents open the same support ticket at 10:00 AM. Agent A updates the ticket status to 'Resolved' at 10:01 AM. Agent B types a note and clicks Save at 10:02 AM. How does Django handle this by default, and how do you prevent Agent B from accidentally reverting Agent A's status?"*

#### Senior Mentor Answer & Key Points:
1. **Default Behavior (Last-Write-Wins)**:
   - Django executes `ticket.save()` which generates `UPDATE tickets SET status = ...;`. Agent B's save completely overwrites Agent A's resolution.
2. **Solution 1: Optimistic Locking (Recommended for web CRUD)**:
   - Add an integer `version` field.
   - Run: `Ticket.objects.filter(id=ticket.id, version=current_version).update(status=new_status, version=F('version') + 1)`.
   - If the rows updated is 0, another user modified the ticket in the meantime. Inform Agent B with a message: *"Ticket was updated by another user. Please review the latest changes."*
3. **Solution 2: Pessimistic Locking (`select_for_update()`)**:
   - Locks the row in the database using `SELECT ... FOR UPDATE` within a transaction. Best for short-lived banking ledger calculations, but poor for human form editing (holds locks while users take minutes to fill forms).
