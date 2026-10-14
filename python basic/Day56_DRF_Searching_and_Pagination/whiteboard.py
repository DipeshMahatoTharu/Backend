"""
============================================================
DAY 50 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: In-Memory Search Engine with Field Weighting

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a weighted search scoring function:
`score_search_results(items: list, search_terms: str, weights: dict) -> list`
that:
1. Splits `search_terms` into individual lowercase tokens.
2. For each item, calculates a relevance score:
   - For each matching token found in a field: `score += weights.get(field, 1)`.
   - If token matches exact word: double the points (`weight * 2`).
3. Returns items with `score > 0` sorted in descending order of score.

Weights example:
`{"title": 10, "tags": 5, "description": 1}`

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return `list` of tuples: `[(item, score)]` sorted by score descending.

============================================================
MY APPROACH:
============================================================
1. Tokenize query.
2. For each item, iterate over weighted fields.
3. Compute matching points.
4. Filter > 0 and sort by score desc.
"""
from typing import List, Dict, Any, Tuple

def score_search_results(
    items: List[Dict[str, Any]],
    search_terms: str,
    weights: Dict[str, int]
) -> List[Tuple[Dict[str, Any], int]]:
    tokens = [t.lower() for t in search_terms.split() if t.strip()]
    if not tokens:
        return []

    scored = []
    for it in items:
        total_score = 0
        for field, weight in weights.items():
            val = str(it.get(field, "")).lower()
            import re
            val_words = set(re.findall(r"\w+", val))
            for tok in tokens:
                if tok in val_words:
                    total_score += weight * 2  # Exact word match bonus
                elif tok in val:
                    total_score += weight      # Substring match

        if total_score > 0:
            scored.append((it, total_score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    docs = [
        {"id": 1, "title": "Django Python Framework", "tags": "python api", "description": "Learn backend"},
        {"id": 2, "title": "Python Basics", "tags": "python", "description": "Django is mentioned here"},
        {"id": 3, "title": "Go Concurrency", "tags": "go", "description": "Goroutines"},
    ]

    weights = {"title": 10, "tags": 5, "description": 1}
    results = score_search_results(docs, "Django Python", weights)

    assert len(results) == 2
    # Doc 1 has both 'Django' (20) and 'Python' (20) in title + 'python' (10) in tags -> score 50!
    assert results[0][0]["id"] == 1
    assert results[1][0]["id"] == 2
    assert results[0][1] > results[1][1]

    print("Whiteboard Day 50 challenge passed successfully!")
