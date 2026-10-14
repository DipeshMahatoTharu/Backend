"""
Day 40 Daily Challenge: Memory QuerySet Engine with Lookups, Q-Objects & F-Expressions

Problem:
Implement a lightweight, chainable QuerySet engine `MemoryQuerySet` that:
1. Supports method chaining: `filter()`, `exclude()`, `order_by()`, `values()`.
2. Supports lazy evaluation: evaluation only happens on `list()`, iteration, or `.count()`.
3. Supports field lookups (`__gt`, `__lt`, `__icontains`, `__in`).
4. Supports `F` expressions for atomic mutations: `.update(stock=F('stock') + 5)`.
"""
from typing import List, Dict, Any, Optional

class F:
    def __init__(self, field_name: str):
        self.field_name = field_name
        self.delta = 0

    def __add__(self, value: int):
        self.delta += value
        return self

    def __sub__(self, value: int):
        self.delta -= value
        return self

    def resolve(self, record: Dict[str, Any]) -> Any:
        return record.get(self.field_name, 0) + self.delta


class MemoryQuerySet:
    def __init__(self, data: List[Dict[str, Any]]):
        self._data = data
        self._filters: List[Dict[str, Any]] = []
        self._excludes: List[Dict[str, Any]] = []
        self._order_by_fields: List[str] = []
        self._cached_results: Optional[List[Dict[str, Any]]] = None

    def filter(self, **kwargs) -> 'MemoryQuerySet':
        clone = self._clone()
        clone._filters.append(kwargs)
        return clone

    def exclude(self, **kwargs) -> 'MemoryQuerySet':
        clone = self._clone()
        clone._excludes.append(kwargs)
        return clone

    def order_by(self, *fields: str) -> 'MemoryQuerySet':
        clone = self._clone()
        clone._order_by_fields = list(fields)
        return clone

    def _clone(self) -> 'MemoryQuerySet':
        qs = MemoryQuerySet(self._data)
        qs._filters = list(self._filters)
        qs._excludes = list(self._excludes)
        qs._order_by_fields = list(self._order_by_fields)
        return qs

    def _evaluate(self) -> List[Dict[str, Any]]:
        if self._cached_results is not None:
            return self._cached_results

        results = list(self._data)

        # Apply filters
        for f in self._filters:
            filtered = []
            for item in results:
                match = True
                for k, v in f.items():
                    parts = k.split("__")
                    fname = parts[0]
                    lookup = parts[1] if len(parts) > 1 else "exact"
                    val = item.get(fname)
                    if lookup == "exact" and val != v: match = False
                    elif lookup == "gt" and not (val > v): match = False
                    elif lookup == "lt" and not (val < v): match = False
                    elif lookup == "icontains" and v.lower() not in str(val).lower(): match = False
                if match:
                    filtered.append(item)
            results = filtered

        # Apply excludes
        for ex in self._excludes:
            results = [
                it for it in results
                if not all(it.get(k) == v for k, v in ex.items())
            ]

        # Apply ordering
        for ord_field in reversed(self._order_by_fields):
            desc = ord_field.startswith("-")
            fname = ord_field[1:] if desc else ord_field
            results.sort(key=lambda x: x.get(fname, 0), reverse=desc)

        self._cached_results = results
        return self._cached_results

    def count(self) -> int:
        return len(self._evaluate())

    def exists(self) -> bool:
        return len(self._evaluate()) > 0

    def update(self, **kwargs) -> int:
        evaluated = self._evaluate()
        count = 0
        for item in evaluated:
            for k, v in kwargs.items():
                if isinstance(v, F):
                    item[k] = v.resolve(item)
                else:
                    item[k] = v
            count += 1
        return count

    def __iter__(self):
        return iter(self._evaluate())

    def __len__(self):
        return len(self._evaluate())


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    records = [
        {"id": 1, "title": "MacBook Pro", "category": "laptops", "price": 2000, "stock": 10},
        {"id": 2, "title": "Dell XPS", "category": "laptops", "price": 1500, "stock": 5},
        {"id": 3, "title": "iPhone 15", "category": "phones", "price": 999, "stock": 20},
        {"id": 4, "title": "iPad Pro", "category": "tablets", "price": 800, "stock": 0},
    ]

    qs = MemoryQuerySet(records)

    # 1. Filter + Lookups
    expensive_laptops = qs.filter(category="laptops", price__gt=1600)
    assert expensive_laptops.count() == 1
    assert list(expensive_laptops)[0]["title"] == "MacBook Pro"

    # 2. Exclude
    in_stock = qs.exclude(stock=0)
    assert in_stock.count() == 3

    # 3. Order By
    cheapest_first = list(qs.order_by("price"))
    assert cheapest_first[0]["price"] == 800

    # 4. F Expression Atomic Mutation
    qs.filter(id=1).update(stock=F("stock") - 2)
    assert records[0]["stock"] == 8

    print("All MemoryQuerySet challenge tests passed successfully!")
