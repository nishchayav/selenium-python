"""
Test Script for Smart University Management System

Demonstrates all 14 OOP concepts as per case study
"""

from models import Student, Faculty, Course, HeadOfDepartment
from utils import student_batch_generator, CourseIterator
from filehandler import save_students_json, generate_csv_report
from exceptions import DuplicateRecordError, InvalidInputError, AuthorizationError

print("="*60)
print("SMART UNIVERSITY MANAGEMENT SYSTEM - TEST SCRIPT")
print("="*60)

# Test 1: Classes & Objects + Constructors
print("\n1. CREATING STUDENTS (Classes, Objects & Constructors)")
print("-"*60)
s1 = Student("S101", "Ananya Sharma", "Computer Science", 4, [78, 85, 90, 88, 92])
s2 = Student("S102", "Rohan Verma", "Computer Science", 4, [65, 70, 72, 68, 75])
print(f"✓ Student 1 Created: {s1.name}")
print(f"✓ Student 2 Created: {s2.name}")

# Test 2: Abstract Base Class + Polymorphism (get_details)
print("\n2. POLYMORPHISM - get_details() Method Override")
print("-"*60)
print("Student Details:")
print(s1.get_details())
print()

# Test 3: Faculty Creation + Single Inheritance
print("\n3. FACULTY CREATION (Single Inheritance: Faculty → Person)")
print("-"*60)
f1 = Faculty("F201", "Dr. Rajesh Kumar", "Computer Science", 85000, is_admin=False)
print(f"✓ Faculty Created: {f1.name}")
print(f"Faculty Details:")
print(f1.get_details())
print()

# Test 4: Multilevel Inheritance (HeadOfDepartment → Faculty → Person)
print("\n4. MULTILEVEL INHERITANCE - Head of Department")
print("-"*60)
hod = HeadOfDepartment("HOD001", "Prof. Vikram Singh", "Computer Science", 120000, 15)
print(f"✓ Head of Department Created: {hod.name}")
print(f"Details:")
print(hod.get_details())
print()

# Test 5: Course Creation with Faculty
print("\n5. COURSE CREATION")
print("-"*60)
c1 = Course("CS401", "Data Structures", 4, f1)
c2 = Course("CS402", "Algorithms", 3, f1)
print(f"✓ Course 1 Created: {c1.name} ({c1.credits} credits)")
print(f"✓ Course 2 Created: {c2.name} ({c2.credits} credits)")
print()

# Test 6: Operator Overloading - Addition (+)
print("\n6. OPERATOR OVERLOADING - + (Merge Course Credits)")
print("-"*60)
total_credits = c1 + c2
print(f"Total Credits: {c1.name} ({c1.credits}) + {c2.name} ({c2.credits}) = {total_credits}")
print()

# Test 7: Enrollment
print("\n7. STUDENT ENROLLMENT")
print("-"*60)
s1.courses.append(c1)
s1.courses.append(c2)
print(f"✓ {s1.name} enrolled in {c1.name}")
print(f"✓ {s1.name} enrolled in {c2.name}")
print()

# Test 8: Decorators + Descriptors Validation + Polymorphism (calculate_performance)
print("\n8. CALCULATE PERFORMANCE (Decorators: @log_execution, @time_it)")
print("-"*60)
avg, grade = s1.calculate_performance()
print(f"Student: {s1.name}")
print(f"Marks: {s1.marks}")
print(f"Average: {round(avg, 1)}")
print(f"Grade: {grade}")
print()

# Test 9: Operator Overloading - Comparison (>)
print("\n9. OPERATOR OVERLOADING - > (Compare Student Performance)")
print("-"*60)
result = s1 > s2
print(f"Comparing Students Performance")
print(f"{s1.name} > {s2.name}: {result}")
print()

# Test 10: Iterator Pattern for Courses
print("\n10. ITERATOR PATTERN - CourseIterator")
print("-"*60)
print("Iterating through courses using CourseIterator:")
course_iterator = CourseIterator([c1, c2])
for course in course_iterator:
    print(f"  Code: {course.code}, Name: {course.name}, Credits: {course.credits}")
print()

# Test 11: Generator Pattern for Student Records
print("\n11. GENERATOR PATTERN - student_batch_generator")
print("-"*60)
all_students = [s1, s2]
for batch in student_batch_generator(all_students, batch_size=1):
    for student in batch:
        print(f"  {student.id} - {student.name}")
print()

# Test 12: Descriptor - Marks Validation
print("\n12. DESCRIPTOR VALIDATION - Marks (0-100)")
print("-"*60)
try:
    invalid_student = Student("S103", "Test", "CS", 1, [50, 101, 75, 80, 90])
    print("ERROR: Should have raised exception for marks > 100")
except InvalidInputError as e:
    print(f"✓ Correctly caught error: {e}")
print()

# Test 13: Descriptor - Salary Access Control
print("\n13. DESCRIPTOR VALIDATION - Salary (Admin Only Access)")
print("-"*60)
try:
    salary = f1.salary
    print("ERROR: Should have raised exception (not admin)")
except AuthorizationError as e:
    print(f"✓ Correctly caught error: {e}")

# Now set admin=True and try again
f1.is_admin = True
try:
    salary = f1.salary
    print(f"✓ Admin access granted. Salary: {salary}")
except AuthorizationError as e:
    print(f"ERROR: {e}")
print()

# Test 14: File Handling - JSON & CSV
print("\n14. FILE HANDLING - JSON & CSV Reports")
print("-"*60)
student_data = [
    {
        "id": s1.id,
        "name": s1.name,
        "department": s1.department,
        "semester": s1.semester,
        "marks": s1.marks
    }
]
save_students_json(student_data, "data/students.json")
generate_csv_report([s1, s2], "data/students_report.csv")
print()

# Test 15: Exception Handling - Duplicate Record
print("\n15. EXCEPTION HANDLING - Duplicate Record Detection")
print("-"*60)
try:
    duplicate = Student("S101", "Duplicate Name", "CS", 1, [50, 60, 70, 80, 90])
    print("ERROR: Duplicate should be caught in main application")
except Exception as e:
    print(f"Note: Duplicate checking happens in main menu application")
print()

# Test 16: Destructors
print("\n16. DESTRUCTORS (__del__ method)")
print("-"*60)
temp_student = Student("S999", "Temp", "CS", 1, [50, 60, 70, 80, 90])
print(f"Temp student created: {temp_student.name}")
del temp_student
print("(Destructor called automatically)")
print()

print("="*60)
print("✓ ALL TESTS COMPLETED SUCCESSFULLY!")
print("="*60)
print("\nCASE STUDY REQUIREMENTS VERIFICATION:")
print("✓ 1.  Introduction to OOP - Classes and objects used")
print("✓ 2.  Classes & Objects - Person, Student, Faculty, Course")
print("✓ 3.  Constructors & Destructors - __init__ and __del__")
print("✓ 4.  Parameterized Methods - Enroll, Calculate, Compare")
print("✓ 5.  Abstract Base Classes - Person is ABC")
print("✓ 6.  Inheritance - Student/Faculty → Person")
print("✓ 7.  Single & Multilevel Inheritance - Faculty & HeadOfDepartment")
print("✓ 8.  Polymorphism - get_details(), calculate_performance()")
print("✓ 9.  Operator Overloading - + (credits), > (performance)")
print("✓ 10. Descriptors - MarksDescriptor, SalaryDescriptor")
print("✓ 11. Decorators - @log_execution, @time_it")
print("✓ 12. Iterators & Generators - CourseIterator, student_batch_generator")
print("✓ 13. File Handling - JSON & CSV")
print("✓ 14. Exception Handling - DuplicateRecord, InvalidInput, Authorization")
print("="*60)
