# Day 43 — Django Forms, `ModelForm` & Validation Lifecycle

## 🎯 Learning Objectives
- Master `forms.Form` (independent forms) vs `forms.ModelForm` (automatically generated from models).
- Master the Form validation lifecycle: `is_valid()`, `full_clean()`, field cleaning, and cross-field cleaning.
- Implement field-level validation using `clean_<fieldname>()` methods.
- Implement cross-field validation using `clean()` and raise `forms.ValidationError`.
- Understand Cross-Site Request Forgery (CSRF) protection tokens (`{% csrf_token %}`).

---

## 📚 Core Backend Concepts

### 1. Form Validation Lifecycle
When `form.is_valid()` is invoked:
1. Field types validate raw input (e.g. `EmailField` verifies regex structure).
2. Field-level clean methods execute: `clean_username()`, `clean_email()`.
3. Cross-field clean method executes: `clean()` (e.g. `password` must match `password_confirmation`).
4. Valid data is stored in `form.cleaned_data`.
5. Invalid data populates `form.errors`.

### 2. Validation Example
```python
from django import forms
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if 'admin' in username:
            raise ValidationError("Usernames containing 'admin' are reserved.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')
        if p1 and p2 and p1 != p2:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data
```

---

## 📅 Today's 3-Hour Structure
- **HOUR 1 (Learn & Concepts)**: Review Form vs ModelForm, clean lifecycle, and complete [`questions.md`](questions.md).
- **HOUR 2 (Practice & Debugging)**: Build clean methods in [`practice.py`](practice.py), and fix validation traps in [`debugging.py`](debugging.py).
- **HOUR 3 (Challenge & Interview)**: Build the Form Validation Engine in [`challenge.py`](challenge.py), complete [`whiteboard.py`](whiteboard.py), and review [`interview.md`](interview.md).
