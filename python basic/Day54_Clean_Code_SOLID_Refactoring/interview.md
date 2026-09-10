# Day 54 — Real-World Backend Engineering Interview

These questions assess your architectural maturity, code refactoring skills, and understanding of SOLID design patterns.

---

### Question 1: How Do You Refactor a 1,000-Line "God Model" in Django?
**Interview Scenario:**
> *"Your team inherited an e-commerce codebase where `models.py` has an `Order` model with 1,200 lines of code. It contains methods like `calculate_taxes()`, `charge_stripe()`, `generate_pdf_receipt()`, `send_sms_notification()`, and `sync_to_salesforce()`. How do you systematically refactor this using SOLID?"*

#### Senior Mentor Answer & Key Points:
1. **The Core Problem (SRP Violation)**:
   - The `Order` model is carrying 5 distinct responsibilities: persistence, pricing calculation, external payment, document rendering, and third-party CRM syncing.
2. **Systematic 4-Step Refactoring Plan**:
   - **Step 1 (Extract Payment Client)**:
     - Move Stripe charge logic into `services/payment_gateway.py`.
   - **Step 2 (Extract Notification & CRM)**:
     - Move SMS and Salesforce syncing into `services/notifications.py` and Celery background tasks.
   - **Step 3 (Extract Document Rendering)**:
     - Move PDF generation into `services/pdf_generator.py`.
   - **Step 4 (Create OrderCheckoutService)**:
     - The `Order` model retains only its database fields, relationships, and basic properties.
     - An `OrderService` coordinates the checkout pipeline.

---

### Question 2: Why Dependency Injection in Python Doesn't Require Heavy Frameworks
**Interview Scenario:**
> *"In Java/C#, developers use Spring or Guice for Dependency Injection. How do experienced Python backend engineers achieve Dependency Injection without adding bloated DI frameworks?"*

#### Senior Mentor Answer & Key Points:
1. **Constructor & Function Injection**:
   - In Python, duck typing and first-class functions make DI effortless:
     ```python
     class InvoiceService:
         def __init__(self, email_client=None):
             self.email_client = email_client or DefaultSMTPEmailClient()
     ```
   - In production: `service = InvoiceService()`.
   - In tests: `service = InvoiceService(email_client=MockEmailClient())`.
2. **Simplicity Over Over-Engineering**:
   - Python's dynamic nature eliminates the need for XML configuration files or complex DI reflection containers.
