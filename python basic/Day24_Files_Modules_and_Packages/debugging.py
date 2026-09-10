# Day 24 Debugging — Files, Modules & Resource Management

from pathlib import Path
import json

# =====================================================================
# BUGGY SCENARIO 1: The File Descriptor Leak (Windows File Locking)
# =====================================================================
# Goal: Write sensitive customer transaction logs.
# Problem: The developer opened the file without a context manager.
# If an error occurs midway through writing, the file handle remains open.
# On Windows, this locks the file and prevents other processes from deleting
# or reading it. On Linux servers, it exhausts OS file descriptors.

def buggy_write_transactions(file_path: str, transactions: list[dict]):
    # f = open(file_path, "w")
    with open(file_path,"w",encoding="utf-8")as f:
        
        for tx in transactions:
            try:
                if tx["amount"] == True
                    return tx["amount"]
            except KeyError:
                raise  "Please enter the key"
            # If tx is missing "amount", a KeyError is raised here
            # and f.close() is NEVER called!
            f.write(f"TX {tx['id']}: ${tx['amount']}\n")
       

# ---------------------------------------------------------------------
# QUESTION: Why is opening files with raw open() and manual close() dangerous?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite using a `with open(...)` context manager and defensive key access.
# ---------------------------------------------------------------------
def fixed_write_transactions(file_path: Path, transactions: list[dict]):
    pass


# =====================================================================
# BUGGY SCENARIO 2: The Hardcoded OS Path Traps
# =====================================================================
# Goal: Locate the backend database configuration relative to project root.
# Problem: The developer concatenated strings using Windows backslashes (`\`).
# When this code is deployed to an Ubuntu Docker container in production,
# the path resolution fails completely with `FileNotFoundError`.

def buggy_get_database_path():
    # Hardcoded Windows path string concatenation
    base_folder = "C:\\projects\\my_backend_app"
    config_path = base_folder + "\\config\\database.json"
    return config_path
#
# CORRECTED CODE:
# TODO: Rewrite to return a cross-platform Path object resolved relative to __file__.
# ---------------------------------------------------------------------
def fixed_get_database_path() -> Path:
    pass


# =====================================================================
# BUGGY SCENARIO 3: Crashing on Corrupted JSON Payloads
# =====================================================================
# Goal: Read incoming webhook payloads stored on disk.
# Problem: If a webhook writes a truncated or empty file (0 bytes),
# json.load(f) crashes with `json.decoder.JSONDecodeError`, bringing down
# the worker process.

def buggy_read_webhook(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        # If file is empty or corrupted, unhandled JSONDecodeError crashes the service!
        data = json.load(f)
        return data

# ---------------------------------------------------------------------
# QUESTION: How should backend file ingestion defensively handle empty or corrupt payloads?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite with try/except to safely handle FileNotFoundError and JSONDecodeError.
# ---------------------------------------------------------------------
def fixed_read_webhook(file_path: Path) -> dict:
    pass