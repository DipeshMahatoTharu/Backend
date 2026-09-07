
# =====================================================================
# TASK 4: Entry Point Guard & Module Testing
# =====================================================================
# The block below should ONLY execute when this file is run directly,
# never when imported by another backend module or test runner.
from pathlib import Path
from practice import (
    write_log_entries,
    read_error_logs,
    save_config,
    load_config,
    export_users_to_csv,
    import_users_from_csv
)
if __name__ == "__main__":
    test_dir = Path(__file__).resolve().parent / "temp_practice_files"
    
    print("--- Running Day 24 Practice Tasks ---")
    
    # Test Task 1
    log_file = test_dir / "app.log"
    sample_logs = [
        "[INFO] Server started on port 8000",
        "[ERROR] Database connection lost",
        "[WARNING] High memory usage: 85%",
        "[ERROR] Payment gateway timeout"
    ]
    write_log_entries(log_file, sample_logs)
    errors = read_error_logs(log_file)
    print(f"Task 1 (Error Logs Found): {errors}")

    # Test Task 2
    config_file = test_dir / "settings.json"
    default_cfg = {"database": "postgres", "port": 5432, "debug": False}
    save_config(config_file, default_cfg)
    loaded_cfg = load_config(config_file, default_cfg)
    print(f"Task 2 (Loaded Config): {loaded_cfg}")

    # Test Task 3
    csv_file = test_dir / "users.csv"
    users_data = [
        {"id": 101, "name": "Dipesh", "role": "Senior Engineer"},
        {"id": 102, "name": "Anjali", "role": "Data Analyst"}
    ]
    export_users_to_csv(csv_file, users_data)
    imported_users = import_users_from_csv(csv_file)
    print(f"Task 3 (Imported Users): {imported_users}")

    # Cleanup temp directory when finished
    import shutil
    if test_dir.exists():
        shutil.rmtree(test_dir)
        print("Cleaned up temporary practice files.")