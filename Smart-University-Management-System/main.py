from models import Student, Faculty, Course, HeadOfDepartment
from utils import student_batch_generator, CourseIterator
from filehandler import save_students_json, generate_csv_report
from exceptions import DuplicateRecordError, InvalidInputError

students = []
faculties = []
courses = []

while True:
    print("""
1 - Add Student
2 - Add Faculty
3 - Add Course
4 - Enroll Student to Course
5 - Calculate Student Performance
6 - Compare Two Students
7 - Student Details 
8 - Display Faculty Details
9 - Generate Reports
10 - Exit
""")

    choice = input("Enter your choice: ").strip()

    # 1. Add Student
    if choice == "1":
        sid = input("Enter Student ID:")
        if any(s.id == sid for s in students):
            raise DuplicateRecordError("Error: Student ID already exists")

        name = input("Enter Student Name:" )
        dept = input("Enter the dept :")
        sem = int(input("Enter Semester:"))
        marks = list(map(int, input("Enter marks separated by space: ").split()))

        student = Student(sid, name, dept, sem, marks)
        students.append(student)

        print("Student Created Successfully")
        print("--------------------------------")
        print(f"ID : {sid}")
        print(f"Name : {name}")
        print(f"Department: {dept}")
        print(f"Semester : {sem}")

    # 2. Add Faculty
    elif choice == "2":
        fid = input("Enter Faculty ID: ")
        name = input("Enter Faculty Name: ")
        dept = input("Enter the dept: ")
        salary = int(input("Enter Salary: "))

        faculty = Faculty(fid, name, dept, salary)
        faculties.append(faculty)

        print("Faculty Created Successfully")
        print("--------------------------------")
        print(f"ID : {fid}")
        print(f"Name : {name}")
        print(f"Department: {dept}")

    # 3. Add Course
    elif choice == "3":
        code = input("Enter Course Code: ")
        cname = input("Enter Course Name: ")
        credits = int(input("Enter Course Credits: "))
        fid = input("Enter Faculty ID: ")

        faculty = next((f for f in faculties if f.id == fid), None)
        if not faculty:
            raise InvalidInputError("Error: Faculty not found")

        course = Course(code, cname, credits, faculty)
        courses.append(course)

        print("Course Added Successfully")
        print("--------------------------------")
        print(f"Course Code : {code}")
        print(f"Course Name : {cname}")
        print(f"Credits : {credits}")
        print(f"Faculty : {faculty.name}")

    # 4. Enroll Student to Course
    elif choice == "4":
        sid = input("Enter Student ID: ")
        code = input("Enter Course code: ")

        student = next((s for s in students if s.id == sid), None)
        course = next((c for c in courses if c.code == code), None)

        if not student or not course:
            raise InvalidInputError("Error: Invalid Student or Course")

        student.courses.append(course)

        print("Enrollment Successful")
        print("--------------------------------")
        print(f"Student Name : {student.name}")
        print(f"Course : {course.name}")

    # 5. Calculate Student Performance
    elif choice == "5":
        sid = input("Enter Student ID: ")
        student = next((s for s in students if s.id == sid), None)

        if not student:
            raise InvalidInputError("Error: Student not found")

        avg, grade = student.calculate_performance()

        print("Student Performance Report")
        print("--------------------------------")
        print(f"Student Name : {student.name}")
        print(f"Marks : {student.marks}")
        print(f"Average : {round(avg, 1)}")
        print(f"Grade : {grade}")

    # 6. Compare Two Students (Operator Overloading >)
    elif choice == "6":
        sid1 = input("Enter Student ID(for first student): ")
        sid2 = input("Enter Student ID(for second student): ")

        s1 = next((s for s in students if s.id == sid1), None)
        s2 = next((s for s in students if s.id == sid2), None)

        if not s1 or not s2:
            raise InvalidInputError("Error: Student not found")

        print("Comparing Students Performance")
        print("--------------------------------")
        print(f"{s1.name} > {s2.name} : {s1 > s2}")

    # 7. Display Student Details (Polymorphism)
    elif choice == "7":
        sid = input("Enter Student ID: ")
        student = next((s for s in students if s.id == sid), None)
        
        if not student:
            raise InvalidInputError("Error: Student not found")
        
        print("Student Details:")
        print("--------------------------------")
        print(student.get_details())

    # 8. Display All Faculty Details (Polymorphism)
    elif choice == "8":
        if not faculties:
            print("No faculty members found")
        else:
            print("Faculty Details:")
            print("--------------------------------")
            for faculty in faculties:
                print(faculty.get_details())
                print("--------------------------------")



    # 9. Generate Reports (JSON + CSV)
    elif choice == "9":
        save_students_json(
            [
                {
                    "id": s.id,
                    "name": s.name,
                    "department": s.department,
                    "semester": s.semester,
                    "marks": s.marks
                }
                for s in students
            ],
            "data/students.json"
        )

        generate_csv_report(students, "data/students_report.csv")

    # 10. Exit
    elif choice == "10":
        print("Thank you for using Smart University Management System")
        break

    else:
        print("Invalid Choice")
