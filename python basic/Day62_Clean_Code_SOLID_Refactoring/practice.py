"""
Day 54: Clean Code & SOLID Refactoring — Practice
Hands-on exercises covering Single Responsibility refactoring, Strategy pattern, and Dependency Injection.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List

# ---------------------------------------------------------------------
# Task 1: Single Responsibility Refactoring (SRP)
# ---------------------------------------------------------------------
# Bad: One class does taxation, discount calculation, and invoice printing.
# Clean: Decouple calculation from formatting.
class OrderCalculator:
    def calculate_total(self, subtotal: float, tax_rate: float, discount: float) -> float:
        tax = subtotal * tax_rate
        return max(0.0, subtotal + tax - discount)

class InvoiceFormatter:
    def format_text_receipt(self, order_id: int, total: float) -> str:
        return f"Order #{order_id} | Total Due: ${total:.2f}"


# ---------------------------------------------------------------------
# Task 2: Strategy Pattern (Open/Closed Principle - OCP)
# ---------------------------------------------------------------------
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

class EmailNotification(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        return f"Email to {recipient}: {message}" != ""

class SMSNotification(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        return f"SMS to {recipient}: {message}" != ""


# ---------------------------------------------------------------------
# Task 3: Dependency Inversion (DIP)
# ---------------------------------------------------------------------
class OrderNotifier:
    def __init__(self, channel: NotificationChannel):
        # High-level module depends on abstraction (NotificationChannel), not concrete Email/SMS!
        self.channel = channel

    def notify_customer(self, recipient: str, order_id: int) -> bool:
        return self.channel.send(recipient, f"Your order #{order_id} has been confirmed.")


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Running Day 54 Practice Tests ---")

    # Test Task 1: SRP
    calc = OrderCalculator()
    tot = calc.calculate_total(100.0, 0.1, 15.0)
    assert tot == 95.0

    formatter = InvoiceFormatter()
    receipt = formatter.format_text_receipt(42, tot)
    assert receipt == "Order #42 | Total Due: $95.00"

    # Test Task 2 & 3: OCP & DIP
    email_channel = EmailNotification()
    notifier = OrderNotifier(email_channel)
    assert notifier.notify_customer("user@example.com", 42) is True

    sms_channel = SMSNotification()
    sms_notifier = OrderNotifier(sms_channel)
    assert sms_notifier.notify_customer("+15551234567", 42) is True

    print("All Day 54 practice assertions passed successfully!")
