"""
Day 38: Django Template Engine & Static Files — Practice
Hands-on exercises covering template context resolution, HTML sanitization, and static path compilation.
"""
import html
from typing import Dict, Any, List

# ---------------------------------------------------------------------
# Task 1: DTL-Style Variable Resolver with Dot-Notation
# ---------------------------------------------------------------------
def resolve_context_variable(context: Dict[str, Any], path: str) -> Any:
    """
    Resolves dot-notation expressions like 'user.profile.name' or 'items.0'
    against a nested dictionary context.
    """
    parts = path.split(".")
    curr = context
    for p in parts:
        if isinstance(curr, dict) and p in curr:
            curr = curr[p]
        elif isinstance(curr, (list, tuple)) and p.isdigit():
            idx = int(p)
            if 0 <= idx < len(curr):
                curr = curr[idx]
            else:
                return ""
        elif hasattr(curr, p):
            curr = getattr(curr, p)
            if callable(curr):
                curr = curr()
        else:
            return ""
    return curr


# ---------------------------------------------------------------------
# Task 2: HTML Auto-Escaper and Filter Simulator
# ---------------------------------------------------------------------
def apply_filter(value: Any, filter_name: str, is_safe: bool = False) -> str:
    """
    Applies template filters: 'upper', 'lower', 'title', 'default'.
    Applies HTML escaping unless is_safe is True.
    """
    val_str = str(value)
    if filter_name == "upper":
        val_str = val_str.upper()
    elif filter_name == "lower":
        val_str = val_str.lower()
    elif filter_name == "title":
        val_str = val_str.title()

    if not is_safe:
        return html.escape(val_str)
    return val_str


# ---------------------------------------------------------------------
# Task 3: Static Asset URL Builder
# ---------------------------------------------------------------------
def static_url_resolver(base_static_url: str, asset_path: str, cache_buster: str = "") -> str:
    """
    Generates production-safe static asset URLs with optional cache-busting hashes.
    """
    base = base_static_url.rstrip("/")
    path = asset_path.lstrip("/")
    url = f"{base}/{path}"
    if cache_buster:
        url += f"?v={cache_buster}"
    return url


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 38 Practice Tests ---")

    # Test Task 1
    ctx = {
        "user": {"name": "Dipesh", "roles": ["Admin", "Engineer"]},
        "counts": [10, 20, 30]
    }
    assert resolve_context_variable(ctx, "user.name") == "Dipesh"
    assert resolve_context_variable(ctx, "user.roles.0") == "Admin"
    assert resolve_context_variable(ctx, "counts.2") == 30
    assert resolve_context_variable(ctx, "nonexistent.field") == ""

    # Test Task 2
    raw_html = "<script>alert('hack');</script>"
    escaped = apply_filter(raw_html, "lower", is_safe=False)
    assert "&lt;script&gt;" in escaped
    assert "<script>" not in escaped

    safe_html = apply_filter("<b>Bold</b>", "lower", is_safe=True)
    assert "<b>" in safe_html

    # Test Task 3
    url = static_url_resolver("/static/", "css/styles.css", cache_buster="abc1234")
    assert url == "/static/css/styles.css?v=abc1234"

    print("All Day 38 practice assertions passed successfully!")
