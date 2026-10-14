"""
Day 35 Daily Challenge: RESTful Bookstore Resource Manager & API Dispatcher

Problem:
Implement a full RESTful Resource Endpoint Controller for a Bookstore API.
The controller must manage `/api/v1/books` and `/api/v1/books/{id}` supporting:
1. `GET /api/v1/books`:
   - Filter by `author` and `genre`.
   - Sort by field with `-` prefix for descending (e.g. `?sort=-price`).
   - Paginate with `page` and `page_size`.
2. `POST /api/v1/books`:
   - Create a book. Must validate required fields: `title`, `author`, `price`.
   - Returns 201 Created with `Location` header.
3. `GET /api/v1/books/{id}`:
   - Returns 200 OK with single book, or 404 Not Found.
4. `PATCH /api/v1/books/{id}`:
   - Partial update of fields. Returns 200 OK.
5. `DELETE /api/v1/books/{id}`:
   - Deletes the book. Returns 204 No Content.
"""
from typing import Dict, List, Any, Optional, Tuple
import json

class BookstoreAPI:
    def __init__(self):
        self._books: Dict[int, Dict[str, Any]] = {
            1: {"id": 1, "title": "Clean Code", "author": "Robert Martin", "genre": "Tech", "price": 45.0},
            2: {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "genre": "Tech", "price": 50.0},
            3: {"id": 3, "title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help", "price": 20.0},
            4: {"id": 4, "title": "Refactoring", "author": "Martin Fowler", "genre": "Tech", "price": 55.0},
        }
        self._next_id = 5

    def handle_request(self, method: str, path: str, query_params: Optional[Dict[str, Any]] = None, body: Optional[Dict[str, Any]] = None) -> Tuple[int, Dict[str, str], Any]:
        method = method.upper()
        query_params = query_params or {}

        # 1. Collection routes: /api/v1/books
        if path == "/api/v1/books":
            if method == "GET":
                return self._list_books(query_params)
            elif method == "POST":
                return self._create_book(body)
            else:
                return 405, {"Allow": "GET, POST"}, {"error": "Method Not Allowed"}

        # 2. Individual item routes: /api/v1/books/{id}
        parts = path.strip("/").split("/")
        if len(parts) == 4 and parts[0] == "api" and parts[1] == "v1" and parts[2] == "books" and parts[3].isdigit():
            book_id = int(parts[3])
            if method == "GET":
                return self._get_book(book_id)
            elif method == "PATCH":
                return self._update_book(book_id, body)
            elif method == "DELETE":
                return self._delete_book(book_id)
            else:
                return 405, {"Allow": "GET, PATCH, DELETE"}, {"error": "Method Not Allowed"}

        return 404, {}, {"error": "Not Found"}

    def _list_books(self, qp: Dict[str, Any]) -> Tuple[int, Dict[str, str], Any]:
        results = list(self._books.values())

        # Filtering
        if "genre" in qp:
            results = [b for b in results if b["genre"].lower() == qp["genre"].lower()]
        if "author" in qp:
            results = [b for b in results if qp["author"].lower() in b["author"].lower()]

        # Sorting
        sort_by = qp.get("sort")
        if sort_by:
            desc = sort_by.startswith("-")
            field = sort_by[1:] if desc else sort_by
            results.sort(key=lambda x: x.get(field, 0), reverse=desc)

        # Pagination
        page = int(qp.get("page", 1))
        page_size = int(qp.get("page_size", 2))
        total_count = len(results)

        start = (page - 1) * page_size
        end = start + page_size
        paged_items = results[start:end]

        envelope = {
            "count": total_count,
            "page": page,
            "page_size": page_size,
            "results": paged_items
        }
        return 200, {"Content-Type": "application/json"}, envelope

    def _create_book(self, body: Optional[Dict[str, Any]]) -> Tuple[int, Dict[str, str], Any]:
        if not body:
            return 400, {}, {"error": "Missing request payload"}
        for field in ["title", "author", "price"]:
            if field not in body:
                return 422, {}, {"error": f"Field '{field}' is required."}

        new_id = self._next_id
        self._next_id += 1
        book = {
            "id": new_id,
            "title": body["title"],
            "author": body["author"],
            "genre": body.get("genre", "General"),
            "price": float(body["price"])
        }
        self._books[new_id] = book
        return 201, {"Location": f"/api/v1/books/{new_id}"}, book

    def _get_book(self, book_id: int) -> Tuple[int, Dict[str, str], Any]:
        if book_id not in self._books:
            return 404, {}, {"error": f"Book {book_id} not found"}
        return 200, {"Content-Type": "application/json"}, self._books[book_id]

    def _update_book(self, book_id: int, body: Optional[Dict[str, Any]]) -> Tuple[int, Dict[str, str], Any]:
        if book_id not in self._books:
            return 404, {}, {"error": f"Book {book_id} not found"}
        if not body:
            return 400, {}, {"error": "Missing request payload"}

        book = self._books[book_id]
        for k in ["title", "author", "genre", "price"]:
            if k in body:
                book[k] = body[k]
        return 200, {"Content-Type": "application/json"}, book

    def _delete_book(self, book_id: int) -> Tuple[int, Dict[str, str], Any]:
        if book_id not in self._books:
            return 404, {}, {"error": f"Book {book_id} not found"}
        del self._books[book_id]
        return 204, {}, None


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    api = BookstoreAPI()

    # 1. Test List with filter & pagination
    status, headers, body = api.handle_request("GET", "/api/v1/books", {"genre": "Tech", "page": 1, "page_size": 2})
    assert status == 200
    assert body["count"] == 3
    assert len(body["results"]) == 2

    # 2. Test Sorting by descending price
    status, headers, body = api.handle_request("GET", "/api/v1/books", {"sort": "-price", "page_size": 10})
    assert status == 200
    assert body["results"][0]["price"] == 55.0  # Refactoring is 55.0

    # 3. Test Create Book
    status, headers, body = api.handle_request("POST", "/api/v1/books", body={
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "price": 60.0,
        "genre": "Tech"
    })
    assert status == 201
    assert headers["Location"] == "/api/v1/books/5"
    assert body["id"] == 5

    # 4. Test Partial Update (PATCH)
    status, headers, body = api.handle_request("PATCH", "/api/v1/books/5", body={"price": 58.5})
    assert status == 200
    assert body["price"] == 58.5
    assert body["title"] == "Designing Data-Intensive Applications"

    # 5. Test Delete Book
    status, headers, body = api.handle_request("DELETE", "/api/v1/books/5")
    assert status == 204
    assert body is None

    # 6. Verify 404 after deletion
    status, headers, body = api.handle_request("GET", "/api/v1/books/5")
    assert status == 404

    print("All BookstoreAPI REST challenge tests passed successfully!")
