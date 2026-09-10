"""
============================================================
DAY 38 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: Dynamic Template String Replacement with HTML Sanitization

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a lightweight template renderer `render_email_template(template_text: str, context: dict) -> str`
that securely formats notification emails.
1. Replaces placeholders in the format `{{ key }}` with context values.
2. Supports fallback default values: `{{ key|default:'Guest' }}`.
3. Automatically escapes HTML special characters in values to prevent injection.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Ignore whitespace around variable names: `{{   user_name   }}`.
- If a variable is missing and has no default, replace with empty string `""`.

============================================================
MY APPROACH:
============================================================
1. Use regex pattern `r"{{\s*([a-zA-Z_][a-zA-Z0-9_]*)(?:\|default:'([^']*)')?\s*}}"`.
2. Extract the key and optional default.
3. Retrieve value from context; if missing, use default or `""`.
4. Escape special characters using `html.escape()` and return substituted string.
"""
import re
import html
from typing import Dict, Any

def render_email_template(template_text: str, context: Dict[str, Any]) -> str:
    pattern = re.compile(r"{{\s*([a-zA-Z_][a-zA-Z0-9_]*)(?:\|default:'([^']*)')?\s*}}")

    def replacer(match: re.Match) -> str:
        key = match.group(1)
        default_val = match.group(2) if match.group(2) is not None else ""
        raw_val = context.get(key)
        if raw_val is None:
            val_to_use = default_val
        else:
            val_to_use = str(raw_val)

        return html.escape(val_to_use)

    return pattern.sub(replacer, template_text)


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    tmpl = "Hello, {{ name|default:'Friend' }}! Your balance is {{ balance }}."
    
    # 1. Full context
    res1 = render_email_template(tmpl, {"name": "Dipesh", "balance": "$150.00"})
    assert res1 == "Hello, Dipesh! Your balance is $150.00."

    # 2. Missing key with default
    res2 = render_email_template(tmpl, {"balance": "$0.00"})
    assert res2 == "Hello, Friend! Your balance is $0.00."

    # 3. HTML escaping
    res3 = render_email_template("Hello {{ name }}", {"name": "<b>Attacker</b>"})
    assert res3 == "Hello &lt;b&gt;Attacker&lt;/b&gt;"

    print("Whiteboard Day 38 challenge passed successfully!")
