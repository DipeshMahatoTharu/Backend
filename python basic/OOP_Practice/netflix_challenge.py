"""
Practice Project: Netflix Account Challenge
============================================
Requirements:
1. Create a `SubscriptionPlan` class:
   - Attributes: `plan_name` (str, e.g., "Basic", "Standard", "Premium"), `price` (float), `resolution` (str, e.g., "720p", "1080p", "4K"), `screen_limit` (int).
2. Create a `UserProfile` class:
   - Attributes: `profile_name` (str), `is_kids` (bool), `watchlist` (list of strings).
   - Methods:
     - `add_to_watchlist(title)`: Appends title to watchlist.
     - `remove_from_watchlist(title)`: Removes title if present.
3. Create a `NetflixAccount` class:
   - Attributes: `email` (str), `__password` (str, private), `active_plan` (SubscriptionPlan object), `profiles` (list of UserProfile objects).
   - Class-level variable: `COMPANY_NAME = "Netflix"`
   - Methods:
     - `change_password(old_pass, new_pass)`: Updates password if old password matches.
     - `add_profile(profile)`: Adds a UserProfile to the account. Maximum limit is 5 profiles. Prints a message if limit exceeded.
     - `change_plan(new_plan)`: Swaps active subscription plan with a new SubscriptionPlan object.
     - `display_account_info()`: Prints account summary, including profile list, watchlist counts, and plan pricing.

Write your code below and test it by running this file.
"""

class SubscriptionPlan:
    def __init__(self, plan_name: str, price: float, resolution: str, screen_limit: int):
        # TODO: Initialize plan specifications
        pass


class UserProfile:
    def __init__(self, profile_name: str, is_kids: bool = False):
        # TODO: Initialize profile attributes (include a watchlist list)
        pass

    def add_to_watchlist(self, title: str):
        # TODO: Add movie/show title to watchlist
        pass

    def remove_from_watchlist(self, title: str) -> bool:
        # TODO: Remove movie/show title from watchlist
        pass


class NetflixAccount:
    COMPANY_NAME = "Netflix"

    def __init__(self, email: str, password: str, active_plan: SubscriptionPlan):
        # TODO: Initialize account attributes (password should be private)
        pass

    def change_password(self, old_pass: str, new_pass: str) -> bool:
        # TODO: Safely change account password
        pass

    def add_profile(self, profile: UserProfile) -> bool:
        # TODO: Add profile up to a maximum limit of 5 profiles
        pass

    def change_plan(self, new_plan: SubscriptionPlan):
        # TODO: Change the active subscription plan
        pass

    def display_account_info(self):
        # TODO: Print account summary
        pass


# =====================================================================
# TEST SUITE (Run this file to verify your implementation)
# =====================================================================
if __name__ == "__main__":
    print("Testing Netflix Account System Class...")
    
    # Try testing your code here:
    # basic_plan = SubscriptionPlan("Basic", 800.0, "720p", 1)
    # acc = NetflixAccount("dipesh@example.com", "secure123", basic_plan)
    # prof1 = UserProfile("Dipesh")
    # acc.add_profile(prof1)
    # ...
    
    print("\nComplete the class implementation to pass the test cases!")
