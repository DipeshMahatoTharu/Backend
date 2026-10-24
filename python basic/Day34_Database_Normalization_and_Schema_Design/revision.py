"""
============================================================
DAY 34 REVISION SESSION (~10–15 MINUTES)
Topic: Lists, List Conditions, Slicing & Dictionaries
============================================================

Verified Prerequisites: Days 7–9 (Day 7 Lists, Day 8 List Operations, Day 9 Dictionaries)

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
# 1. What is the algorithmic time complexity of checking if a key exists in a Python dict (O(1)) 
# vs an item in an unsorted list (O(n))?

#Python dictionary key lookup — O(1) (average case): Checking whether a key exists is generally constant time,
# regardless of how many keys the dictionary contains.

#Unsorted list item lookup — O(n): Python may need to check each item one by one until it finds the target. Here, 
# n is the number of items.

# 2. How does Python list slice step syntax `items[::-1]` reverse a sequence?
#items[::-1] reverses a sequence by using slicing with a step of -1, so it reads the items from the end to the beginning.

# 3. Why is `dict.get(key, default)` preferred over direct bracket indexing `dict[key]` when keys may be absent?
# .get() returns a default value if the key is missing, while dict[key] raises a KeyError.

# ============================================================
# PART 2: 10-MINUTE CODING CHALLENGE
# ============================================================
# Scenario:
# Write `count_word_frequencies(words: list[str]) -> dict[str, int]`
# that normalizes all words to lowercase and counts the occurrence of each word in a dictionary.

def count_word_frequencies(words: list[str]) -> dict[str, int]:
    """
    Counts frequency of each word normalized to lowercase.
    Example: ['Python', 'Django', 'python'] -> {'python': 2, 'django': 1}
    """
    # WRITE YOUR CODE HERE:
    tolowerdict={}
    for word in words:
        lowerword=word.lower()
        if lowerword in tolowerdict:
            tolowerdict[lowerword]+=1
        else:
            tolowerdict[lowerword]=1
    return tolowerdict
            
    

# ============================================================
# VERIFICATION RUNNER (Executes your code without revealing solutions)
# ============================================================
def run_test():
    print("--- Running Day 34 Revision Challenge ---")
    words = ["Python", "Django", "python", "API", "api", "Python"]
    res = count_word_frequencies(words)
    if res is None:
        print("[!] Function `count_word_frequencies` is not yet implemented.")
        return
    if res.get("python") == 3 and res.get("django") == 1 and res.get("api") == 2:
        print("[+] Test Passed: Word frequency dictionary correctly aggregated.")
    else:
        print(f"[-] Test Failed: Got {res}")

if __name__ == "__main__":
    run_test()


# ============================================================
# [*] HINTS SECTION (Read only if stuck after ~10 minutes)
# ============================================================
# Hint 1: Iterate through words, calling `.lower()` on each word.
# Hint 2: Use `counts[w] = counts.get(w, 0) + 1` to accumulate counts in a loop.


# ============================================================
# [!] SOLUTION SECTION (Do not look until your 15-minute attempt is done!)
# ============================================================
def _reference_solution(words: list[str]) -> dict[str, int]:
    counts = {}
    for w in words:
        lw = w.lower()
        counts[lw] = counts.get(lw, 0) + 1
    return counts


# ============================================================
# [?] SELF-ASSESSMENT CHECKLIST
# After completing, mark your result in `revision_tracker.md`:
# [ ] INDEPENDENT: Solved within 15 minutes with no hints.
# [ ] HINT NEEDED: Solved after reading Hint 1 or Hint 2.
# [ ] REFRESHER NEEDED: Needed mentor explanation or reference solution.
# [ ] NOT ATTEMPTED: Not attempted yet.
# ============================================================
