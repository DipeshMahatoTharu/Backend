"""
Practice Project: Inventory Management System
============================================
Requirements:
1. Create a `Product` class:
   - Attributes: `product_id` (str), `name` (str), `_price` (float, protected), `stock` (int).
   - Use a getter and setter property for `price` to prevent prices from becoming negative. If set to a negative value, print a warning and set it to 0.0.
2. Create an `Inventory` class:
   - Attributes: `products` (dictionary of product_id -> Product object).
   - Methods:
     - `add_product(product)`: Adds a new Product to the inventory. If the product already exists, print a message and do not overwrite.
     - `update_stock(product_id, quantity)`: Updates stock count. Positive quantity adds stock (restock); negative quantity reduces stock (sale). Ensure stock does not go below 0.
     - `get_product(product_id)`: Returns the Product object or None if not found.
     - `list_low_stock(threshold)`: Returns a list of Product objects whose stock is less than or equal to the threshold (default threshold is 5).
     - `calculate_inventory_value()`: Returns the total sum value of all products in stock (price * stock for all items).

Write your code below and test it by running this file.
"""

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int = 0):
        # TODO: Initialize attributes. Make price protected using self._price.
        pass

    @property
    def price(self) -> float:
        # TODO: Implement getter
        return 0.0

    @price.setter
    def price(self, value: float):
        # TODO: Implement setter (must validate that price >= 0)
        pass


class Inventory:
    def __init__(self):
        # TODO: Initialize product tracker dictionary
        pass

    def add_product(self, product: Product) -> bool:
        # TODO: Add product to inventory
        pass

    def update_stock(self, product_id: str, quantity: int) -> bool:
        # TODO: Adjust stock level. Restock (positive) or Sell (negative). Prevent negative stock levels.
        pass

    def get_product(self, product_id: str) -> Product:
        # TODO: Retrieve product by ID
        pass

    def list_low_stock(self, threshold: int = 5) -> list:
        # TODO: Return a list of products under the stock threshold
        return []

    def calculate_inventory_value(self) -> float:
        # TODO: Calculate total asset value (sum of stock * price for each product)
        return 0.0


# =====================================================================
# TEST SUITE (Run this file to verify your implementation)
# =====================================================================
if __name__ == "__main__":
    print("Testing Inventory Management System Class...")
    
    # Try testing your code here:
    # inv = Inventory()
    # p1 = Product("P101", "Laptop", 85000.0, 10)
    # inv.add_product(p1)
    # ...
    
    print("\nComplete the class implementation to pass the test cases!")
