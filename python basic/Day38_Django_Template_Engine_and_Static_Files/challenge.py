"""
Day 38 Daily Challenge: Minimal Template Engine & Static Asset Resolver

Problem:
Implement a lightweight template renderer that simulates Django's core DTL:
1. Variable Interpolation: `{{ variable }}` replaced by context value with auto-escaping.
2. Filters: `{{ variable|filter }}` supporting `|upper`, `|lower`, and `|safe` (bypasses escaping).
3. Loops: `{% for item in items %}...{% endfor %}` repeated for each element in iterable.
4. Static Tag: `{% static 'path' %}` replaced with `STATIC_URL + path`.
"""
import re
import html
from typing import Dict, Any

class MiniTemplateEngine:
    def __init__(self, static_url: str = "/static/"):
        self.static_url = static_url.rstrip("/") + "/"

    def render(self, template_str: str, context: Dict[str, Any]) -> str:
        output = template_str

        # 1. Process static tags: {% static 'css/app.css' %}
        output = re.sub(
            r"""{%\s*static\s*['"]([^'"]+)['"]\s*%}""",
            lambda m: f"{self.static_url}{m.group(1).lstrip('/')}",
            output
        )

        # 2. Process for loops: {% for item in items %}...{% endfor %}
        loop_pattern = re.compile(r"{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%}(.*?){%\s*endfor\s*%}", re.DOTALL)
        def replace_loop(match):
            var_name = match.group(1)
            list_name = match.group(2)
            body = match.group(3)
            items = context.get(list_name, [])
            rendered_blocks = []
            for it in items:
                sub_ctx = dict(context)
                sub_ctx[var_name] = it
                rendered_blocks.append(self.render(body, sub_ctx))
            return "".join(rendered_blocks)

        output = loop_pattern.sub(replace_loop, output)

        # 3. Process variables & filters: {{ var }} or {{ var|filter }}
        var_pattern = re.compile(r"{{\s*([a-zA-Z0-9_\.]+)(\|([a-zA-Z0-9_]+))?\s*}}")
        def replace_var(match):
            var_path = match.group(1)
            filter_name = match.group(3)

            # Resolve variable
            parts = var_path.split(".")
            curr = context
            for p in parts:
                if isinstance(curr, dict) and p in curr:
                    curr = curr[p]
                else:
                    curr = ""
                    break

            val_str = str(curr)

            # Apply filter
            is_safe = False
            if filter_name == "upper":
                val_str = val_str.upper()
            elif filter_name == "lower":
                val_str = val_str.lower()
            elif filter_name == "safe":
                is_safe = True

            return val_str if is_safe else html.escape(val_str)

        output = var_pattern.sub(replace_var, output)
        return output


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    engine = MiniTemplateEngine(static_url="/assets/")

    tpl = """
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <h1>Welcome, {{ user.name|upper }}!</h1>
    <ul>
    {% for item in items %}
      <li>{{ item }}</li>
    {% endfor %}
    </ul>
    <div>{{ raw_markup|safe }}</div>
    <div>{{ dangerous_input }}</div>
    """

    data = {
        "user": {"name": "Dipesh"},
        "items": ["Python", "Django", "PostgreSQL"],
        "raw_markup": "<span class='badge'>Active</span>",
        "dangerous_input": "<script>alert(1)</script>"
    }

    rendered = engine.render(tpl, data)
    assert "/assets/css/style.css" in rendered
    assert "Welcome, DIPESH!" in rendered
    assert "<li>Python</li>" in rendered
    assert "<li>Django</li>" in rendered
    assert "<span class='badge'>Active</span>" in rendered  # Unescaped because of |safe
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in rendered  # Escaped!

    print("All MiniTemplateEngine challenge tests passed successfully!")
