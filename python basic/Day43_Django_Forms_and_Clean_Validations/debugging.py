"""
Day 43: Django Forms & Clean Validations — Debugging
Diagnose and fix 3 common form validation and clean method mistakes.
"""
from typing import Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Forgetting to Return Cleaned Value in `clean_<field>()`
# Problem: A developer normalized phone numbers in `clean_phone()` but didn't return
# the value. `form.cleaned_data['phone']` became `None`!
# Fix: Always return the cleaned value from `clean_<field>()`.
# ---------------------------------------------------------------------
def clean_phone_number(raw_phone: str) -> str:
    # BUGGY VERSION:
    # digits = "".join(c for c in raw_phone if c.isdigit())
    # # Forgot return! Returns None!

    # FIXED VERSION:
    digits = "".join(c for c in raw_phone if c.isdigit())
    return digits


# ---------------------------------------------------------------------
# Bug 2: Missing `super().clean()` in `clean()` Method
# Problem: Overriding `clean()` without calling `super().clean()` stripped out
# base model validation errors.
# Fix: Call `super().clean()` first.
# ---------------------------------------------------------------------
class BaseForm:
    def clean(self) -> Dict[str, Any]:
        return {"base_field": "validated_base"}

class ChildForm(BaseForm):
    def clean(self) -> Dict[str, Any]:
        # BUGGY VERSION:
        # return {"child_field": "validated_child"} # Lost base_field!

        # FIXED VERSION:
        cleaned_data = super().clean()
        cleaned_data["child_field"] = "validated_child"
        return cleaned_data


# ---------------------------------------------------------------------
# Bug 3: Reading `request.POST` Instead of `form.cleaned_data`
# Problem: A view did `title = request.POST['title']` bypassing the form's HTML
# sanitization and type coercion.
# Fix: Use `form.cleaned_data`.
# ---------------------------------------------------------------------
def extract_title_safe(cleaned_data: Dict[str, Any], raw_post: Dict[str, Any]) -> str:
    # BUGGY VERSION:
    # return raw_post.get("title", "")

    # FIXED VERSION:
    return cleaned_data.get("title", "")


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    assert clean_phone_number("+1 (555) 123-4567") == "15551234567"

    # Test Bug 2 fix
    form = ChildForm()
    res = form.clean()
    assert "base_field" in res and "child_field" in res

    # Test Bug 3 fix
    assert extract_title_safe({"title": "Cleaned"}, {"title": "<script>Bad"}) == "Cleaned"

    print("All Day 43 debugging fixes verified successfully!")
