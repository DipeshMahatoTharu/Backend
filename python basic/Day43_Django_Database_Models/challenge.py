"""
Day 39 Daily Challenge: Mini-ORM Schema & Migration Generator

Problem:
Implement a migration manager that:
1. Detects schema changes between two model state definitions.
2. Identifies:
   - Added tables (`CreateTableOperation`).
   - Added columns (`AddColumnOperation`).
   - Removed columns (`DropColumnOperation`).
3. Generates the forward SQL statements for the migration.
4. Generates backward rollback SQL statements.
"""
from typing import Dict, List, Any, Tuple

class MigrationOperation:
    def forward_sql(self) -> str:
        raise NotImplementedError
    def backward_sql(self) -> str:
        raise NotImplementedError

class CreateTableOperation(MigrationOperation):
    def __init__(self, table_name: str, columns: Dict[str, str]):
        self.table_name = table_name
        self.columns = columns  # {col_name: col_type}

    def forward_sql(self) -> str:
        cols = ["id SERIAL PRIMARY KEY"] + [f"{k} {v}" for k, v in self.columns.items()]
        return f"CREATE TABLE {self.table_name} ({', '.join(cols)});"

    def backward_sql(self) -> str:
        return f"DROP TABLE {self.table_name};"

class AddColumnOperation(MigrationOperation):
    def __init__(self, table_name: str, col_name: str, col_type: str):
        self.table_name = table_name
        self.col_name = col_name
        self.col_type = col_type

    def forward_sql(self) -> str:
        return f"ALTER TABLE {self.table_name} ADD COLUMN {self.col_name} {self.col_type};"

    def backward_sql(self) -> str:
        return f"ALTER TABLE {self.table_name} DROP COLUMN {self.col_name};"

class SchemaDiffEngine:
    @staticmethod
    def diff(old_schema: Dict[str, Dict[str, str]], new_schema: Dict[str, Dict[str, str]]) -> List[MigrationOperation]:
        operations: List[MigrationOperation] = []

        # Check for new tables
        for tbl, cols in new_schema.items():
            if tbl not in old_schema:
                operations.append(CreateTableOperation(tbl, cols))
            else:
                # Check for added columns
                for cname, ctype in cols.items():
                    if cname not in old_schema[tbl]:
                        operations.append(AddColumnOperation(tbl, cname, ctype))

        return operations


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    old_state = {
        "products": {
            "title": "VARCHAR(200) NOT NULL",
            "price": "DECIMAL(10,2) NOT NULL"
        }
    }

    new_state = {
        "products": {
            "title": "VARCHAR(200) NOT NULL",
            "price": "DECIMAL(10,2) NOT NULL",
            "stock": "INTEGER NOT NULL DEFAULT 0"  # Added column
        },
        "orders": {                                # Added table
            "user_id": "INTEGER NOT NULL",
            "total": "DECIMAL(10,2) NOT NULL"
        }
    }

    ops = SchemaDiffEngine.diff(old_state, new_state)
    assert len(ops) == 2

    # Check AddColumnOperation
    add_col = [op for op in ops if isinstance(op, AddColumnOperation)][0]
    assert add_col.forward_sql() == "ALTER TABLE products ADD COLUMN stock INTEGER NOT NULL DEFAULT 0;"
    assert add_col.backward_sql() == "ALTER TABLE products DROP COLUMN stock;"

    # Check CreateTableOperation
    create_tbl = [op for op in ops if isinstance(op, CreateTableOperation)][0]
    assert "CREATE TABLE orders" in create_tbl.forward_sql()
    assert create_tbl.backward_sql() == "DROP TABLE orders;"

    print("All SchemaDiffEngine migration challenge tests passed successfully!")
