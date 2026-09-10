# Day 42 — Full-Stack Django CRUD Workflows & PRG Pattern

## 🎯 Learning Objectives
- Build an end-to-end CRUD (Create, Read, Update, Delete) application in Django.
- Master the **Post/Redirect/Get (PRG)** pattern to prevent duplicate form submissions upon browser refresh.
- Implement secure state modification with Django's Messages framework (`django.contrib.messages`).
- Master URL reversal (`django.urls.reverse` and `redirect`) to decouple views from hardcoded paths.
- Handle object lookups with `get_object_or_404()` to return clean HTTP 404 responses automatically.

---

## 📚 Core Backend Concepts

### 1. The Post/Redirect/Get (PRG) Pattern
Without PRG:
1. User submits `POST /tickets/create/` (creates ticket #42).
2. Server renders `success.html` directly with status `200 OK`.
3. User hits `F5` (Refresh) -> Browser prompts *"Confirm Form Resubmission"* and sends another `POST`, creating ticket #43!

**With PRG (Industry Standard)**:
1. User submits `POST /tickets/create/`.
2. Server creates ticket #42 and returns **`302 Found` Redirect** to `/tickets/42/`.
3. Browser performs `GET /tickets/42/`. Refreshing now only re-executes safe `GET`!

### 2. Standard Django CRUD View Structure
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm

def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, f"Ticket #{ticket.pk} updated successfully!")
            return redirect('ticket-detail', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'ticket': ticket})
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review CRUD workflows, PRG mechanics, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Implement PRG controllers in [`practice.py`](practice.py), and fix duplicate mutation bugs in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Ticket Management CRUD Application in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
