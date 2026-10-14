"""
============================================================
DAY 36 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Production Django Settings Configuration Parser & Sanitizer

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Write a configuration sanitizer `sanitize_django_settings(raw_settings: dict) -> dict`
that prepares settings for safe logging/inspection in an APM tool (e.g. Sentry/Datadog):
1. Redact values for any keys containing sensitive keywords: 'KEY', 'SECRET', 'PASSWORD', 'TOKEN', 'SIGNATURE'.
   Replace values with '********'.
2. If `DEBUG` is True, emit a warning log in the returned dictionary under `_warnings`.
3. Normalize `ALLOWED_HOSTS` into a list of lowercase strings.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Recursive inspection if nested dictionaries exist.
- Preserve all non-sensitive keys intact.

============================================================
MY APPROACH:
============================================================
1. Traverse dictionary items.
2. If a key contains sensitive substrings (case-insensitive), replace its value with '********'.
3. Recursively process nested dictionaries.
4. Normalize ALLOWED_HOSTS and add `_warnings` if DEBUG is True.
"""
from typing import Dict, Any

SENSITIVE_KEYWORDS = ["KEY", "SECRET", "PASSWORD", "TOKEN", "SIGNATURE"]

def sanitize_django_settings(raw_settings: Dict[str, Any]) -> Dict[str, Any]:
    sanitized: Dict[str, Any] = {}
    warnings = []

    if raw_settings.get("DEBUG") is True:
        warnings.append("DEBUG mode is ENABLED")

    for k, v in raw_settings.items():
        # Check sensitivity
        is_sensitive = any(kw in k.upper() for kw in SENSITIVE_KEYWORDS)
        if is_sensitive and isinstance(v, (str, int, float, bytes)):
            sanitized[k] = "********"
        elif isinstance(v, dict):
            # Nested dictionary (e.g. DATABASES)
            nested_sanitized = {}
            for nk, nv in v.items():
                if any(kw in nk.upper() for kw in SENSITIVE_KEYWORDS):
                    nested_sanitized[nk] = "********"
                else:
                    nested_sanitized[nk] = nv
            sanitized[k] = nested_sanitized
        elif k == "ALLOWED_HOSTS" and isinstance(v, list):
            sanitized[k] = [str(h).lower() for h in v]
        else:
            sanitized[k] = v

    if warnings:
        sanitized["_warnings"] = warnings

    return sanitized


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    test_settings = {
        "DEBUG": True,
        "SECRET_KEY": "supersecretkey123",
        "ALLOWED_HOSTS": ["API.EXAMPLE.COM", "LOCALHOST"],
        "DATABASES": {
            "ENGINE": "django.db.backends.postgresql",
            "PASSWORD": "db_master_password_99"
        }
    }
    result = sanitize_django_settings(test_settings)
    assert result["SECRET_KEY"] == "********"
    assert result["DATABASES"]["PASSWORD"] == "********"
    assert result["ALLOWED_HOSTS"] == ["api.example.com", "localhost"]
    assert "DEBUG mode is ENABLED" in result["_warnings"]

    print("Whiteboard Day 36 challenge passed successfully!")
