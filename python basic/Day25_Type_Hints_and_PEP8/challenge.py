"""
============================================================
DAY 25 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: E-Commerce Typed Order & Invoice Engine

Build a type-annotated, dataclass-driven order calculation and
invoice generation engine for an e-commerce backend service.

============================================================
REQUIREMENTS:
============================================================
1. Dataclass `Product`:
   - `id`: int
   - `title`: str
   - `unit_price`: float
   - `sku`: str

2. Dataclass `OrderItem`:
   - `product`: Product
   - `quantity`: int
   - `discount_pct`: float = 0.0  (e.g., 10.0 represents 10% discount)
   - Property `line_total(self) -> float`:
     Computes `quantity * unit_price * (1 - discount_pct / 100)`.
     Validate in `__post_init__` that `quantity > 0` and `0 <= discount_pct <= 100`.

3. Dataclass `Order`:
   - `order_id`: str
   - `customer_email`: str
   - `items`: list[OrderItem] (use field(default_factory=list))
   - `status`: Literal["PENDING", "PAID", "SHIPPED", "CANCELLED"] = "PENDING"
   - `created_at`: datetime = field(default_factory=datetime.utcnow)

   Methods:
   - `add_item(self, item: OrderItem) -> None`
   - `subtotal(self) -> float`: Sum of all item line totals.
   - `tax(self, tax_rate: float = 0.10) -> float`: Tax computed on subtotal.
   - `grand_total(self, tax_rate: float = 0.10) -> float`: Subtotal + tax.
   - `mark_paid(self) -> None`: Changes status to "PAID". Raises ValueError if order is CANCELLED.
   - `generate_invoice(self, tax_rate: float = 0.10) -> dict[str, Any]`:
     Returns a structured dictionary representation suitable for JSON export.
"""

from dataclasses import dataclass, field
from typing import Literal, Any
from datetime import datetime


@dataclass
class Product:
    id: int
    title: str
    unit_price: float
    sku: str


@dataclass
class OrderItem:
    product: Product
    quantity: int
    discount_pct: float = 0.0

    # TODO: Add __post_init__ validation
    # TODO: Add line_total property
    pass


@dataclass
class Order:
    order_id: str
    customer_email: str
    items: list[OrderItem] = field(default_factory=list)
    status: Literal["PENDING", "PAID", "SHIPPED", "CANCELLED"] = "PENDING"
    created_at: datetime = field(default_factory=datetime.utcnow)

    def add_item(self, item: OrderItem) -> None:
        # TODO: Append item to self.items
        pass

    def subtotal(self) -> float:
        # TODO: Calculate subtotal
        pass

    def tax(self, tax_rate: float = 0.10) -> float:
        # TODO: Calculate tax
        pass

    def grand_total(self, tax_rate: float = 0.10) -> float:
        # TODO: Calculate grand total
        pass

    def mark_paid(self) -> None:
        # TODO: Transition status to PAID
        pass

    def generate_invoice(self, tax_rate: float = 0.10) -> dict[str, Any]:
        # TODO: Return formatted dictionary
        pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    print("Testing E-Commerce Typed Order Engine...")
    
    laptop = Product(id=1, title="MacBook Pro", unit_price=1999.0, sku="MBP-16")
    mouse = Product(id=2, title="Wireless Mouse", unit_price=49.0, sku="MOU-WL")
    
    order = Order(order_id="ORD-2026-001", customer_email="customer@example.com")
    order.add_item(OrderItem(product=laptop, quantity=1, discount_pct=5.0))
    order.add_item(OrderItem(product=mouse, quantity=2))
    
    print(f"Order Status: {order.status}")
    print(f"Subtotal: ${order.subtotal():.2f}")
    print(f"Tax: ${order.tax(0.10):.2f}")
    print(f"Grand Total: ${order.grand_total(0.10):.2f}")
    
    order.mark_paid()
    print(f"Updated Status: {order.status}")
    
    invoice = order.generate_invoice(0.10)
    print("Invoice Generated:")
    print(invoice)