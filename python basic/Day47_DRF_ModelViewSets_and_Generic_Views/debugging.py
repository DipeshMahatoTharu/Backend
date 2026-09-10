"""
Day 47: DRF ModelViewSets & Generic Views — Debugging
Diagnose and fix 3 common ModelViewSet configuration and routing traps.
"""
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Bug 1: Missing `detail=True` on Item Action
# Problem: An action `@action(detail=False, methods=['post']) def approve(self, request, pk=None)`
# was created, but because `detail=False`, DRF routed it to `/items/approve/`
# without accepting a primary key!
# Fix: Set `detail=True`.
# ---------------------------------------------------------------------
class ActionConfig:
    def __init__(self, name: str, detail: bool):
        self.name = name
        self.detail = detail

def get_action_url_pattern(prefix: str, action_cfg: ActionConfig) -> str:
    # BUGGY VERSION:
    # return f"/{prefix}/{action_cfg.name}/"

    # FIXED VERSION:
    if action_cfg.detail:
        return f"/{prefix}/<pk>/{action_cfg.name}/"
    return f"/{prefix}/{action_cfg.name}/"


# ---------------------------------------------------------------------
# Bug 2: Missing `basename` in Router Registration
# Problem: `router.register(r'users', CustomUserViewSet)` without a `queryset` attribute
# raises `AssertionError: 'basename' argument not specified, and could not automatically determine...`
# Fix: Always specify `basename` when queryset is dynamically overridden.
# ---------------------------------------------------------------------
def validate_router_registration(has_static_queryset: bool, basename: Optional[str]) -> bool:
    # BUGGY VERSION: Allowed registration without basename when queryset is None
    # return True

    # FIXED VERSION:
    if not has_static_queryset and not basename:
        raise ValueError("'basename' argument must be specified if ViewSet lacks a static queryset.")
    return True


# ---------------------------------------------------------------------
# Bug 3: `get_queryset()` Not Returning an Evaluatable QuerySet
# Problem: An engineer wrote `def get_queryset(self): return list(Model.objects.all())`.
# DRF filters and pagination failed because they require an un-evaluated Django QuerySet!
# Fix: Return QuerySet, not a Python list.
# ---------------------------------------------------------------------
class MockQuerySet:
    def filter(self, **kwargs): return self

def get_clean_queryset(is_list: bool) -> Any:
    # BUGGY VERSION:
    # if is_list: return [1, 2, 3]

    # FIXED VERSION:
    return MockQuerySet()


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    cfg_detail = ActionConfig("approve", detail=True)
    assert get_action_url_pattern("loans", cfg_detail) == "/loans/<pk>/approve/"

    # Test Bug 2 fix
    try:
        validate_router_registration(has_static_queryset=False, basename=None)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    assert validate_router_registration(has_static_queryset=False, basename="custom-users") is True

    # Test Bug 3 fix
    qs = get_clean_queryset(is_list=False)
    assert isinstance(qs, MockQuerySet)

    print("All Day 47 debugging fixes verified successfully!")
