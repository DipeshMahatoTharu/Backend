"""
Day 47 Daily Challenge: Mini-DRF ModelViewSet & Router Engine

Problem:
Implement a full ModelViewSet and Router pipeline that:
1. Provides default CRUD actions: `list`, `create`, `retrieve`, `update`, `destroy`.
2. Supports `@action(detail=True/False, methods=[...])`.
3. Auto-registers endpoints in a Router:
   - Collection routes: `GET /items/` -> list, `POST /items/` -> create.
   - Detail routes: `GET /items/{id}/` -> retrieve, `PUT /items/{id}/` -> update, `DELETE /items/{id}/` -> destroy.
   - Custom action routes: `POST /items/{id}/archive/` -> archive.
"""
from typing import Dict, Any, List, Optional, Tuple, Callable

class ActionDescriptor:
    def __init__(self, func: Callable, detail: bool, methods: List[str]):
        self.func = func
        self.detail = detail
        self.methods = [m.upper() for m in methods]

def action(detail: bool, methods: List[str]):
    def decorator(func: Callable):
        func._action_meta = ActionDescriptor(func, detail, methods)
        return func
    return decorator


class ModelViewSet:
    def __init__(self):
        self.db: Dict[int, Dict[str, Any]] = {}
        self.next_id = 1

    def list(self) -> List[Dict[str, Any]]:
        return list(self.db.values())

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        item_id = self.next_id
        self.next_id += 1
        record = dict(data)
        record["id"] = item_id
        self.db[item_id] = record
        return record

    def retrieve(self, pk: int) -> Dict[str, Any]:
        if pk not in self.db:
            raise LookupError("Not found")
        return self.db[pk]

    def update(self, pk: int, data: Dict[str, Any]) -> Dict[str, Any]:
        if pk not in self.db:
            raise LookupError("Not found")
        self.db[pk].update(data)
        return self.db[pk]

    def destroy(self, pk: int) -> bool:
        if pk not in self.db:
            raise LookupError("Not found")
        del self.db[pk]
        return True


class SimpleRouter:
    def __init__(self):
        self.registry: Dict[str, ModelViewSet] = {}

    def register(self, prefix: str, viewset_instance: ModelViewSet):
        self.registry[prefix] = viewset_instance

    def dispatch(self, method: str, path: str, payload: Optional[Dict[str, Any]] = None) -> Tuple[int, Any]:
        method = method.upper()
        parts = [p for p in path.strip("/").split("/") if p]
        if not parts:
            return 404, {"error": "Not Found"}

        prefix = parts[0]
        if prefix not in self.registry:
            return 404, {"error": "Not Found"}

        viewset = self.registry[prefix]

        # Case 1: Collection /prefix/
        if len(parts) == 1:
            if method == "GET": return 200, viewset.list()
            elif method == "POST": return 201, viewset.create(payload or {})
            return 405, {"error": "Method Not Allowed"}

        # Case 2: Detail /prefix/{id}/
        if len(parts) == 2 and parts[1].isdigit():
            pk = int(parts[1])
            try:
                if method == "GET": return 200, viewset.retrieve(pk)
                elif method in ("PUT", "PATCH"): return 200, viewset.update(pk, payload or {})
                elif method == "DELETE":
                    viewset.destroy(pk)
                    return 204, None
                return 405, {"error": "Method Not Allowed"}
            except LookupError:
                return 404, {"error": "Not Found"}

        # Case 3: Custom action /prefix/{id}/{action}/ or /prefix/{action}/
        if len(parts) == 3 and parts[1].isdigit():
            pk = int(parts[1])
            action_name = parts[2]
            action_fn = getattr(viewset, action_name, None)
            if action_fn and hasattr(action_fn, "_action_meta"):
                meta: ActionDescriptor = action_fn._action_meta
                if meta.detail and method in meta.methods:
                    return 200, action_fn(pk, payload)
                return 405, {"error": "Method Not Allowed"}

        return 404, {"error": "Not Found"}


# Concrete ViewSet
class ProductViewSet(ModelViewSet):
    @action(detail=True, methods=["POST"])
    def discount(self, pk: int, payload: Dict[str, Any]):
        item = self.retrieve(pk)
        discount_rate = payload.get("rate", 0.1)
        item["price"] = round(item["price"] * (1.0 - discount_rate), 2)
        return item


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    router = SimpleRouter()
    p_viewset = ProductViewSet()
    router.register("products", p_viewset)

    # 1. Create
    status, body = router.dispatch("POST", "/products/", {"title": "Desk Lamp", "price": 40.0})
    assert status == 201
    assert body["id"] == 1

    # 2. List
    status, body = router.dispatch("GET", "/products/")
    assert status == 200
    assert len(body) == 1

    # 3. Retrieve
    status, body = router.dispatch("GET", "/products/1/")
    assert status == 200
    assert body["title"] == "Desk Lamp"

    # 4. Custom @action: discount
    status, body = router.dispatch("POST", "/products/1/discount/", {"rate": 0.25})
    assert status == 200
    assert body["price"] == 30.0

    # 5. Delete
    status, body = router.dispatch("DELETE", "/products/1/")
    assert status == 204

    # 6. Retrieve after delete -> 404
    status, body = router.dispatch("GET", "/products/1/")
    assert status == 404

    print("All ModelViewSet & Router challenge tests passed successfully!")
