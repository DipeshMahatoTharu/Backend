"""
Day 50 Daily Challenge: High-Performance Multi-Field Search & Keyset Cursor Pagination Engine

Problem:
Implement a standalone pagination and search controller that handles:
1. Search across multiple fields (`search_fields = ['^title', '=category', 'description']`).
2. Keyset (Cursor) Pagination:
   - Encodes opaque cursor: base64-encoded `{"last_id": 42, "last_timestamp": 1789092800}`.
   - Reads records strictly greater/less than cursor values without using SQL OFFSET.
   - Generates next/previous cursor links.
"""
import base64
import json
from typing import Dict, List, Any, Optional, Tuple

class CursorPaginator:
    def __init__(self, page_size: int = 2):
        self.page_size = page_size

    def encode_cursor(self, record: Dict[str, Any]) -> str:
        payload = {"id": record["id"], "created_at": record["created_at"]}
        return base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()

    def decode_cursor(self, cursor_str: str) -> Optional[Dict[str, Any]]:
        try:
            raw = base64.urlsafe_b64decode(cursor_str.encode()).decode()
            return json.loads(raw)
        except Exception:
            return None

    def paginate(self, dataset: List[Dict[str, Any]], cursor_str: Optional[str] = None) -> Dict[str, Any]:
        # Records assumed ordered by (created_at DESC, id DESC)
        sorted_data = sorted(dataset, key=lambda x: (x["created_at"], x["id"]), reverse=True)

        start_idx = 0
        if cursor_str:
            cursor_data = self.decode_cursor(cursor_str)
            if cursor_data:
                target_ts = cursor_data["created_at"]
                target_id = cursor_data["id"]
                for idx, it in enumerate(sorted_data):
                    # Find first item strictly after cursor
                    if (it["created_at"], it["id"]) < (target_ts, target_id):
                        start_idx = idx
                        break
                else:
                    start_idx = len(sorted_data)

        items = sorted_data[start_idx:start_idx + self.page_size]
        has_more = (start_idx + self.page_size) < len(sorted_data)

        next_cursor = self.encode_cursor(items[-1]) if has_more and items else None

        return {
            "results": items,
            "next_cursor": next_cursor,
            "has_next": has_more
        }


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    records = [
        {"id": 1, "title": "Article 1", "created_at": 100},
        {"id": 2, "title": "Article 2", "created_at": 200},
        {"id": 3, "title": "Article 3", "created_at": 300},
        {"id": 4, "title": "Article 4", "created_at": 400},
        {"id": 5, "title": "Article 5", "created_at": 500},
    ]

    paginator = CursorPaginator(page_size=2)

    # Page 1 (Newest first: ID 5, ID 4)
    p1 = paginator.paginate(records, cursor_str=None)
    assert len(p1["results"]) == 2
    assert p1["results"][0]["id"] == 5
    assert p1["results"][1]["id"] == 4
    assert p1["has_next"] is True
    assert p1["next_cursor"] is not None

    # Page 2 using cursor from Page 1 (ID 3, ID 2)
    p2 = paginator.paginate(records, cursor_str=p1["next_cursor"])
    assert len(p2["results"]) == 2
    assert p2["results"][0]["id"] == 3
    assert p2["results"][1]["id"] == 2
    assert p2["has_next"] is True

    # Page 3 using cursor from Page 2 (ID 1)
    p3 = paginator.paginate(records, cursor_str=p2["next_cursor"])
    assert len(p3["results"]) == 1
    assert p3["results"][0]["id"] == 1
    assert p3["has_next"] is False
    assert p3["next_cursor"] is None

    print("All CursorPaginator challenge tests passed successfully!")
