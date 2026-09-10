"""
Day 54: Clean Code & SOLID Refactoring — Debugging
Diagnose and fix 3 common SOLID violations.
"""
from typing import Dict, Any

# ---------------------------------------------------------------------
# Bug 1: Violating OCP with Fragile `if/elif` Chains
# Problem: Every new payment method required modifying `process_payment()`
# with another `elif provider == '...'` block.
# Fix: Use a provider dictionary or strategy registry.
# ---------------------------------------------------------------------
class PaymentRegistry:
    def __init__(self):
        self._providers = {}

    def register(self, name: str, handler):
        self._providers[name.lower()] = handler

    def execute(self, name: str, amount: float) -> str:
        handler = self._providers.get(name.lower())
        if not handler:
            raise ValueError(f"Unsupported payment provider: {name}")
        return handler(amount)


# ---------------------------------------------------------------------
# Bug 2: Violating LSP (Liskov Substitution Principle)
# Problem: Subclass `ReadonlyUser` inherited from `User` but raised
# `NotImplementedError` on `.save()`, breaking calling code that expects
# all `User` instances to be savable!
# Fix: Separate interfaces into `ReadOnlyEntity` and `PersistableEntity`.
# ---------------------------------------------------------------------
class PersistableEntity:
    def save(self) -> bool:
        return True

class ReadOnlyEntity:
    # Does not expose .save() contract!
    pass


# ---------------------------------------------------------------------
# Bug 3: Violating DIP (Direct Dependency on External Concrete Client)
# Problem: A class created `self.client = ConcreteStripeClient()` directly in
# `__init__`, preventing unit tests from substituting a mock client.
# Fix: Inject client via constructor.
# ---------------------------------------------------------------------
class BillingManager:
    # BUGGY VERSION:
    # def __init__(self): self.client = ConcreteStripeClient()

    # FIXED VERSION:
    def __init__(self, client=None):
        self.client = client or "DefaultClient"


# ---------------------------------------------------------------------
# Verification Suite
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Test Bug 1 fix
    reg = PaymentRegistry()
    reg.register("stripe", lambda amt: f"Stripe charged {amt}")
    assert "Stripe charged 50" in reg.execute("stripe", 50)

    # Test Bug 2 fix
    entity = PersistableEntity()
    assert entity.save() is True

    # Test Bug 3 fix
    mgr = BillingManager(client="MockClient")
    assert mgr.client == "MockClient"

    print("All Day 54 debugging fixes verified successfully!")
