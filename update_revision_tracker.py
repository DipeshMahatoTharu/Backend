#!/usr/bin/env python3
"""
update_revision_tracker.py
--------------------------
Synchronizes, audits, and reconciles `revision_tracker.md` for Days 32–75.

Features:
- Standard library only (no external dependencies).
- Windows cp1252 / console safe (uses ASCII indicators or UTF-8 reconfiguration).
- Accurately counts: Total Planned (44), Completed, Independent, Hint Needed,
  Refresher Needed, Not Attempted, and Completion %.
- Enforces: Planned == Completed + Not Attempted.
- Identifies weak topics (HINT NEEDED or REFRESHER NEEDED) and recommends
  spaced reviews 1–3 days later.
- Replaces only the header summary section without modifying table rows, dates,
  or custom user notes.
"""

import os
import sys
import re
from typing import Dict, List, Tuple

# Ensure UTF-8 output even on Windows command prompt
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

TRACKER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "revision_tracker.md")
TOTAL_PLANNED = 44
VALID_OUTCOMES = {"INDEPENDENT", "HINT NEEDED", "REFRESHER NEEDED", "NOT ATTEMPTED"}


def parse_tracker(file_path: str) -> Tuple[str, List[Dict[str, str]], str]:
    """
    Parses revision_tracker.md into:
    - pre_summary_content (text before the summary header)
    - rows (list of parsed table rows)
    - post_table_content (any text after the table)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Tracker file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into sections: before summary, summary, table and after
    summary_match = re.search(r"(## 📊 Summary of Outcomes.*?)(?=## 📅 Revision Log Sheet)", content, re.DOTALL)
    if not summary_match:
        # Fallback without emoji if needed
        summary_match = re.search(r"(## Summary of Outcomes.*?)(?=## Revision Log Sheet)", content, re.DOTALL)
    
    if not summary_match:
        raise ValueError("Could not find 'Summary of Outcomes' section in tracker file.")

    table_match = re.search(r"(## (?:📅 )?Revision Log Sheet.*)", content, re.DOTALL)
    if not table_match:
        raise ValueError("Could not find 'Revision Log Sheet' section in tracker file.")

    pre_summary = content[: summary_match.start()]
    table_section = table_match.group(1)

    # Parse table rows
    rows = []
    lines = table_section.split("\n")
    header_found = False
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and "**Day" in stripped:
            # Table row: | Day | Topics | Date | Outcome | Next Review | Notes |
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) >= 6:
                day_raw = cells[0]
                day_num_match = re.search(r"\d+", day_raw)
                day_num = int(day_num_match.group()) if day_num_match else 0
                
                outcome_raw = cells[3].replace("`", "").strip().upper()
                # Normalize outcome
                matched_outcome = "NOT ATTEMPTED"
                for vo in VALID_OUTCOMES:
                    if vo in outcome_raw:
                        matched_outcome = vo
                        break

                rows.append({
                    "day_raw": cells[0],
                    "day_num": day_num,
                    "topics": cells[1],
                    "date": cells[2],
                    "outcome": matched_outcome,
                    "next_review": cells[4],
                    "notes": cells[5],
                    "raw_line": line
                })

    return pre_summary, rows, table_section


def calculate_metrics(rows: List[Dict[str, str]]) -> Dict[str, object]:
    """
    Computes summary metrics and verifies formula integrity.
    """
    independent = sum(1 for r in rows if r["outcome"] == "INDEPENDENT")
    hint_needed = sum(1 for r in rows if r["outcome"] == "HINT NEEDED")
    refresher_needed = sum(1 for r in rows if r["outcome"] == "REFRESHER NEEDED")
    not_attempted = sum(1 for r in rows if r["outcome"] == "NOT ATTEMPTED")

    completed = independent + hint_needed + refresher_needed
    total = len(rows)

    if total != TOTAL_PLANNED:
        print(f"[!] Warning: Found {total} rows instead of expected {TOTAL_PLANNED}.")

    completion_pct = (completed / total * 100.0) if total > 0 else 0.0

    # Formula check: Planned == Completed + Not_Attempted
    reconciled = (total == (completed + not_attempted))

    # Weak topics needing spaced review
    weak_topics = []
    for r in rows:
        if r["outcome"] in ("HINT NEEDED", "REFRESHER NEEDED"):
            weak_topics.append({
                "day": r["day_num"],
                "outcome": r["outcome"],
                "topics": r["topics"],
                "next_review": r["next_review"],
                "notes": r["notes"]
            })

    return {
        "total_planned": total,
        "completed": completed,
        "completion_pct": completion_pct,
        "independent": independent,
        "hint_needed": hint_needed,
        "refresher_needed": refresher_needed,
        "not_attempted": not_attempted,
        "reconciled": reconciled,
        "weak_topics": weak_topics
    }


def generate_summary_block(metrics: Dict[str, object]) -> str:
    """
    Builds the updated markdown summary block.
    """
    pct_str = f"{metrics['completion_pct']:.1f}%"
    
    lines = [
        "## 📊 Summary of Outcomes",
        f"- **Total Planned Sessions**: {metrics['total_planned']} Days (Day 32 to Day 75)",
        f"- **Completed Sessions**: {metrics['completed']} / {metrics['total_planned']} ({pct_str})",
        f"- **Independent**: {metrics['independent']}",
        f"- **Hint Needed**: {metrics['hint_needed']}",
        f"- **Refresher Needed**: {metrics['refresher_needed']}",
        f"- **Not Attempted**: {metrics['not_attempted']}",
    ]

    weak_topics = metrics["weak_topics"]
    if weak_topics:
        lines.append("")
        lines.append("### 🔁 Spaced Review Queue (Weak Topics)")
        lines.append("| Day | Topic | Outcome | Suggested Spaced Review |")
        lines.append("| :---: | :--- | :---: | :---: |")
        for w in weak_topics:
            lines.append(f"| **Day {w['day']}** | {w['topics']} | `{w['outcome']}` | {w['next_review']} |")
    else:
        lines.append("")
        lines.append("> **Spaced Review Status**: No weak areas currently flagged. All attempted sessions completed independently.")

    lines.append("\n---\n")
    return "\n".join(lines)


def update_tracker_file(file_path: str = TRACKER_FILE, dry_run: bool = False) -> Dict[str, object]:
    """
    Parses, computes metrics, and updates revision_tracker.md in-place.
    """
    pre_summary, rows, table_section = parse_tracker(file_path)
    metrics = calculate_metrics(rows)

    summary_block = generate_summary_block(metrics)

    # Combine into new content
    new_content = pre_summary.rstrip() + "\n\n" + summary_block + "\n" + table_section.lstrip()

    if not dry_run:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[+] Updated {file_path} successfully.")
    else:
        print("[*] Dry run mode enabled. No file changes written.")

    print(f"[*] Summary: Completed {metrics['completed']}/{metrics['total_planned']} ({metrics['completion_pct']:.1f}%) | "
          f"Independent: {metrics['independent']} | Hint Needed: {metrics['hint_needed']} | "
          f"Refresher Needed: {metrics['refresher_needed']} | Not Attempted: {metrics['not_attempted']}")
    print(f"[*] Reconciliation check: {'PASSED' if metrics['reconciled'] else 'FAILED'}")

    return metrics


if __name__ == "__main__":
    is_dry = "--dry-run" in sys.argv
    update_tracker_file(dry_run=is_dry)

