# Day 24 Practice — Files, Modules & Packages in Backend Engineering

import json
import csv
from pathlib import Path
from datetime import datetime

# =====================================================================
# TASK 1: Modern File Pathing & Context Managers (pathlib.Path)
# =====================================================================
# In production, never hardcode string paths like "C:\\logs\\app.log".
# Always use pathlib.Path relative to your project base directory.
#
# INSTRUCTIONS:
# 1. Complete `write_log_entries(file_path, entries)`:
#    - Ensure the parent directory of `file_path` exists using `Path.mkdir(parents=True, exist_ok=True)`.
#    - Open the file using a context manager in write mode with UTF-8 encoding.
#    - Write each entry from `entries` on a new line.
# 2. Complete `read_error_logs(file_path)`:
#    - If the file does not exist, return an empty list `[]`.
#    - Open the file using a context manager and return a list of lines that contain "[ERROR]" (stripped of trailing whitespace).

def write_log_entries(file_path: Path, entries: list[str]) -> None:
    # Ensure file_path is a Path object
    path = Path(file_path)
    path.parent.mkdir(parents=True,exist_ok=True)

    # TODO: Open and write entries line by line using UTF-8
    with open(path,"w",encoding="utf-8") as file:
        for entry in entries:
            file.write(entry + "\n")
    
    pass

#  - Open the file using a context manager and return a list of lines that contain "[ERROR]" (stripped of trailing whitespace).
def read_error_logs(file_path: Path) -> list[str]:
   
    path = Path(file_path)
    if  not path.exists():
        return []
    error_list=[]
    with open(path,"r",encoding="utf-8") as file:
        for line in file:
            if "[ERROR]" in line:
                error_list.append(line.strip())
    return error_list
            
    pass


# =====================================================================
# TASK 2: Backend JSON Configuration Manager
# =====================================================================
# Backend APIs load settings (DB hosts, timeouts, secret names) from JSON.
#
# INSTRUCTIONS:
# 1. Complete `save_config(file_path, config_data)`:
#    - Saves the `config_data` dictionary to the path formatted with `indent=4`.
# 2. Complete `load_config(file_path, default_config)`:
#    - If `file_path` does not exist, return `default_config`.
#    - If `file_path` contains invalid/malformed JSON, raise a `ValueError("Invalid JSON configuration")`.
#    - If valid, return the parsed dictionary.

def save_config(file_path: Path, config_data: dict) -> None:
    path = Path(file_path)
    # TODO: Create parent dir and write json with indent=4
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding="utf-8")as file:
        json.dump(config_data,file,indent=4)

    pass


def load_config(file_path: Path, default_config: dict) -> dict:
    path = Path(file_path)
    # TODO: Handle missing file -> return default_config
    if not path.exists():
        return default_config
    try:
        with open(path,"r",encoding="utf-8")as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON configuration")


    

    pass


# =====================================================================
# TASK 3: Database CSV Import & Export (DictReader / DictWriter)
# =====================================================================
# Customer records, invoice reports, and analytics exports rely heavily on CSV.
#
# INSTRUCTIONS:
# 1. Complete `export_users_to_csv(file_path, users)`:
#    - `users` is a list of dicts: `[{"id": 1, "name": "Dipesh", "role": "Backend Dev"}, ...]`
#    - Fieldnames are: `["id", "name", "role"]`.
#    - Use `csv.DictWriter` with `newline=""` and `encoding="utf-8"`.
#    - Make sure to call `writer.writeheader()` before writing rows.
# 2. Complete `import_users_from_csv(file_path)`:
#    - Reads the CSV using `csv.DictReader`.
#    - Casts `"id"` field to `int`.
#    - Returns a list of dicts. If the file is missing, return `[]`.



def export_users_to_csv(file_path: Path, users: list[dict]) -> None:
    path = Path(file_path)
    # TODO: Write CSV with headers ["id", "name", "role"]
   # users=[{"id": 1, "name": "Dipesh", "role": "Backend Dev"}]
    with open(path,"w",newline="",encoding="utf-8")as file:
        writer=csv.DictWriter(file,fieldnames=["id","name","role"])
        writer.writeheader()
        writer.writerows(users)
                        
    pass


def import_users_from_csv(file_path: Path) -> list[dict]:
    path = Path(file_path)
    user=[]
    # TODO: Read CSV, convert "id" to int, and return list of dicts
    if not path.exists():
        return []
    
    with open(path,"r",newline="",encoding="utf-8")as file:
        reader=csv.DictReader(file,fieldnames=["id"])
        for row in reader:
            row["id"]=int(row["id"]) 
            user.append(row)
        return user
    pass

