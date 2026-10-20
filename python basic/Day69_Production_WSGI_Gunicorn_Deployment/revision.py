"""
============================================================
DAY 69 REVISION SESSION (~10–15 MINUTES)
Topic: Webhooks, Payment Gateways & Cryptographic Verification
============================================================

Verified Prerequisites: Day 68 (Webhooks & Payment Gateways)

------------------------------------------------------------
[!] THE 15-MINUTE ATTEMPT RULE
------------------------------------------------------------
1. Start your 15-minute timer before looking at any hints or external resources.
2. Read the recall questions and coding challenge below.
3. Attempt to solve the challenge using your own reasoning and verified notes.
4. If stuck after ~10 minutes, scroll to the HINTS section.
5. If still stuck after ~15 minutes, pause and ask ChatGPT / AI mentor for a targeted clue.
6. After receiving help, type out and solve the problem independently.
7. Record your honest outcome in `revision_tracker.md`!
"""

# ============================================================
# PART 1: RAPID RECALL (2–3 MINUTES)
# Answer these questions in your head or in comments:
# ============================================================
# 1. How does an asynchronous webhook notification work from payment providers (Stripe, PayPal)?
#
# 2. Why must webhook handlers verify the HMAC signature header before processing the request body?
#
# 3. What is an idempotency key and how does it prevent duplicate charges?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `verify_webhook_signature(payload_bytes: bytes, secret: str, signature_header: str) -> bool` using standard library `hmac` and `hashlib.sha256`.

import hmac
import hashlib

def verify_webhook_signature(payload_bytes: bytes, secret: str, signature_header: str) -> bool:
    """
    Verifies HMAC-SHA256 signature using hmac.compare_digest.
    """
    # WRITE YOUR CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    import hmac, hashlib
    print("--- Running Day 69 Revision Challenge ---")
    secret = "my_webhook_secret_key"
    payload = b'{"event": "payment_succeeded", "amount": 100}'
    expected_sig = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    v1 = verify_webhook_signature(payload, secret, expected_sig)
    v2 = verify_webhook_signature(payload, secret, "tampered_signature")
    if v1 is None:
        print("[!] Function `verify_webhook_signature` is not yet implemented.")
        return
    if v1 is True and v2 is False:
        print("[+] Test Passed: HMAC webhook signature verification succeeded.")
    else:
        print(f"[-] Test Failed: v1={v1}, v2={v2}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Compute the hex digest using `hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()`.
# Hint 2: Use `hmac.compare_digest(computed_sig, signature_header)` to prevent timing attacks.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
import hmac
import hashlib

def _reference_solution(payload_bytes: bytes, secret: str, signature_header: str) -> bool:
    computed = hmac.new(secret.encode(), payload_bytes, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature_header)


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
