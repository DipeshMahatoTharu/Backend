# Day 23 Exceptions & Defensive Programming Debugging

# =====================================================================
# BUGGY SCENARIO 1: The Bare Except Trap (Swallowing System Errors)
# =====================================================================
# Goal: Write a function that converts input to integer. If an error occurs,
# it should return None.
# Explain why writing `except:` (a bare except) is a major bug (e.g. it blocks
# the user from stopping the program with Ctrl+C), and rewrite it to catch
# only ValueError.

def convert_to_int(value):
    try:
        return int(value)
    except: # Swallows SystemExit, KeyboardInterrupt, etc.
        return None

# ---------------------------------------------------------------------
# QUESTION: Why is a bare except clause dangerous in backend scripts?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the function to catch only the specific ValueError.
# ---------------------------------------------------------------------


# =====================================================================
# BUGGY SCENARIO 2: Missing resource cleanup (finally block)
# =====================================================================
# Goal: Open a connection, read data, and ensure it is ALWAYS closed.
# The code below crashes and fails to close the connection if read() throws.
# Fix it using a try-finally structure.

class MockDBConnection:
    def open(self): print("Connection Opened.")
    def read(self): raise ConnectionError("Database timed out!")
    def close(self): print("Connection Closed.") # This must ALWAYS run.

def fetch_data_pipeline():
    conn = MockDBConnection()
    conn.open()
    # If this line crashes, conn.close() is never called!
    conn.read()
    conn.close()

# ---------------------------------------------------------------------
# QUESTION: How do you guarantee conn.close() runs even on fatal crashes?
#
# MY ANSWER:
# _____________________________________________________________________
#
# CORRECTED CODE:
# TODO: Rewrite the fetch_data_pipeline function to implement cleanups.
# ---------------------------------------------------------------------