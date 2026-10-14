"""
Day 39: Django Database Models — Practice
Hands-on exercises covering field definitions, DDL generation, and model metadata inspection.
"""
from typing import Dict, Any, List, Optional

# ---------------------------------------------------------------------
# Task 1: Field Definition & Constraint Validator
# ---------------------------------------------------------------------
class Field:
    def __init__(self, field_type: str, null: bool = False, blank: bool = False, max_length: Optional[int] = None, unique: bool = False):
        self.field_type = field_type
        self.null = null
        self.blank = blank
        self.max_length = max_length
        self.unique = unique

        # Linting validation
        if field_type in ("CharField", "SlugField") and not max_length:
            raise ValueError(f"{field_type} must define 'max_length'.")
        if field_type in ("CharField", "TextField") and null and not unique:
            raise ValueError(f"Avoid null=True on {field_type} unless unique=True.")

    def to_sql_column(self, col_name: str) -> str:
        sql_types = {
            "CharField": f"VARCHAR({self.max_length})",
            "TextField": "TEXT",
            "IntegerField": "INTEGER",
            "BooleanField": "BOOLEAN"
        }
        sql_type = sql_types.get(self.field_type, "VARCHAR(255)")
        null_clause = "NULL" if self.null else "NOT NULL"
        unique_clause = " UNIQUE" if self.unique else ""
        return f"{col_name} {sql_type} {null_clause}{unique_clause}"


# ---------------------------------------------------------------------
# Task 2: Model Metaclass Simulator
# ---------------------------------------------------------------------
class ModelMeta:
    def __init__(self, db_table: str, ordering: Optional[List[str]] = None):
        self.db_table = db_table
        self.ordering = ordering or ["id"]

class BaseModel:
    _meta: ModelMeta
    _fields: Dict[str, Field]

    @classmethod
    def generate_create_table_ddl(cls) -> str:
        cols = ["id SERIAL PRIMARY KEY"]
        for fname, field in cls._fields.items():
            cols.append(field.to_sql_column(fname))
        cols_sql = ",\n  ".join(cols)
        return f"CREATE TABLE {cls._meta.db_table} (\n  {cols_sql}\n);"


# ---------------------------------------------------------------------
# Task 3: Concrete Model Example
# ---------------------------------------------------------------------
class UserAccount(BaseModel):
    _meta = ModelMeta(db_table="auth_users", ordering=["-id"])
    _fields = {
        "username": Field("CharField", max_length=150, unique=True, null=False),
        "bio": Field("TextField", null=False, blank=True),
        "is_active": Field("BooleanField", null=False)
    }


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 39 Practice Tests ---")

    # Test Task 1
    f_char = Field("CharField", max_length=100)
    assert "VARCHAR(100) NOT NULL" in f_char.to_sql_column("title")

    try:
        Field("CharField")  # Missing max_length
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    try:
        Field("CharField", max_length=50, null=True, unique=False)  # null=True on CharField
        assert False, "Should raise ValueError for null=True on CharField"
    except ValueError:
        pass

    # Test Task 2 & 3
    ddl = UserAccount.generate_create_table_ddl()
    assert "CREATE TABLE auth_users" in ddl
    assert "username VARCHAR(150) NOT NULL UNIQUE" in ddl
    assert "is_active BOOLEAN NOT NULL" in ddl

    print("All Day 39 practice assertions passed successfully!")
