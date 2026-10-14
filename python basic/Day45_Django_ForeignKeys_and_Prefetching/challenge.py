"""
Day 41 Daily Challenge: Relational Prefetching Query Engine

Problem:
Implement a lightweight ORM relationship loader that resolves One-to-Many
and Many-to-Many relationships without triggering N+1 queries.
1. `select_related(*fields)`: Emulates SQL INNER JOIN by populating foreign key objects.
2. `prefetch_related(*fields)`: Emulates batch lookups (`WHERE id IN (...)`) to attach child lists.
3. Track and verify that nested relationships are loaded with minimal query executions.
"""
from typing import List, Dict, Any, Set

class DatabaseSession:
    def __init__(self):
        self.query_count = 0
        self.authors = {
            1: {"id": 1, "name": "Martin Fowler"},
            2: {"id": 2, "name": "Robert Martin"}
        }
        self.books = [
            {"id": 101, "author_id": 1, "title": "Refactoring"},
            {"id": 102, "author_id": 1, "title": "Patterns of Enterprise Application Architecture"},
            {"id": 103, "author_id": 2, "title": "Clean Code"},
            {"id": 104, "author_id": 2, "title": "Clean Architecture"},
        ]
        self.tags = {
            101: [{"id": 1, "name": "Architecture"}, {"id": 2, "name": "Refactoring"}],
            102: [{"id": 1, "name": "Architecture"}],
            103: [{"id": 3, "name": "Clean Code"}],
            104: [{"id": 1, "name": "Architecture"}, {"id": 3, "name": "Clean Code"}]
        }

    def fetch_books(self) -> List[Dict[str, Any]]:
        self.query_count += 1
        return [dict(b) for b in self.books]

    def fetch_authors_by_ids(self, author_ids: Set[int]) -> Dict[int, Dict[str, Any]]:
        self.query_count += 1
        return {aid: dict(self.authors[aid]) for aid in author_ids if aid in self.authors}

    def fetch_tags_for_books(self, book_ids: Set[int]) -> Dict[int, List[Dict[str, Any]]]:
        self.query_count += 1
        return {bid: list(self.tags.get(bid, [])) for bid in book_ids}

class BookQuerySet:
    def __init__(self, db: DatabaseSession):
        self.db = db
        self._select_fields: Set[str] = set()
        self._prefetch_fields: Set[str] = set()

    def select_related(self, *fields: str) -> 'BookQuerySet':
        self._select_fields.update(fields)
        return self

    def prefetch_related(self, *fields: str) -> 'BookQuerySet':
        self._prefetch_fields.update(fields)
        return self

    def execute(self) -> List[Dict[str, Any]]:
        books = self.db.fetch_books()

        # 1. Handle select_related (Foreign Key: Author)
        if "author" in self._select_fields:
            author_ids = {b["author_id"] for b in books}
            authors_map = self.db.fetch_authors_by_ids(author_ids)
            for b in books:
                b["author"] = authors_map.get(b["author_id"])

        # 2. Handle prefetch_related (Many-to-Many: Tags)
        if "tags" in self._prefetch_fields:
            book_ids = {b["id"] for b in books}
            tags_map = self.db.fetch_tags_for_books(book_ids)
            for b in books:
                b["tags"] = tags_map.get(b["id"], [])

        return books


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    db = DatabaseSession()
    qs = BookQuerySet(db)

    # Execute with both select_related and prefetch_related
    results = qs.select_related("author").prefetch_related("tags").execute()

    # Total queries must be exactly 3 (1 for books, 1 for authors, 1 for tags)
    assert db.query_count == 3
    assert len(results) == 4

    # Verify author populated via select_related
    assert results[0]["author"]["name"] == "Martin Fowler"
    assert results[2]["author"]["name"] == "Robert Martin"

    # Verify tags populated via prefetch_related
    assert len(results[0]["tags"]) == 2
    assert results[0]["tags"][0]["name"] == "Architecture"

    print("All Relational Prefetching challenge tests passed successfully!")
