"""
============================================================
DAY 51 — WHITEBOARD / BLANK-PAGE CODING CHALLENGE
============================================================

Topic: POSIX vs Windows Shell cURL Command Formatter

------------------------------------------------------------
1. PROBLEM STATEMENT:
------------------------------------------------------------
Implement a cross-platform cURL command generator:
`generate_curl_script(method: str, url: str, headers: dict, json_payload: dict, target_os: str = "posix") -> str`

Requirements:
- `target_os="posix"` (Linux/macOS Bash):
  - Single-quote wrapped strings: `-d '{"key": "val"}'`.
  - Backslash line continuations: `\
`.
- `target_os="windows"` (Windows PowerShell):
  - Escaped double quotes: `-d "{"key": "val"}"`.
  - Backtick line continuations: `` `
 ``.

------------------------------------------------------------
2. REQUIREMENTS:
------------------------------------------------------------
- Return valid single-string command with proper line breaks.

============================================================
MY APPROACH:
============================================================
1. Format JSON string compactly using `json.dumps()`.
2. Format line continuation: `\` for posix, `` ` `` for windows.
3. Escape payload appropriately for the shell.
4. Assemble and return string.
"""
import json
from typing import Dict, Any

def generate_curl_script(
    method: str,
    url: str,
    headers: Dict[str, str],
    json_payload: Dict[str, Any],
    target_os: str = "posix"
) -> str:
    method = method.upper()
    line_cont = " \\\n  " if target_os == "posix" else " `\n  "
    raw_json = json.dumps(json_payload)

    parts = [f"curl -X {method} '{url}'"]

    for k, v in headers.items():
        parts.append(f"-H '{k}: {v}'")

    if target_os == "posix":
        parts.append(f"-d '{raw_json}'")
    else:
        escaped_json = raw_json.replace('"', '\\"')
        parts.append(f'-d "{escaped_json}"')

    return line_cont.join(parts)


# ------------------------------------------------------------
# Verification
# ------------------------------------------------------------
if __name__ == "__main__":
    headers = {"Content-Type": "application/json"}
    payload = {"id": 1, "title": "Test Post"}

    # 1. POSIX
    posix_cmd = generate_curl_script("POST", "https://api.com/items", headers, payload, target_os="posix")
    assert " \\\n  " in posix_cmd
    assert "-d '{\"id\": 1, \"title\": \"Test Post\"}'" in posix_cmd

    # 2. Windows PowerShell
    win_cmd = generate_curl_script("POST", "https://api.com/items", headers, payload, target_os="windows")
    assert " `\n  " in win_cmd
    assert '-d "{\\"id\\": 1, \\"title\\": \\"Test Post\\"}"' in win_cmd

    print("Whiteboard Day 51 challenge passed successfully!")
