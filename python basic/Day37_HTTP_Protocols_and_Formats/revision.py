"""
============================================================
DAY 37 REVISION SESSION (~10–15 MINUTES)
Topic: Encapsulation, Polymorphism & Abstract Base Classes
============================================================

Verified Prerequisites: Days 16–18 (Day 16 Encapsulation, Day 17 Polymorphism, Day 18 Abstraction & ABC)

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
# 1. What is the convention for protected attributes (`_name`) vs private attributes (`__name` with name mangling)?
#
# 2. What is polymorphism in Python (treating different objects via the same interface)?
#
# 3. Why cannot an Abstract Base Class (inheriting `abc.ABC` with `@abstractmethod`) be instantiated directly?


# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Implement abstract class `Notification(ABC)` with `@abstractmethod def send(recipient: str, msg: str) -> str`. Implement concrete subclasses `EmailNotification` returning `'Email to {recipient}: {msg}'` and `SMSNotification` returning `'SMS to {recipient}: {msg}'`.

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, msg: str) -> str:
        pass

class EmailNotification(Notification):
    # WRITE CODE HERE:
    pass

class SMSNotification(Notification):
    # WRITE CODE HERE:
    pass


# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 37 Revision Challenge ---")
    try:
        e = EmailNotification()
        s = SMSNotification()
        r1 = e.send("alice@mail.com", "Hello")
        r2 = s.send("9841000000", "OTP 1234")
        if r1 is None or r2 is None:
            print("[!] Methods are not yet implemented.")
            return
        if r1 == "Email to alice@mail.com: Hello" and r2 == "SMS to 9841000000: OTP 1234":
            print("[+] Test Passed: Polymorphic Notification subclasses confirmed.")
        else:
            print(f"[-] Test Failed: r1='{r1}', r2='{r2}'")
    except Exception as e:
        print(f"[!] Test error: {e}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Each subclass overrides `send(self, recipient: str, msg: str) -> str`.
# Hint 2: EmailNotification returns `f'Email to {recipient}: {msg}'`; SMSNotification returns `f'SMS to {recipient}: {msg}'`.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
from abc import ABC, abstractmethod

class _RefNotification(ABC):
    @abstractmethod
    def send(self, recipient: str, msg: str) -> str:
        pass

class _RefEmail(_RefNotification):
    def send(self, recipient: str, msg: str) -> str:
        return f"Email to {recipient}: {msg}"

class _RefSMS(_RefNotification):
    def send(self, recipient: str, msg: str) -> str:
        return f"SMS to {recipient}: {msg}"


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
