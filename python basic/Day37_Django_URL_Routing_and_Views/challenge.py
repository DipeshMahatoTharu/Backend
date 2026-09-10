"""
Day 37 Daily Challenge: Dynamic URL Resolver & CBV Request Dispatcher

Problem:
Implement a standalone URL routing engine that mimics Django's URL resolution:
1. `path(route, view, name=None)`: Registers routes supporting `<int:param>`, `<str:param>`, and `<slug:param>`.
2. `resolve(path)`: Matches an incoming URI against registered patterns, extracts typed parameters, and returns `(view_func, kwargs)`.
3. `reverse(name, kwargs)`: Reverses a named route given keyword parameters.
"""
import re
from typing import Dict, Any, Callable, Tuple, Optional, List

class URLPattern:
    CONVERTERS = {
        "int": (r"[0-9]+", int),
        "str": (r"[^/]+", str),
        "slug": (r"[-a-zA-Z0-9_]+", str)
    }

    def __init__(self, raw_route: str, view: Callable, name: Optional[str] = None):
        self.raw_route = raw_route
        self.view = view
        self.name = name
        self.param_types: Dict[str, Callable] = {}
        self.regex = self._compile(raw_route)

    def _compile(self, route: str) -> re.Pattern:
        # Convert e.g. "articles/<int:pk>/" to regex r"^articles/(?P<pk>[0-9]+)/$"
        regex_pattern = "^"
        parts = route.strip("/").split("/") if route.strip("/") else []
        for part in parts:
            match = re.match(r"^<([a-z]+):([a-zA-Z_][a-zA-Z0-9_]*)>$", part)
            if match:
                conv_name, param_name = match.groups()
                pattern_str, type_fn = self.CONVERTERS[conv_name]
                self.param_types[param_name] = type_fn
                regex_pattern += f"/(?P<{param_name}>{pattern_str})"
            else:
                regex_pattern += f"/{re.escape(part)}"
        regex_pattern += "/?$"
        return re.compile(regex_pattern)

    def match(self, path: str) -> Optional[Dict[str, Any]]:
        normalized = "/" + path.strip("/") if path.strip("/") else "/"
        m = self.regex.match(normalized)
        if not m:
            return None
        raw_kwargs = m.groupdict()
        typed_kwargs = {}
        for k, v in raw_kwargs.items():
            type_fn = self.param_types.get(k, str)
            typed_kwargs[k] = type_fn(v)
        return typed_kwargs

class URLResolver:
    def __init__(self):
        self.patterns: List[URLPattern] = []
        self.named_routes: Dict[str, URLPattern] = {}

    def path(self, route: str, view: Callable, name: Optional[str] = None):
        pattern = URLPattern(route, view, name)
        self.patterns.append(pattern)
        if name:
            self.named_routes[name] = pattern

    def resolve(self, path: str) -> Tuple[Callable, Dict[str, Any]]:
        for pat in self.patterns:
            kwargs = pat.match(path)
            if kwargs is not None:
                return pat.view, kwargs
        raise LookupError(f"Page not found: 404 for '{path}'")

    def reverse(self, name: str, **kwargs) -> str:
        if name not in self.named_routes:
            raise KeyError(f"Reverse for '{name}' not found.")
        pattern = self.named_routes[name]
        route = pattern.raw_route
        for k, v in kwargs.items():
            # Replace <type:k> with string value
            route = re.sub(rf"<[a-z]+:{k}>", str(v), route)
        return "/" + route.strip("/") + "/"


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    resolver = URLResolver()

    def user_list(request, **kwargs): return "user_list"
    def user_detail(request, **kwargs): return f"user_{kwargs.get('pk')}"
    def article_by_slug(request, **kwargs): return f"article_{kwargs.get('slug')}"

    resolver.path("users/", user_list, name="user-list")
    resolver.path("users/<int:pk>/", user_detail, name="user-detail")
    resolver.path("articles/<slug:slug>/", article_by_slug, name="article-detail")

    # 1. Resolve users/
    fn, kw = resolver.resolve("/users/")
    assert fn(None, **kw) == "user_list"
    assert kw == {}

    # 2. Resolve users/42/ with integer type-casting
    fn, kw = resolver.resolve("/users/42/")
    assert fn(None, **kw) == "user_42"
    assert kw["pk"] == 42
    assert isinstance(kw["pk"], int)

    # 3. Resolve articles/django-deep-dive/
    fn, kw = resolver.resolve("/articles/django-deep-dive/")
    assert kw["slug"] == "django-deep-dive"

    # 4. Reverse resolution
    rev_user = resolver.reverse("user-detail", pk=99)
    assert rev_user == "/users/99/"

    rev_article = resolver.reverse("article-detail", slug="best-practices")
    assert rev_article == "/articles/best-practices/"

    print("All URLResolver challenge tests passed successfully!")
