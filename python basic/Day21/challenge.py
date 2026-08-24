"""
============================================================
DAY 21 PROJECT — STUDENT RECORD MANAGER
============================================================

Your goal is to build a Student Record Manager. This exercise will 
demonstrate the real-world performance difference between managing data 
in lists versus dictionaries.

------------------------------------------------------------
STEP 1: LIST-BASED STUDENT MANAGER
------------------------------------------------------------
Implement the manager class using a list to store students. 
Each student is represented as a dictionary: `{"id": "S001", "name": "Name", "marks": 85}`.

Requirements:
- `add_student(student_id, name, marks)`: Adds the record. If ID already exists, do not add.
- `find_student(student_id)`: Searches the list. Returns the student dictionary or None.
- `update_marks(student_id, new_marks)`: Searches, updates, returns True. Returns False if not found.
- `delete_student(student_id)`: Removes the student from the list.
- `get_average_marks()`: Calculates the average marks of all students.
- `get_top_student()`: Returns the student record with the highest marks.

------------------------------------------------------------
STEP 2: DICTIONARY-BASED STUDENT MANAGER
------------------------------------------------------------
Refactor your entire code to use a dictionary where the keys are student IDs:
`self.students = {"S001": {"name": "Name", "marks": 85}}`

Ensure all methods (add, find, update, delete, average, top) work identical 
to the list version.

------------------------------------------------------------
STEP 3: ANALYZE THE DIFFERENCE
------------------------------------------------------------
Write a brief comparison of both versions. Which operations are faster in 
the dictionary version? Why?

============================================================
MY DATA ANALYSIS:
============================================================
Write your comparisons here:

____________________________________________________
____________________________________________________


============================================================
MY CODE:
============================================================
Implement the List-based version first, then the Refactored Dictionary version:

____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
____________________________________________________
"""