"""
Day 36 Daily Challenge: Django Project Scaffold Generator & Environment Config Validator

Problem:
Create a production-grade Django project configuration manager that:
1. Simulates Django's `settings.py` loading pipeline.
2. Validates `INSTALLED_APPS` dependencies (e.g. `django.contrib.auth` requires `django.contrib.contenttypes`).
3. Validates database engine connection configuration (ENGINE, NAME, USER, PASSWORD, HOST, PORT).
4. Verifies middleware ordering: SecurityMiddleware must come first, CommonMiddleware before CsrfViewMiddleware, etc.
"""
from typing import Dict, List, Any

class SettingsValidator:
    REQUIRED_CORE_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
    
    @staticmethod
    def validate_installed_apps(installed_apps: List[str]) -> List[str]:
        errors = []
        app_set = set(installed_apps)
        
        # Dependency check: auth requires contenttypes
        if "django.contrib.auth" in app_set and "django.contrib.contenttypes" not in app_set:
            errors.append("django.contrib.auth requires django.contrib.contenttypes in INSTALLED_APPS.")
            
        return errors

    @staticmethod
    def validate_database_config(databases: Dict[str, Dict[str, Any]]) -> List[str]:
        errors = []
        if "default" not in databases:
            errors.append("DATABASES setting must contain a 'default' connection.")
            return errors

        default_db = databases["default"]
        required_fields = ["ENGINE", "NAME"]
        for f in required_fields:
            if f not in default_db or not default_db[f]:
                errors.append(f"DATABASES['default'] missing required configuration key '{f}'.")

        if "sqlite3" not in default_db.get("ENGINE", ""):
            # Client-server databases (postgres/mysql) require user and host
            for f in ["USER", "HOST"]:
                if f not in default_db:
                    errors.append(f"Network database engine requires '{f}' field.")
        return errors

    @staticmethod
    def validate_middleware_order(middleware: List[str]) -> List[str]:
        errors = []
        if not middleware:
            return ["MIDDLEWARE list cannot be empty."]

        # SecurityMiddleware should typically be first
        sec_mw = "django.middleware.security.SecurityMiddleware"
        if sec_mw in middleware and middleware[0] != sec_mw:
            errors.append(f"{sec_mw} should be the first middleware executed.")

        # Session must precede Auth
        sess_mw = "django.contrib.sessions.middleware.SessionMiddleware"
        auth_mw = "django.contrib.auth.middleware.AuthenticationMiddleware"
        if sess_mw in middleware and auth_mw in middleware:
            if middleware.index(sess_mw) > middleware.index(auth_mw):
                errors.append("SessionMiddleware must precede AuthenticationMiddleware.")

        return errors


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    validator = SettingsValidator()

    # 1. Test App Dependencies
    apps_invalid = ["django.contrib.auth"]
    errs = validator.validate_installed_apps(apps_invalid)
    assert len(errs) == 1
    assert "contenttypes" in errs[0]

    apps_valid = ["django.contrib.contenttypes", "django.contrib.auth"]
    assert len(validator.validate_installed_apps(apps_valid)) == 0

    # 2. Test Database Config
    db_bad = {}
    assert "default" in validator.validate_database_config(db_bad)[0]

    db_postgres = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "my_db",
            "USER": "postgres_user",
            "HOST": "localhost"
        }
    }
    assert len(validator.validate_database_config(db_postgres)) == 0

    # 3. Test Middleware Ordering
    bad_mw = [
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.security.SecurityMiddleware"
    ]
    mw_errs = validator.validate_middleware_order(bad_mw)
    assert len(mw_errs) == 2  # Security not first + Auth before Session

    good_mw = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware"
    ]
    assert len(validator.validate_middleware_order(good_mw)) == 0

    print("All SettingsValidator challenge tests passed successfully!")
