"""
Day 38: Django Template Engine & Static Files — Debugging
Diagnose and fix 3 common template security flaws and static configuration errors.
"""
import html
from typing import Dict, Any, List

# ---------------------------------------------------------------------
# Bug 1: Improper Use of `|safe` Causing Stored XSS
# Problem: A forum view renders user comments using `{{ comment.text|safe }}`
# so users can use markdown, but attackers submit `<script>` tags.
# Fix: Sanitize content before marking safe.
# ---------------------------------------------------------------------
def render_user_comment(raw_comment: str, allowed_tags: List[str] = None) -> str:
    # BUGGY VERSION:
    # return raw_comment # Marking unsafe input as safe!

    # FIXED VERSION:
    allowed_tags = allowed_tags or ["<b>", "</b>", "<i>", "</i>"]
    # Escape everything first
    clean = html.escape(raw_comment)
    # Unescape explicitly allowed safe formatting tags
    for tag in allowed_tags:
        escaped_tag = html.escape(tag)
        clean = clean.replace(escaped_tag, tag)
    return clean


# ---------------------------------------------------------------------
# Bug 2: `STATIC_ROOT` and `STATICFILES_DIRS` Conflict
# Problem: Settings configuration has:
#   STATIC_ROOT = BASE_DIR / 'static'
#   STATICFILES_DIRS = [BASE_DIR / 'static']
# Running `collectstatic` errors with:
#   "The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting."
# Fix: Ensure source dirs and build output dir are completely separate.
# ---------------------------------------------------------------------
def validate_static_settings(staticfiles_dirs: List[str], static_root: str) -> bool:
    # BUGGY VERSION: Allowed overlapping paths
    # return True

    # FIXED VERSION:
    for d in staticfiles_dirs:
        if d == static_root:
            raise ValueError(f"STATICFILES_DIRS contains STATIC_ROOT ('{static_root}'). They must be separate!")
    return True


# ---------------------------------------------------------------------
# Bug 3: Missing Context Processor Variables
# Problem: Navbar template requires `{{ request.user }}`, but `request` is None
# because `django.template.context_processors.request` was missing.
# Fix: Inject standard request context.
# ---------------------------------------------------------------------
def build_template_context(custom_context: Dict[str, Any], request_user: str) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return custom_context # Missing user context!

    # FIXED VERSION:
    full_ctx = {"request": {"user": request_user}}
    full_ctx.update(custom_context)
    return full_ctx


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    malicious = "Hello <b>world</b> <script>stealCookies()</script>"
    safe_out = render_user_comment(malicious)
    assert "<b>world</b>" in safe_out
    assert "<script>" not in safe_out
    assert "&lt;script&gt;" in safe_out

    # Test Bug 2 fix
    try:
        validate_static_settings(["/app/static"], "/app/static")
        assert False, "Should raise ValueError on overlapping static dirs"
    except ValueError:
        pass
    assert validate_static_settings(["/app/frontend/static"], "/app/staticfiles") is True

    # Test Bug 3 fix
    ctx = build_template_context({"title": "Dashboard"}, "dipesh_admin")
    assert ctx["request"]["user"] == "dipesh_admin"

    print("All Day 38 debugging fixes verified successfully!")
