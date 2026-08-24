"""
Day 20 OOP Coding Practice — School Grade Book
==============================================
Requirements:
1. Create a `Course` class:
   - Attributes: `course_code` (str, e.g. "CS101"), `course_name` (str), `max_capacity` (int).
   - Validation: `max_capacity` must be a positive integer. Protect this using @property.
2. Create a `Student` class:
   - Attributes: `student_id` (str), `name` (str), `_grades` (dict mapping Course objects -> float grade).
   - Use @property to expose a read-only list of enrolled courses.
   - Methods:
     - `enroll_in_course(course)`: Enrolls student in course. 
     - `add_grade(course, score)`: Validates score is between 0 and 100. If valid, records it.
     - `get_gpa()`: Calculates and returns the average grade of all enrolled courses. Returns 0.0 if no grades exist.
3. Create a `School` class:
   - Attributes: `school_name` (str), `students` (list of Student objects), `courses` (list of Course objects).
   - Methods:
     - `register_student(student)`: Adds student.
     - `create_course(course)`: Adds course.
     - `enroll_student_in_course(student_id, course_code)`: Finds the student and course, and handles enrollment. Should raise a custom exception `EnrollmentError` if capacity of course is exceeded.

Write your code below. DO NOT change the test cases in the main block.
"""

# Define custom exception here
class EnrollmentError(Exception):
    pass


class Course:
    def __init__(self, course_code: str, course_name: str, max_capacity: int):
        # TODO: Initialize attributes. Validate max_capacity using setter.
        pass

    @property
    def max_capacity(self) -> int:
        # TODO: Implement getter
        return 0

    @max_capacity.setter
    def max_capacity(self, value: int):
        # TODO: Implement setter validation (capacity > 0)
        pass


class Student:
    def __init__(self, student_id: str, name: str):
        # TODO: Initialize attributes. _grades should start as an empty dictionary.
        pass

    @property
    def enrolled_courses(self) -> list:
        # TODO: Return list of Course objects the student is enrolled in
        return []

    def enroll_in_course(self, course: Course):
        # TODO: Add course to grades dict with initial grade as None
        pass

    def add_grade(self, course: Course, score: float):
        # TODO: Add grade score (must be between 0.0 and 100.0). Raise ValueError if invalid.
        pass

    def get_gpa(self) -> float:
        # TODO: Return average of all graded courses. Ignore courses where grade is None.
        return 0.0


class School:
    def __init__(self, school_name: str):
        # TODO: Initialize school name, empty lists for students and courses
        pass

    def register_student(self, student: Student):
        # TODO: Add student to school list
        pass

    def create_course(self, course: Course):
        # TODO: Add course to school list
        pass

    def enroll_student_in_course(self, student_id: str, course_code: str):
        # TODO: Perform enrollment. Verify course capacity has not been exceeded. 
        # Hint: Count how many students in the school are already enrolled in this course.
        # If capacity reached, raise EnrollmentError.
        pass


# =====================================================================
# TEST BLOCK (Do NOT modify this)
# =====================================================================
if __name__ == "__main__":
    print("Running School Grade Book Tests...")
    
    # 1. Test Course capacity validation
    try:
        invalid_course = Course("CS101", "Python Basics", -5)
        print("FAIL: Negative capacity should have raised ValueError.")
    except ValueError:
        print("PASS: Negative capacity validation caught.")

    # 2. Setup School
    school = School("Apex Academy")
    c1 = Course("CS101", "Python Basics", 2)
    c2 = Course("CS102", "OOP Design", 5)
    school.create_course(c1)
    school.create_course(c2)

    s1 = Student("S001", "Dipesh")
    s2 = Student("S002", "Anjali")
    s3 = Student("S003", "Ramesh")
    school.register_student(s1)
    school.register_student(s2)
    school.register_student(s3)

    # 3. Test enrollment
    school.enroll_student_in_course("S001", "CS101")
    school.enroll_student_in_course("S002", "CS101")
    
    try:
        school.enroll_student_in_course("S003", "CS101")
        print("FAIL: Enrolling student 3 should have raised EnrollmentError (exceeded capacity limit of 2).")
    except EnrollmentError:
        print("PASS: Course capacity validation caught.")

    # 4. Test Grades and GPA
    s1.enroll_in_course(c2)
    s1.add_grade(c1, 90.0)
    s1.add_grade(c2, 80.0)
    
    try:
        s1.add_grade(c1, 150.0)
        print("FAIL: Out of bound grade should have raised ValueError.")
    except ValueError:
        print("PASS: Grade validation caught.")

    print(f"Student GPA: {s1.get_gpa()}") # Should be 85.0
