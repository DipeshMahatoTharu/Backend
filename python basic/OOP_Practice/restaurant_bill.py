"""
Practice Project: Restaurant Bill Calculator
============================================
Requirements:
1. Create a `RestaurantBill` class.
2. The constructor should accept:
   - `customer_name` (str)
   - `table_number` (int)
3. Maintain a class-level variable `MENU` representing the food items and their prices.
   Example:
   `MENU = {"Momo": 150, "Chowmein": 120, "Burger": 180, "Pizza": 350, "Coke": 60}`
4. Implement methods for:
   - `add_item(item_name, quantity)`: Adds the specified quantity of an item from the menu to the order. Prints error if item not in menu.
   - `remove_item(item_name, quantity)`: Removes the specified quantity of an item from the order, or deletes it if quantity falls to 0.
   - `calculate_subtotal()`: Returns the sum price of all ordered items.
   - `calculate_total(discount_pct, service_charge_pct, tax_pct)`: 
     - Calculates subtotal.
     - Subtracts discount (e.g., discount_pct = 10 -> 10% discount on subtotal).
     - Adds service charge (e.g., service_charge_pct = 10 -> 10% service charge on discounted total).
     - Adds VAT/tax (e.g., tax_pct = 13 -> 13% VAT on the amount after service charge).
     - Returns final total bill amount.
   - `print_invoice(discount_pct, service_charge_pct, tax_pct)`: Prints a detailed, itemized receipt.

Write your code below and test it by running this file.
"""

class RestaurantBill:
    # Class-level menu card
    MENU = {
        "Momo": 150.0,
        "Chowmein": 120.0,
        "Burger": 180.0,
        "Pizza": 350.0,
        "Coke": 60.0
    }

    def __init__(self, customer_name: str, table_number: int):
        # TODO: Initialize instance variables (e.g., customer, table, and order_items dictionary)
        pass

    def add_item(self, item_name: str, quantity: int) -> bool:
        # TODO: Add item to order
        pass

    def remove_item(self, item_name: str, quantity: int) -> bool:
        # TODO: Remove item or decrease quantity in order
        pass

    def calculate_subtotal(self) -> float:
        # TODO: Sum of ordered items * their price
        return 0.0

    def calculate_total(self, discount_pct: float = 0.0, service_charge_pct: float = 10.0, tax_pct: float = 13.0) -> float:
        # TODO: Apply discount, add service charge, and add tax. Return final amount.
        return 0.0

    def print_invoice(self, discount_pct: float = 0.0, service_charge_pct: float = 10.0, tax_pct: float = 13.0):
        # TODO: Print an itemized invoice statement
        pass


# =====================================================================
# TEST SUITE (Run this file to verify your implementation)
# =====================================================================
if __name__ == "__main__":
    print("Testing Restaurant Bill Calculator Class...")
    
    # Try testing your code here:
    # bill = RestaurantBill("Dipesh", 5)
    # bill.add_item("Momo", 2)
    # bill.add_item("Pizza", 1)
    # bill.add_item("Coke", 3)
    # bill.print_invoice(10, 10, 13) # 10% discount, 10% service charge, 13% tax
    
    print("\nComplete the class implementation to pass the test cases!")
