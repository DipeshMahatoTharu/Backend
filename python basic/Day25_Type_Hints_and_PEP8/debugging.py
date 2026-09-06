# Day 25 Debugging — Type Annotations, Dataclasses & Mutable Defaults

from dataclasses import dataclass, field
from typing import Any

# =====================================================================
# BUGGY SCENARIO 1: The Shared Mutable Default List
# =====================================================================
# Goal: Create customer cart sessions.
# Problem: The developer used a mutable list as a default parameter.
# Because default arguments are evaluated only once when the function is defined,
# every customer without explicit items ends up modifying the EXACT SAME cart!

def buggy_create_cart(customer_id: str, items: list = []):
    items.append("Welcome Coupon")
    return {"customer_id": customer_id, "items": items}

# ---------------------------------------------------------------------
# QUESTION: Why do mutable default arguments cause state leakage between requests?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using None as the default argument and initializing inside.
# ---------------------------------------------------------------------
def fixed_create_cart(customer_id: str, items: list[str] | None = None) -> dict[str, Any]:
    pass


# =====================================================================
# BUGGY SCENARIO 2: Silent Type Mismatch in API Filtering
# =====================================================================
# Goal: Filter products by ID received from an HTTP query parameter.
# Problem: In Python, `101 == "101"` is False! Because the developer did not
# enforce type casting or type annotations, the function silently returns
# None for valid IDs without raising an error.

def buggy_find_product(products: list[dict], search_id):
    for p in products:
        if p["id"] == search_id: # search_id comes in as string "101", p["id"] is int 101!
            return p
    return None

# ---------------------------------------------------------------------
# QUESTION: How do explicit type hints and type casting prevent silent query bugs?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with type hints and defensive integer conversion.
# ---------------------------------------------------------------------
def fixed_find_product(products: list[dict[str, Any]], search_id: int | str) -> dict[str, Any] | None:
    pass


# =====================================================================
# BUGGY SCENARIO 3: The "Any" Type Escape Hatch
# =====================================================================
# Goal: Log user display name.
# Problem: The developer typed the argument as `Any` to silence the linter.
# In production, different user objects are passed (some are dicts, some are
# Django User model objects, some are dataclasses). The code calls `.username`
# which crashes with AttributeError when a dict is passed!

def buggy_get_display_name(user: Any) -> str:
    # Unchecked attribute access crashes at runtime if user is a dict!
    return user.username.upper()

# ---------------------------------------------------------------------
# QUESTION: Why is overusing 'Any' anti-pattern in backend type systems?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with Union/isinstance checks to handle both dict and object types.
# ---------------------------------------------------------------------
def fixed_get_display_name(user: dict[str, Any] | object) -> str:
    pass