# Day 25 Practice — Type Hints, Dataclasses & Clean Python

from dataclasses import dataclass, field
from typing import Optional, Literal, Any
from datetime import datetime

# =====================================================================
# TASK 1: Type-Annotated Backend Query Parser
# =====================================================================
# In web frameworks like Django and FastAPI, request query parameters
# arrive as strings. We must validate and convert them into strict types.
#
# INSTRUCTIONS:
# 1. Complete `parse_pagination_params`:
#    - Parameters:
#      * `page`: str | int | None (defaults to None)
#      * `page_size`: str | int | None (defaults to None)
#    - Return type: `tuple[int, int]` -> (page_number, limit)
#    - Logic: Convert strings to ints. If value is None or <= 0, use defaults:
#      page = 1, page_size = 20.
#    - If string cannot be parsed to an int, raise `ValueError("Invalid pagination")`.

def parse_pagination_params(
    page: str | int | None = None,
    page_size: str | int | None = None
) -> tuple[int, int]:
    # TODO: Implement type-safe pagination parsing
    pass


# =====================================================================
# TASK 2: Immutable Database Configuration Dataclass
# =====================================================================
# Configuration objects should not be altered accidentally during runtime.
#
# INSTRUCTIONS:
# 1. Define a `@dataclass(frozen=True)` named `DatabaseConfig`:
#    - `host`: str
#    - `port`: int = 5432
#    - `database_name`: str = "app_db"
#    - `user`: str = "postgres"
#    - `password`: str = "secret"
# 2. Add a property `connection_url(self) -> str`:
#    - Returns: `"postgresql://{user}:{password}@{host}:{port}/{database_name}"`

@dataclass(frozen=True)
class DatabaseConfig:
    # TODO: Declare fields and connection_url property
    pass


# =====================================================================
# TASK 3: Dataclass with Field Factory & Post-Init Validation
# =====================================================================
# Build a `UserProfile` dataclass that guards against invalid state.
#
# INSTRUCTIONS:
# 1. Create a `@dataclass` named `UserProfile`:
#    - `user_id`: int
#    - `username`: str
#    - `email`: str
#    - `roles`: list[str] = field(default_factory=lambda: ["viewer"])
#    - `created_at`: datetime = field(default_factory=datetime.utcnow)
# 2. Implement `__post_init__(self)`:
#    - If `username` is empty, raise `ValueError("Username cannot be empty")`.
#    - If `email` does not contain `'@'`, raise `ValueError("Invalid email address")`.

@dataclass
class UserProfile:
    # TODO: Declare fields with safe default_factory and validate in __post_init__
    pass


# =====================================================================
# TASK 4: Typed Pipeline Filter
# =====================================================================
# Implement a function that filters a list of user profiles by role.
#
# INSTRUCTIONS:
# 1. Complete `filter_users_by_role`:
#    - Parameters:
#      * `users`: list[UserProfile]
#      * `role`: str
#    - Returns: list[UserProfile] matching that role in their `roles` list.

def filter_users_by_role(users: list[UserProfile], role: str) -> list[UserProfile]:
    # TODO: Implement filtering
    pass


# =====================================================================
# VERIFICATION SUITE
# =====================================================================
if __name__ == "__main__":
    print("--- Running Day 25 Practice Tasks ---")

    # Test Task 1
    p1, s1 = parse_pagination_params("2", "50")
    print(f"Task 1 (Parsed): page={p1}, page_size={s1}")
    p2, s2 = parse_pagination_params(None, None)
    print(f"Task 1 (Defaults): page={p2}, page_size={s2}")

    # Test Task 2
    db = DatabaseConfig(host="localhost", database_name="production_db")
    print(f"Task 2 (URL): {db.connection_url}")
    # Verify immutability
    try:
        db.port = 9999 # type: ignore
        print("ERROR: DatabaseConfig should be frozen/immutable!")
    except Exception:
        print("Task 2 (Frozen check passed: cannot modify attributes)")

    # Test Task 3 & 4
    u1 = UserProfile(user_id=1, username="dipesh", email="dipesh@test.com", roles=["admin", "developer"])
    u2 = UserProfile(user_id=2, username="anjali", email="anjali@test.com")
    print(f"Task 3 (Created User): {u1.username}, roles: {u1.roles}")
    print(f"Task 3 (Default Role User): {u2.username}, roles: {u2.roles}")

    admins = filter_users_by_role([u1, u2], "admin")
    print(f"Task 4 (Filtered Admins count): {len(admins)}")