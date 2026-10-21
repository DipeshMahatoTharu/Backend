"""
sync_tracker_rows.py
--------------------
Updates revision_tracker.md table rows from generate_and_audit_revisions.DAYS_DATA.
"""

from generate_and_audit_revisions import DAYS_DATA
import re

def sync_table():
    with open("revision_tracker.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Split before the table separator line
    sep = "| :---: | :--- | :---: | :---: | :---: | :--- |\n"
    if sep not in content:
        raise ValueError("Could not find table separator in revision_tracker.md")

    pre_table = content.split(sep)[0] + sep

    rows = []
    for d in range(32, 76):
        data = DAYS_DATA[d]
        topic = f"{data['topic']} ({data['prereqs']})"
        next_rev = f"Day {min(d + 3, 75)}" if d < 73 else "—"
        note = "Current Day — First revision session ready" if d == 32 else ""
        rows.append(f"| **Day {d}** | {topic} | — | `NOT ATTEMPTED` | {next_rev} | {note} |")

    new_content = pre_table + "\n".join(rows) + "\n"

    with open("revision_tracker.md", "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[+] Successfully wrote {len(rows)} updated rows into revision_tracker.md.")

if __name__ == "__main__":
    sync_table()

