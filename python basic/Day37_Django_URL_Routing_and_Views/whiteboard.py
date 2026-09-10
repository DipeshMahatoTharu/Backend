"""
============================================================
DAY 37 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Custom Regex URL Path Converter for ISO Dates

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a Django-compatible custom URL converter class `DatePathConverter`
that matches dates in `YYYY-MM-DD` format and converts them directly to Python `datetime.date` objects.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Attribute `regex`: regex pattern matching 4 digits, hyphen, 2 digits, hyphen, 2 digits.
- Method `to_python(self, value: str) -> datetime.date`: Parses string into `datetime.date`. Raises `ValueError` if month or day is invalid.
- Method `to_url(self, value: datetime.date) -> str`: Converts `datetime.date` back to string `YYYY-MM-DD`.

============================================================
MY APPROACH:
============================================================
1. Define regex attribute matching `r'[0-9]{4}-[0-9]{2}-[0-9]{2}'`.
2. In `to_python`, parse year, month, and day integers, then construct `datetime.date(y, m, d)`.
3. In `to_url`, use `.isoformat()` or `strftime('%Y-%m-%d')`.
"""
from datetime import date
import re

class DatePathConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> date:
        match = re.match(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", value)
        if not match:
            raise ValueError(f"Invalid date format: '{value}'")
        year, month, day = map(int, match.groups())
        # datetime.date constructor validates calendar day/month bounds (e.g. Feb 30, leap years)
        return date(year, month, day)

    def to_url(self, value: date) -> str:
        return value.isoformat()


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    converter = DatePathConverter()

    # Valid conversion
    d = converter.to_python("2026-09-09")
    assert isinstance(d, date)
    assert d.year == 2026 and d.month == 9 and d.day == 9

    # Reverse URL
    assert converter.to_url(d) == "2026-09-09"

    # Invalid calendar dates
    try:
        converter.to_python("2026-02-30")  # Invalid day in Feb
        assert False, "Should raise ValueError for invalid calendar day"
    except ValueError:
        pass

    try:
        converter.to_python("2026-13-01")  # Invalid month
        assert False, "Should raise ValueError for invalid month"
    except ValueError:
        pass

    print("Whiteboard Day 37 challenge passed successfully!")
