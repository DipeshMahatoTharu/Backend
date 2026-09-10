"""
Day 36: Django Project Installation & Structure — Practice
Hands-on exercises covering configuration validation, environment variable extraction, and app registry logic.
"""
import os
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Task 1: Environment Variable Loader with Type Casting
# ---------------------------------------------------------------------
def load_env_config(env_dict: Dict[str, str]) -> Dict[str, Any]:
    """
    Extracts and type-casts essential Django settings:
    - 'DEBUG': boolean ('True'/'1' -> True, 'False'/'0' -> False)
    - 'SECRET_KEY': string, raises ValueError if empty or missing
    - 'ALLOWED_HOSTS': comma-separated string converted to list of strings
    - 'DB_PORT': integer, defaults to 5432
    """
    if not env_dict.get("SECRET_KEY"):
        raise ValueError("SECRET_KEY is mandatory and cannot be empty")

    debug_val = env_dict.get("DEBUG", "False").lower() in ("true", "1", "yes")
    allowed_hosts = [h.strip() for h in env_dict.get("ALLOWED_HOSTS", "").split(",") if h.strip()]
    db_port = int(env_dict.get("DB_PORT", "5432"))

    return {
        "DEBUG": debug_val,
        "SECRET_KEY": env_dict["SECRET_KEY"],
        "ALLOWED_HOSTS": allowed_hosts,
        "DB_PORT": db_port
    }


# ---------------------------------------------------------------------
# Task 2: Production Readiness Security Linter
# ---------------------------------------------------------------------
def check_production_settings(settings: Dict[str, Any]) -> List[str]:
    """
    Inspects settings dictionary and returns a list of security warnings/errors:
    1. If DEBUG is True: 'CRITICAL: DEBUG must be False in production.'
    2. If ALLOWED_HOSTS contains '*' or is empty: 'CRITICAL: ALLOWED_HOSTS must specify explicit domains.'
    3. If len(SECRET_KEY) < 32: 'WARNING: SECRET_KEY is too short (min 32 chars).'
    """
    issues = []
    if settings.get("DEBUG") is True:
        issues.append("CRITICAL: DEBUG must be False in production.")

    hosts = settings.get("ALLOWED_HOSTS", [])
    if not hosts or "*" in hosts:
        issues.append("CRITICAL: ALLOWED_HOSTS must specify explicit domains.")

    secret = settings.get("SECRET_KEY", "")
    if len(secret) < 32:
        issues.append("WARNING: SECRET_KEY is too short (min 32 chars).")

    return issues


# ---------------------------------------------------------------------
# Task 3: Django App Registry Simulator
# ---------------------------------------------------------------------
class MockAppConfig:
    def __init__(self, name: str, verbose_name: Optional[str] = None):
        self.name = name
        self.verbose_name = verbose_name or name.capitalize()

class AppRegistry:
    def __init__(self):
        self._apps: Dict[str, MockAppConfig] = {}

    def register(self, app_name: str, verbose_name: Optional[str] = None):
        if app_name in self._apps:
            raise RuntimeError(f"App '{app_name}' is already registered.")
        self._apps[app_name] = MockAppConfig(app_name, verbose_name)

    def get_app(self, app_name: str) -> MockAppConfig:
        if app_name not in self._apps:
            raise LookupError(f"No installed app with label '{app_name}'.")
        return self._apps[app_name]

    @property
    def installed_apps(self) -> List[str]:
        return list(self._apps.keys())


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 36 Practice Tests ---")

    # Test Task 1
    sample_env = {
        "DEBUG": "False",
        "SECRET_KEY": "django-insecure-supersecretkey1234567890",
        "ALLOWED_HOSTS": "api.domain.com, backend.domain.com",
        "DB_PORT": "5432"
    }
    cfg = load_env_config(sample_env)
    assert cfg["DEBUG"] is False
    assert len(cfg["ALLOWED_HOSTS"]) == 2
    assert cfg["DB_PORT"] == 5432

    # Test Task 2
    bad_settings = {
        "DEBUG": True,
        "ALLOWED_HOSTS": ["*"],
        "SECRET_KEY": "short"
    }
    warnings = check_production_settings(bad_settings)
    assert len(warnings) == 3

    # Test Task 3
    registry = AppRegistry()
    registry.register("accounts", "User Accounts")
    registry.register("billing")
    assert "accounts" in registry.installed_apps
    assert registry.get_app("accounts").verbose_name == "User Accounts"

    try:
        registry.register("accounts")
        assert False, "Duplicate registration should fail"
    except RuntimeError:
        pass

    print("All Day 36 practice assertions passed successfully!")
