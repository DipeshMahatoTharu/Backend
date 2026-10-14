"""
Day 37: Django URL Routing & Views — Practice
Hands-on exercises covering path converters, custom converters, and CBV dispatching.
"""
import re
from typing import Dict, Any, Optional, Callable

# ---------------------------------------------------------------------
# Task 1: Custom Path Converter (Four-Digit Year)
# ---------------------------------------------------------------------
class FourDigitYearConverter:
    regex = r'[0-9]{4}'

    def to_python(self, value: str) -> int:
        return int(value)

    def to_url(self, value: int) -> str:
        return f"{value:04d}"


# ---------------------------------------------------------------------
# Task 2: Custom ISO Date Path Converter
# ---------------------------------------------------------------------
class ISODateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> str:
        # Validate format YYYY-MM-DD
        parts = value.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Invalid calendar date")
        return value

    def to_url(self, value: str) -> str:
        return str(value)


# ---------------------------------------------------------------------
# Task 3: Base CBV Implementation
# ---------------------------------------------------------------------
class MockHttpRequest:
    def __init__(self, method: str = "GET", params: Optional[Dict[str, str]] = None):
        self.method = method.upper()
        self.GET = params or {}

class MockHttpResponse:
    def __init__(self, content: str, status_code: int = 200, content_type: str = "text/html"):
        self.content = content
        self.status_code = status_code
        self.content_type = content_type

class View:
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']

    def dispatch(self, request: MockHttpRequest, *args, **kwargs) -> MockHttpResponse:
        method = request.method.lower()
        if method in self.http_method_names and hasattr(self, method):
            handler = getattr(self, method)
            return handler(request, *args, **kwargs)
        return MockHttpResponse("Method Not Allowed", status_code=405)

    @classmethod
    def as_view(cls):
        def view(request: MockHttpRequest, *args, **kwargs):
            self = cls()
            return self.dispatch(request, *args, **kwargs)
        return view


class ArticleDetailView(View):
    def get(self, request: MockHttpRequest, slug: str) -> MockHttpResponse:
        return MockHttpResponse(f"Displaying article: {slug}", status_code=200)

    def post(self, request: MockHttpRequest, slug: str) -> MockHttpResponse:
        return MockHttpResponse(f"Article {slug} updated", status_code=200)


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 37 Practice Tests ---")

    # Test Task 1
    yr_conv = FourDigitYearConverter()
    assert yr_conv.to_python("2026") == 2026
    assert yr_conv.to_url(2026) == "2026"

    # Test Task 2
    date_conv = ISODateConverter()
    assert date_conv.to_python("2026-09-09") == "2026-09-09"
    try:
        date_conv.to_python("2026-15-40")
        assert False, "Invalid date should raise ValueError"
    except ValueError:
        pass

    # Test Task 3
    view_func = ArticleDetailView.as_view()
    req_get = MockHttpRequest("GET")
    resp_get = view_func(req_get, slug="django-routing-mastery")
    assert resp_get.status_code == 200
    assert "django-routing-mastery" in resp_get.content

    req_delete = MockHttpRequest("DELETE")
    resp_delete = view_func(req_delete, slug="django-routing-mastery")
    assert resp_delete.status_code == 405

    print("All Day 37 practice assertions passed successfully!")
