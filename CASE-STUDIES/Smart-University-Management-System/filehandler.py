import json
import csv
from exceptions import FileAccessError


def save_students_json(students, path):
    try:
        with open(path, "w") as f:
            json.dump(students, f, indent=4)
        print("Student data successfully saved to students.json")
    except FileNotFoundError:
        raise FileAccessError("Error: File not found")


def generate_csv_report(students, path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.id, s.name, s.department, round(avg, 1), grade])
