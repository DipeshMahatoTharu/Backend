"""
Day 47: DRF ModelViewSets & Generic Views — Practice
Hands-on exercises covering ViewSet action mapping, @action decoration, and URL path generation.
"""
from typing import Dict, Any, List, Callable, Optional

# ---------------------------------------------------------------------
# Task 1: Action Decorator Simulator
# ---------------------------------------------------------------------
def action(detail: bool, methods: List[str]):
    """Decorator marking a method as an extra REST action."""
    def decorator(func: Callable):
        func.is_action = True
        func.detail = detail
        func.methods = [m.upper() for m in methods]
        return func
    return decorator


# ---------------------------------------------------------------------
# Task 2: Action-to-URL Mapper
# ---------------------------------------------------------------------
def generate_action_routes(prefix: str, viewset_cls: Any) -> List[Dict[str, Any]]:
    """
    Inspects a ViewSet class and returns generated route definitions for custom @actions.
    """
    routes = []
    for attr_name in dir(viewset_cls):
        attr = getattr(viewset_cls, attr_name)
        if callable(attr) and getattr(attr, "is_action", False):
            if attr.detail:
                path = f"/api/v1/{prefix}/{{id}}/{attr_name}/"
            else:
                path = f"/api/v1/{prefix}/{attr_name}/"
            routes.append({
                "action": attr_name,
                "path": path,
                "methods": attr.methods,
                "detail": attr.detail
            })
    return routes


# ---------------------------------------------------------------------
# Task 3: Mock ViewSet Example
# ---------------------------------------------------------------------
class OrderViewSetMock:
    @action(detail=True, methods=["POST"])
    def cancel(self, request, pk=None):
        return {"status": f"Order {pk} cancelled"}

    @action(detail=False, methods=["GET"])
    def metrics(self, request):
        return {"total_revenue": 50000}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 47 Practice Tests ---")

    # Test Task 1 & 2
    routes = generate_action_routes("orders", OrderViewSetMock)
    assert len(routes) == 2

    cancel_route = [r for r in routes if r["action"] == "cancel"][0]
    assert cancel_route["path"] == "/api/v1/orders/{id}/cancel/"
    assert cancel_route["methods"] == ["POST"]
    assert cancel_route["detail"] is True

    metrics_route = [r for r in routes if r["action"] == "metrics"][0]
    assert metrics_route["path"] == "/api/v1/orders/metrics/"
    assert metrics_route["methods"] == ["GET"]
    assert metrics_route["detail"] is False

    print("All Day 47 practice assertions passed successfully!")
