# Project 2 - Student Performance Analyzer

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Priya", "marks": 91},
    {"name": "Neha", "marks": 78},
    {"name": "Rohit", "marks": 88}
]


def get_performance(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    else:
        return "Needs Improvement"


def calculate_average(students):
    marks = [student["marks"] for student in students]
    return sum(marks) / len(marks)


print("STUDENT PERFORMANCE REPORT")
print("=" * 30)

for student in students:
    performance = get_performance(student["marks"])

    print(
        student["name"],
        "- Marks:", student["marks"],
        "- Performance:", performance
    )

average = calculate_average(students)

highest = max(students, key=lambda student: student["marks"])
lowest = min(students, key=lambda student: student["marks"])

print("=" * 30)
print("Average Marks:", average)
print("Highest Marks:", highest["name"], "-", highest["marks"])
print("Lowest Marks:", lowest["name"], "-", lowest["marks"])
