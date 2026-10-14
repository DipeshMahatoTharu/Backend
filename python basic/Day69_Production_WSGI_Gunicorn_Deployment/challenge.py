"""
Day 56 Daily Challenge: Gunicorn & Nginx Reverse Proxy Architecture Simulator

Problem:
Implement a simulation of the Nginx -> Gunicorn -> Django pipeline:
1. `NginxProxy`:
   - Inspects static file paths: directly returns assets without waking Gunicorn.
   - Forwards dynamic requests, injecting `X-Forwarded-For` and `X-Forwarded-Proto`.
2. `GunicornMaster`:
   - Manages a pool of worker processes.
   - Enforces request timeouts: aborts requests taking longer than `timeout_seconds`.
3. `DjangoApp`:
   - Inspects `SECURE_PROXY_SSL_HEADER` to verify HTTPS status.
   - Returns response.
"""
import time
from typing import Dict, Any, Optional, Tuple

class DjangoApp:
    def __init__(self, secure_ssl_redirect: bool = True):
        self.secure_ssl_redirect = secure_ssl_redirect

    def handle(self, environ: Dict[str, Any]) -> Tuple[int, Dict[str, str], str]:
        proto = environ.get("HTTP_X_FORWARDED_PROTO", "http")
        if self.secure_ssl_redirect and proto != "https":
            # Redirect to HTTPS
            return 301, {"Location": f"https://{environ.get('HTTP_HOST')}{environ.get('PATH_INFO')}"}, ""

        path = environ.get("PATH_INFO", "/")
        return 200, {"Content-Type": "application/json"}, f'{{"path": "{path}", "status": "ok"}}'


class GunicornWorkerPool:
    def __init__(self, app: DjangoApp, worker_count: int = 3, timeout_seconds: float = 0.5):
        self.app = app
        self.worker_count = worker_count
        self.timeout_seconds = timeout_seconds

    def execute_request(self, environ: Dict[str, Any], sim_latency: float = 0.01) -> Tuple[int, Dict[str, str], str]:
        if sim_latency > self.timeout_seconds:
            return 504, {}, "Gateway Timeout (Worker killed)"
        return self.app.handle(environ)


class NginxReverseProxy:
    def __init__(self, gunicorn_pool: GunicornWorkerPool, static_files: Dict[str, str]):
        self.gunicorn = gunicorn_pool
        self.static_files = static_files

    def dispatch(self, method: str, path: str, headers: Dict[str, str], client_ip: str, sim_latency: float = 0.01) -> Tuple[int, Dict[str, str], str]:
        # 1. Check static cache
        if path.startswith("/static/"):
            asset_key = path[len("/static/"):]
            if asset_key in self.static_files:
                return 200, {"Content-Type": "text/css", "X-Served-By": "Nginx"}, self.static_files[asset_key]
            return 404, {"X-Served-By": "Nginx"}, "Static file not found"

        # 2. Forward to Gunicorn
        environ = {
            "REQUEST_METHOD": method,
            "PATH_INFO": path,
            "HTTP_HOST": headers.get("Host", "localhost"),
            "HTTP_X_FORWARDED_FOR": client_ip,
            "HTTP_X_FORWARDED_PROTO": headers.get("X-Forwarded-Proto", "https"),
        }
        return self.gunicorn.execute_request(environ, sim_latency=sim_latency)


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    django = DjangoApp(secure_ssl_redirect=True)
    gunicorn = GunicornWorkerPool(django, worker_count=4, timeout_seconds=0.1)
    static_assets = {"css/style.css": "body { color: black; }"}
    nginx = NginxReverseProxy(gunicorn, static_assets)

    # 1. Static asset served directly by Nginx (Gunicorn not touched!)
    status, hdrs, body = nginx.dispatch("GET", "/static/css/style.css", {}, client_ip="192.168.1.5")
    assert status == 200
    assert hdrs["X-Served-By"] == "Nginx"
    assert "body {" in body

    # 2. Dynamic API request over HTTPS
    status, hdrs, body = nginx.dispatch("GET", "/api/v1/orders", {"Host": "api.site.com", "X-Forwarded-Proto": "https"}, client_ip="192.168.1.5")
    assert status == 200
    assert "orders" in body

    # 3. Insecure HTTP request -> 301 Redirect to HTTPS
    status, hdrs, body = nginx.dispatch("GET", "/api/v1/orders", {"Host": "api.site.com", "X-Forwarded-Proto": "http"}, client_ip="192.168.1.5")
    assert status == 301
    assert "https://" in hdrs["Location"]

    # 4. Gunicorn Worker Timeout
    status, hdrs, body = nginx.dispatch("GET", "/api/slow", {"X-Forwarded-Proto": "https"}, client_ip="1.2.3.4", sim_latency=0.3)
    assert status == 504
    assert "Timeout" in body

    print("All Nginx & Gunicorn challenge tests passed successfully!")
