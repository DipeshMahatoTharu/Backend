"""
Day 43: Django Forms & Clean Validations — Practice
Hands-on exercises covering field cleaning, cross-field validation, and error dictionary mapping.
"""
from typing import Dict, Any, List, Optional

class ValidationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

# ---------------------------------------------------------------------
# Task 1: Field-Level Clean Method
# ---------------------------------------------------------------------
def clean_corporate_email(email_str: str) -> str:
    """
    Validates and normalizes email:
    - Strips whitespace and lowercases.
    - Rejects non-corporate domains ('@gmail.com', '@yahoo.com').
    """
    cleaned = email_str.strip().lower()
    if not "@" in cleaned or "." not in cleaned:
        raise ValidationError("Enter a valid email address.")
    
    banned_domains = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
    for d in banned_domains:
        if cleaned.endswith(d):
            raise ValidationError("Personal email providers are not permitted. Please use your corporate email.")
    return cleaned


# ---------------------------------------------------------------------
# Task 2: Cross-Field Password Matcher
# ---------------------------------------------------------------------
def clean_password_confirmation(cleaned_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Verifies that 'password' and 'confirm_password' match exactly.
    """
    p1 = cleaned_data.get("password")
    p2 = cleaned_data.get("confirm_password")

    if p1 and p2 and p1 != p2:
        raise ValidationError("The two password fields didn't match.")
    return cleaned_data


# ---------------------------------------------------------------------
# Task 3: Error Formatter for API/Template Rendering
# ---------------------------------------------------------------------
def format_form_errors(errors: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Flattens a dictionary of field errors into a single clean string per field.
    """
    return {field: "; ".join(err_list) for field, err_list in errors.items()}


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 43 Practice Tests ---")

    # Test Task 1
    assert clean_corporate_email("  DIPESH@Company.com ") == "dipesh@company.com"
    try:
        clean_corporate_email("user@gmail.com")
        assert False, "Should raise ValidationError on gmail.com"
    except ValidationError:
        pass

    # Test Task 2
    valid_data = {"password": "SecretPassword123!", "confirm_password": "SecretPassword123!"}
    assert clean_password_confirmation(valid_data) == valid_data

    invalid_data = {"password": "Pass1", "confirm_password": "Pass2"}
    try:
        clean_password_confirmation(invalid_data)
        assert False, "Should raise ValidationError"
    except ValidationError:
        pass

    # Test Task 3
    raw_errs = {"email": ["Enter a valid email.", "Corporate domain required."]}
    flat = format_form_errors(raw_errs)
    assert flat["email"] == "Enter a valid email.; Corporate domain required."

    print("All Day 43 practice assertions passed successfully!")
