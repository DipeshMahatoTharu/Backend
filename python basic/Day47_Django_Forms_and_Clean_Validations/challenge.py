"""
Day 43 Daily Challenge: Comprehensive Registration Form Validator Engine

Problem:
Implement a standalone form validator class `UserRegistrationForm` that simulates
Django's complete form validation lifecycle:
1. Field extraction and required-field checks.
2. Field-level cleans:
   - `clean_username()`: Must be alphanumeric, min 4 chars, no reserved names ('admin', 'root').
   - `clean_email()`: Must be valid email format.
3. Form-level clean:
   - `clean()`: Passwords must match and be at least 8 characters.
4. Populates `cleaned_data` on success or `errors` dictionary on failure.
"""
from typing import Dict, Any, List

class ValidationError(Exception):
    pass

class UserRegistrationForm:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.cleaned_data: Dict[str, Any] = {}
        self.errors: Dict[str, List[str]] = {}
        self._is_valid: Optional[bool] = None

    def add_error(self, field: str, message: str):
        if field not in self.errors:
            self.errors[field] = []
        self.errors[field].append(message)

    def is_valid(self) -> bool:
        if self._is_valid is not None:
            return self._is_valid

        self.errors.clear()
        self.cleaned_data.clear()

        # 1. Required fields
        required_fields = ["username", "email", "password", "confirm_password"]
        for f in required_fields:
            val = self.data.get(f)
            if not val:
                self.add_error(f, f"This field is required.")
            else:
                self.cleaned_data[f] = val

        # 2. Field-level cleans
        if "username" in self.cleaned_data:
            uname = str(self.cleaned_data["username"]).strip().lower()
            if len(uname) < 4:
                self.add_error("username", "Username must be at least 4 characters long.")
            elif uname in ("admin", "root", "superuser"):
                self.add_error("username", f"'{uname}' is a reserved username.")
            else:
                self.cleaned_data["username"] = uname

        if "email" in self.cleaned_data:
            email = str(self.cleaned_data["email"]).strip().lower()
            if "@" not in email or "." not in email:
                self.add_error("email", "Enter a valid email address.")
            else:
                self.cleaned_data["email"] = email

        # 3. Form-level clean (Passwords)
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("confirm_password")
        if p1 and p2:
            if len(p1) < 8:
                self.add_error("password", "Password must be at least 8 characters long.")
            if p1 != p2:
                self.add_error("confirm_password", "Passwords do not match.")

        self._is_valid = len(self.errors) == 0
        return self._is_valid


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Valid Form
    valid_payload = {
        "username": "dipesh_dev",
        "email": "dipesh@example.com",
        "password": "SuperSecurePassword123!",
        "confirm_password": "SuperSecurePassword123!"
    }
    form = UserRegistrationForm(valid_payload)
    assert form.is_valid() is True
    assert form.cleaned_data["username"] == "dipesh_dev"
    assert len(form.errors) == 0

    # 2. Invalid Form (Reserved username + Mismatched passwords)
    invalid_payload = {
        "username": "admin",
        "email": "not-an-email",
        "password": "short",
        "confirm_password": "different_password"
    }
    bad_form = UserRegistrationForm(invalid_payload)
    assert bad_form.is_valid() is False
    assert "reserved" in bad_form.errors["username"][0]
    assert "valid email" in bad_form.errors["email"][0]
    assert "at least 8" in bad_form.errors["password"][0]
    assert "do not match" in bad_form.errors["confirm_password"][0]

    print("All UserRegistrationForm challenge tests passed successfully!")
