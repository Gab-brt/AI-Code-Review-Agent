"""Example of a simple and readable Python file for code review testing."""


def calculate_average_grade(students):
    """Calculate the average grade from a list of student dictionaries."""
    if not students:
        return 0

    total = sum(student["grade"] for student in students)
    return total / len(students)


def count_passed_students(students, passing_grade=50):
    """Count how many students have a grade greater than or equal to the passing grade."""
    return sum(1 for student in students if student["grade"] >= passing_grade)


def create_summary(students):
    """Create a short summary of the student results."""
    average_grade = calculate_average_grade(students)
    passed_students = count_passed_students(students)

    return {
        "total_students": len(students),
        "average_grade": average_grade,
        "passed_students": passed_students,
    }


def display_summary(summary):
    """Display the student summary in a readable format."""
    print("Student Summary")
    print("----------------")
    print(f"Total students: {summary['total_students']}")
    print(f"Average grade: {summary['average_grade']:.2f}")
    print(f"Passed students: {summary['passed_students']}")


def main():
    """Run the student summary example."""
    students = [
        {"name": "Alice", "grade": 92},
        {"name": "Bob", "grade": 45},
        {"name": "Charlie", "grade": 67},
    ]

    summary = create_summary(students)
    display_summary(summary)


if __name__ == "__main__":
    main()
