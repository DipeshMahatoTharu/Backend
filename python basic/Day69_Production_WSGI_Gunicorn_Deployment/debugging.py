"""
Day 56: Production WSGI & Gunicorn Deployment — Debugging
Diagnose and fix 3 common production deployment and WSGI traps.
"""
from typing import Dict, Any, Tuple

# ---------------------------------------------------------------------
# Bug 1: Missing `SECURE_PROXY_SSL_HEADER` Causing Infinite Redirect Loop
# Problem: Nginx terminates SSL and forwards HTTP to Gunicorn. Django has
# `SECURE_SSL_REDIRECT = True`, sees HTTP, and returns 301 to HTTPS.
# The browser connects to HTTPS, Nginx forwards HTTP, and Django redirects again!
# Fix: Configure SECURE_PROXY_SSL_HEADER to recognize Nginx's HTTPS flag.
# ---------------------------------------------------------------------
def check_ssl_redirect(environ: Dict[str, str], secure_ssl_header_setting: Tuple[str, str]) -> bool:
    # BUGGY VERSION: Checked only environ.get('HTTPS') which is always None behind Nginx!
    # return environ.get('HTTPS') == 'on'

    # FIXED VERSION:
    header_key, expected_val = secure_ssl_header_setting
    return environ.get(header_key) == expected_val


# ---------------------------------------------------------------------
# Bug 2: Worker Hanging on Large File Uploads (Slowloris Attack)
# Problem: A client on a slow 2G connection took 45 seconds to upload 5MB.
# A sync Gunicorn worker remained blocked for 45 seconds, starving other users.
# Fix: Let Nginx buffer the entire request body before proxying to Gunicorn.
# ---------------------------------------------------------------------
def is_buffering_enabled(nginx_directives: Dict[str, str]) -> bool:
    # BUGGY VERSION:
    # return False

    # FIXED VERSION:
    return nginx_directives.get("proxy_request_buffering", "on") == "on"


# ---------------------------------------------------------------------
# Bug 3: Binding Gunicorn Publicly to `0.0.0.0:8000`
# Problem: Binding Gunicorn to `0.0.0.0:8000` bypassed Nginx rate-limiting,
# allowing attackers to hit Gunicorn directly over the internet.
# Fix: Bind only to localhost `127.0.0.1:8000` or UNIX domain socket.
# ---------------------------------------------------------------------
def validate_gunicorn_bind(bind_address: str) -> bool:
    # BUGGY VERSION: Allowed 0.0.0.0
    # return True

    # FIXED VERSION:
    if bind_address.startswith("0.0.0.0"):
        raise ValueError("Gunicorn should not be bound publicly to 0.0.0.0. Use 127.0.0.1 or a UNIX socket.")
    return True


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    env = {"HTTP_X_FORWARDED_PROTO": "https"}
    setting = ("HTTP_X_FORWARDED_PROTO", "https")
    assert check_ssl_redirect(env, setting) is True

    # Test Bug 2 fix
    assert is_buffering_enabled({"proxy_request_buffering": "on"}) is True

    # Test Bug 3 fix
    try:
        validate_gunicorn_bind("0.0.0.0:8000")
        assert False, "Should raise ValueError on 0.0.0.0 bind"
    except ValueError:
        pass
    assert validate_gunicorn_bind("127.0.0.1:8000") is True
    assert validate_gunicorn_bind("unix:/run/gunicorn.sock") is True

    print("All Day 56 debugging fixes verified successfully!")
