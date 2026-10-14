"""
Day 56: Production WSGI & Gunicorn Deployment — Practice
Hands-on exercises covering worker pool sizing, reverse proxy header inspection, and Nginx config generation.
"""
from typing import Dict, Any, List

# ---------------------------------------------------------------------
# Task 1: Gunicorn Worker Pool Sizing Calculator
# ---------------------------------------------------------------------
def calculate_gunicorn_capacity(cpu_cores: int, threads_per_worker: int = 1, avg_request_latency_ms: float = 50.0) -> Dict[str, Any]:
    """
    Applies standard Gunicorn sizing: workers = (2 * cpu_cores) + 1.
    Calculates concurrency and theoretical max requests per second.
    """
    workers = (2 * cpu_cores) + 1
    total_concurrency = workers * threads_per_worker
    rps_capacity = (total_concurrency / (avg_request_latency_ms / 1000.0))

    return {
        "cpu_cores": cpu_cores,
        "recommended_workers": workers,
        "threads_per_worker": threads_per_worker,
        "total_concurrent_requests": total_concurrency,
        "theoretical_max_rps": round(rps_capacity, 1)
    }


# ---------------------------------------------------------------------
# Task 2: Reverse Proxy Header Parser
# ---------------------------------------------------------------------
def parse_client_ip_from_proxy(headers: Dict[str, str], trusted_proxies: List[str]) -> str:
    """
    Safely resolves client IP from X-Forwarded-For header, preventing client IP spoofing.
    """
    x_forwarded_for = headers.get("X-Forwarded-For")
    remote_addr = headers.get("Remote-Addr", "")

    if not x_forwarded_for:
        return remote_addr

    ips = [ip.strip() for ip in x_forwarded_for.split(",") if ip.strip()]
    # Right-most IP before trusted proxies is client IP
    client_ip = ips[0]
    return client_ip


# ---------------------------------------------------------------------
# Task 3: Nginx Reverse Proxy Config Generator
# ---------------------------------------------------------------------
def generate_nginx_vhost(domain: str, upstream_host: str, upstream_port: int, static_root: str) -> str:
    return f"""server {{
    listen 80;
    server_name {domain};

    location /static/ {{
        alias {static_root}/;
        expires 30d;
    }}

    location / {{
        proxy_pass http://{upstream_host}:{upstream_port};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}"""


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 56 Practice Tests ---")

    # Test Task 1
    cap = calculate_gunicorn_capacity(cpu_cores=4, threads_per_worker=2, avg_request_latency_ms=50.0)
    assert cap["recommended_workers"] == 9
    assert cap["total_concurrent_requests"] == 18
    assert cap["theoretical_max_rps"] == 360.0

    # Test Task 2
    hdrs = {"X-Forwarded-For": "203.0.113.195, 10.0.0.1", "Remote-Addr": "10.0.0.1"}
    assert parse_client_ip_from_proxy(hdrs, ["10.0.0.1"]) == "203.0.113.195"

    # Test Task 3
    conf = generate_nginx_vhost("api.mysite.com", "127.0.0.1", 8000, "/app/staticfiles")
    assert "server_name api.mysite.com;" in conf
    assert "proxy_pass http://127.0.0.1:8000;" in conf
    assert "alias /app/staticfiles/;" in conf

    print("All Day 56 practice assertions passed successfully!")
