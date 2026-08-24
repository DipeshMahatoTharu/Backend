"""
Practice Project: ATM Machine
==============================
Requirements:
1. Create an `ATM` class.
2. The constructor should accept:
   - `account_holder` (string)
   - `initial_pin` (string, e.g., "1234")
   - `initial_balance` (float/int, default to 0.0)
3. Protect the balance and PIN from direct external access using private variables (e.g., `__balance`, `__pin`).
4. Implement methods for:
   - `verify_pin(input_pin)`: Returns True if the pin matches, False otherwise.
   - `check_balance(input_pin)`: Prints and returns the balance if PIN is correct, else prints "Invalid PIN" and returns None.
   - `deposit(amount)`: Adds money to the balance if amount is positive.
   - `withdraw(amount, input_pin)`: Subtracts money from the balance if PIN is correct and there are sufficient funds.
   - `change_pin(old_pin, new_pin)`: Changes the PIN if the old PIN is verified and the new PIN is valid (exactly 4 digits).

Write your code below and test it by running this file.
"""

class ATM:
    def __init__(self, account_holder: str, initial_pin: str, initial_balance: float = 0.0):
        # TODO: Initialize instance variables. Use private variables for pin and balance.
        pass

    def verify_pin(self, input_pin: str) -> bool:
        # TODO: Implement PIN verification
        pass

    def check_balance(self, input_pin: str):
        # TODO: Implement balance checking (requires PIN verification)
        pass

    def deposit(self, amount: float) -> bool:
        # TODO: Implement deposit functionality
        pass

    def withdraw(self, amount: float, input_pin: str) -> bool:
        # TODO: Implement withdrawal functionality
        pass

    def change_pin(self, old_pin: str, new_pin: str) -> bool:
        # TODO: Implement PIN change functionality
        pass


# =====================================================================
# TEST SUITE (Run this file to verify your implementation)
# =====================================================================
if __name__ == "__main__":
    print("Testing ATM Machine Class...")
    
    # Try testing your code here:
    # my_atm = ATM("Dipesh", "1234", 1000.0)
    # print("PIN Verified:", my_atm.verify_pin("1234"))
    # ...
    
    print("\nComplete the class implementation to pass the test cases!")
