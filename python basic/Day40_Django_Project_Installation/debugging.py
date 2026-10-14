"""
Day 36: Django Project Installation & Structure — Debugging
Diagnose and fix 3 common Django configuration errors.
"""
from typing import Dict, Any, List

# ---------------------------------------------------------------------
# Bug 1: Hardcoded Secret Key and DEBUG in Production
# Problem: A developer checked `DEBUG = True` and hardcoded SECRET_KEY into Git.
# Fix: Load securely from environment with sensible fallbacks for dev only.
# ---------------------------------------------------------------------
def get_security_settings(env: Dict[str, str]) -> Dict[str, Any]:
    # BUGGY VERSION:
    # return {
    #     "DEBUG": True,
    #     "SECRET_KEY": "django-insecure-38491823901"
    # }

    # FIXED VERSION:
    secret_key = env.get("DJANGO_SECRET_KEY")
    debug = env.get("DJANGO_DEBUG", "False").lower() in ("true", "1")
    if not debug and not secret_key:
        raise ValueError("DJANGO_SECRET_KEY must be provided in production!")

    return {
        "DEBUG": debug,
        "SECRET_KEY": secret_key or "django-insecure-local-dev-fallback"
    }


# ---------------------------------------------------------------------
# Bug 2: Forgotten App in INSTALLED_APPS
# Problem: A developer created a new app 'payments', wrote models, but migrations
# fail with "No changes detected in app 'payments'".
# Fix: App must be registered in INSTALLED_APPS.
# ---------------------------------------------------------------------
def register_installed_apps(base_apps: List[str], new_app: str) -> List[str]:
    # BUGGY VERSION:
    # return base_apps # Failed to append new_app

    # FIXED VERSION:
    apps = list(base_apps)
    if new_app not in apps:
        apps.append(new_app)
    return apps


# ---------------------------------------------------------------------
# Bug 3: ALLOWED_HOSTS Domain Matching
# Problem: The backend is deployed at `api.example.com`, but ALLOWED_HOSTS is
# configured as `['example.com']`, returning 400 Bad Request to all API traffic.
# Fix: Include subdomains or use leading dot `.example.com` to match all subdomains.
# ---------------------------------------------------------------------
def is_host_allowed(host: str, allowed_hosts: List[str]) -> bool:
    # BUGGY VERSION:
    # return host in allowed_hosts # Fails for api.example.com when allowed is ['.example.com']

    # FIXED VERSION:
    for pattern in allowed_hosts:
        if pattern == "*":
            return True
        if pattern.startswith("."):
            # .example.com matches example.com and api.example.com
            domain = pattern[1:]
            if host == domain or host.endswith("." + domain):
                return True
        elif host == pattern:
            return True
    return False


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    prod_env = {"DJANGO_DEBUG": "False", "DJANGO_SECRET_KEY": "super-strong-prod-secret"}
    sec = get_security_settings(prod_env)
    assert sec["DEBUG"] is False
    assert sec["SECRET_KEY"] == "super-strong-prod-secret"

    # Test Bug 2 fix
    core_apps = ["django.contrib.auth", "django.contrib.contenttypes"]
    updated = register_installed_apps(core_apps, "payments")
    assert "payments" in updated

    # Test Bug 3 fix
    allowed = [".example.com", "localhost"]
    assert is_host_allowed("api.example.com", allowed) is True
    assert is_host_allowed("example.com", allowed) is True
    assert is_host_allowed("attacker.com", allowed) is False

    print("All Day 36 debugging fixes verified successfully!")
