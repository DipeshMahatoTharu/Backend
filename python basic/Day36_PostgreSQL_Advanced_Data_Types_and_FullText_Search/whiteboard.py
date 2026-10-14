"""
============================================================
DAY 36 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Senior PostgreSQL Architect — Full-Text Search with Trigram Fuzzy Matching

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Design a PostgreSQL search architecture for an online bookstore with 5 million titles.
Users frequently type misspelled queries (e.g. "harry poter", "python programing").
Standard `WHERE title LIKE '%query%'` is too slow (full table scan) and cannot handle typos!

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
1. Provide the PostgreSQL DDL commands to:
   - Enable the `pg_trgm` extension.
   - Create a `books` table with `id`, `title`, `author`, `description`.
   - Add a GIN index on `title` using the `gin_trgm_ops` operator class.
   - Add a generated `tsvector` column on `description` with a GIN index.
2. Implement a Python demonstration class `BookSearchEngine` that implements:
   - Exact and Prefix search.
   - Fuzzy typo-tolerant search using Trigram similarity ($N$-gram sliding window).

============================================================
MY IMPLEMENTATION:
============================================================
"""

import sqlite3
from typing import List, Tuple

class TrigramSearchSimulator:
    """
    Demonstrates the mechanics of PostgreSQL's pg_trgm extension.
    A trigram is a sequence of 3 consecutive characters.
    Similarity is calculated as:
    Similarity = (Common Trigrams) / (Total Unique Trigrams)
    """
    @staticmethod
    def generate_trigrams(text: str) -> set:
        cleaned = f"  {text.lower()} " # PostgreSQL standard padding
        trigrams = set()
        for i in range(len(cleaned) - 2):
            trigrams.add(cleaned[i:i+3])
        return trigrams

    @classmethod
    def similarity(cls, str1: str, str2: str) -> float:
        tri1 = cls.generate_trigrams(str1)
        tri2 = cls.generate_trigrams(str2)
        intersection = tri1.intersection(tri2)
        union = tri1.union(tri2)
        if not union:
            return 0.0
        return len(intersection) / len(union)

    @classmethod
    def word_similarity(cls, document: str, query: str) -> float:
        """Computes maximum word-level trigram similarity between document and query."""
        query_words = query.lower().split()
        doc_words = document.lower().split()
        if not query_words or not doc_words:
            return 0.0
        
        # Calculate average best word match
        scores = []
        for q in query_words:
            best_match = max(cls.similarity(dw, q) for dw in doc_words)
            scores.append(best_match)
        return sum(scores) / len(scores)

class BookSearchEngine:
    def __init__(self):
        self.catalog = [
            (1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
            (2, "Fluent Python: Clear, Concise, and Effective Programming", "Luciano Ramalho"),
            (3, "Designing Data-Intensive Applications", "Martin Kleppmann"),
            (4, "Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin"),
            (5, "PostgreSQL: Up and Running", "Regina Obe"),
        ]

    def fuzzy_search(self, user_query: str, threshold: float = 0.25) -> List[Tuple[int, str, float]]:
        """
        Simulates PostgreSQL pg_trgm word_similarity operator:
        SELECT id, title, word_similarity(title, ?) as score
        FROM books
        WHERE title %> ?
        ORDER BY score DESC;
        """
        matches = []
        for book_id, title, author in self.catalog:
            score = TrigramSearchSimulator.word_similarity(title, user_query)
            if score >= threshold:
                matches.append((book_id, title, round(score, 3)))
        # Sort by similarity score descending
        matches.sort(key=lambda x: x[2], reverse=True)
        return matches


if __name__ == "__main__":
    search = BookSearchEngine()
    
    # Test 1: Misspelling "harry poter"
    query_1 = "harry poter"
    results_1 = search.fuzzy_search(query_1)
    print(f"Results for typo query '{query_1}':")
    for r in results_1:
        print(f"  Match: {r[1]} (Score: {r[2]})")
    assert "Harry Potter" in results_1[0][1]
    
    # Test 2: Misspelling "pythn programing"
    query_2 = "pythn programing"
    results_2 = search.fuzzy_search(query_2)
    print(f"\nResults for typo query '{query_2}':")
    for r in results_2:
        print(f"  Match: {r[1]} (Score: {r[2]})")
    assert "Fluent Python" in results_2[0][1]
    print("\n[+] Trigram similarity engine passed with robust typo-tolerance!")
