"""
Day 54 Daily Challenge: E-Commerce SOLID Checkout Pipeline

Problem:
Refactor an e-commerce checkout flow adhering strictly to SOLID:
1. `PricingEngine` (SRP): Computes taxes and apply discount strategies.
2. `DiscountStrategy` (OCP): Extensible base class for percentage, flat, or VIP discounts.
3. `PaymentProcessor` (DIP/LSP): Abstract payment provider interface.
4. `CheckoutService`: Orchestrates calculation, payment, and receipt generation via dependency injection.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

# --- Discount Strategies (OCP) ---
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, subtotal: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, subtotal: float) -> float:
        return 0.0

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, subtotal: float) -> float:
        return round(subtotal * (self.percent / 100.0), 2)

class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, subtotal: float) -> float:
        return min(subtotal, self.amount)


# --- Payment Gateway Interface (DIP / LSP) ---
class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: float) -> Dict[str, Any]:
        pass

class MockStripeGateway(PaymentGateway):
    def charge(self, amount: float) -> Dict[str, Any]:
        return {"provider": "stripe", "status": "succeeded", "amount": amount}

class MockPayPalGateway(PaymentGateway):
    def charge(self, amount: float) -> Dict[str, Any]:
        return {"provider": "paypal", "status": "succeeded", "amount": amount}


# --- Checkout Service Orchestrator (SRP & DIP) ---
class CheckoutService:
    def __init__(self, payment_gateway: PaymentGateway, tax_rate: float = 0.08):
        self.payment_gateway = payment_gateway
        self.tax_rate = tax_rate

    def process_order(self, subtotal: float, discount_strategy: Optional[DiscountStrategy] = None) -> Dict[str, Any]:
        strategy = discount_strategy or NoDiscount()
        discount_amount = strategy.apply_discount(subtotal)
        discounted_subtotal = max(0.0, subtotal - discount_amount)
        tax = round(discounted_subtotal * self.tax_rate, 2)
        final_total = round(discounted_subtotal + tax, 2)

        # Process payment via injected gateway
        payment_result = self.payment_gateway.charge(final_total)

        return {
            "subtotal": subtotal,
            "discount": discount_amount,
            "tax": tax,
            "final_total": final_total,
            "payment": payment_result
        }


# ---------------------------------------------------------------------
# Test Harness
# ---------------------------------------------------------------------
if __name__ == "__main__":
    gateway = MockStripeGateway()
    checkout = CheckoutService(gateway, tax_rate=0.10)

    # 1. No discount
    res1 = checkout.process_order(100.0)
    assert res1["discount"] == 0.0
    assert res1["tax"] == 10.0
    assert res1["final_total"] == 110.0
    assert res1["payment"]["provider"] == "stripe"

    # 2. Percentage discount (20% off $100 -> $80 + $8 tax = $88)
    res2 = checkout.process_order(100.0, PercentageDiscount(20))
    assert res2["discount"] == 20.0
    assert res2["tax"] == 8.0
    assert res2["final_total"] == 88.0

    # 3. Swap Payment Gateway to PayPal without modifying CheckoutService (OCP / DIP)
    paypal_checkout = CheckoutService(MockPayPalGateway(), tax_rate=0.10)
    res3 = paypal_checkout.process_order(50.0, FlatDiscount(10))
    assert res3["discount"] == 10.0
    assert res3["final_total"] == 44.0
    assert res3["payment"]["provider"] == "paypal"

    print("All SOLID Checkout challenge tests passed successfully!")
