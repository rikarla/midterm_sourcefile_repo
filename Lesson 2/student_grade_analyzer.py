"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    # TODO: Use if/elif/else and return (classification, status).
    if grade < 0 or grade > 100:
        return ("Invalid", "Invalid")
    if grade >= 90:
        return ("Excellent", "Passed")
    elif grade >= 85:
        return ("Very Good", "Passed")
    elif grade >= 80:
        return ("Good", "Passed")
    elif grade >= 75:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    # TODO: Open filename safely by using with open(...) and try/except.
    # TODO: Loop through the file, clean each line, and skip blank lines.
    # TODO: Split each record and check that it contains three fields.
    # TODO: Convert and validate the grade.
    # TODO: Append a dictionary for every valid record.
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    continue
                student_id, name, grade_str = parts
                try:
                    grade = float(grade_str)
                except ValueError:
                    continue
                if 0 <= grade <= 100:
                    students.append({
                        "student_id": student_id,
                        "name": name,
                        "grade": grade
                    })
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    # TODO: Use one loop to update the accumulator, counters, highest, and lowest.
    # Do not use sum(), max(), or min() for this part.
    for student in students:
        grade = student["grade"]
        total_grade += grade

        classification, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student
        if grade < lowest_student["grade"]:
            lowest_student = student

    # TODO: Calculate the average and return all results in a dictionary.
    average = total_grade / len(students)
    return {
        "number_of_students": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student,
    }


def display_students(students):
    """Display all student records in a formatted table."""
    # TODO: Print column headings.
    # TODO: Loop through students and call classify_grade for each record.
    if not students:
        print("No student records to display.")
        return

    print("\nALL STUDENTS")
    print("-" * 70)
    print(f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<20} {'Status'}")
    print("-" * 70)

    for student in students:
        student_id = student["student_id"]
        name = student["name"]
        grade = student["grade"]
        classification, status = classify_grade(grade)

        # Shorten name if necessary (max 20 characters)
        if len(name) > 20:
            name = name[:17] + "..."

        print(f"{student_id:<12} {name:<20} {grade:<8.2f} {classification:<20} {status}")

    print("-" * 70)


def display_statistics(statistics):
    """Display the calculated class statistics."""
    # TODO: Display every value in statistics clearly.
    if not statistics:
        print("No statistics to display.")
        return

    print("\nCLASS STATISTICS")
    print("-" * 40)
    print(f"Number of students: {statistics['number_of_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}")
    print("-" * 40)


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    # TODO: Make keyword lowercase and remove extra whitespace.
    # TODO: Use a loop and partial, case-insensitive matching.
    keyword = keyword.strip().lower()
    if not keyword:
        return matches

    for student in students:
        student_id = student["student_id"].lower()
        name = student["name"].lower()
        if keyword in student_id or keyword in name:
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    # TODO: Safely open filename in write mode.
    # TODO: Write all student results and statistics.
    # TODO: Handle a possible OSError.
    try:
        with open(filename, 'w') as file:
            file.write("STUDENT GRADE REPORT\n")
            file.write("=" * 70 + "\n\n")

            file.write("STUDENT RESULTS\n")
            file.write("-" * 70 + "\n")
            file.write(f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<20} {'Status'}\n")
            file.write("-" * 70 + "\n")

            for student in students:
                student_id = student["student_id"]
                name = student["name"]
                grade = student["grade"]
                classification, status = classify_grade(grade)

                if len(name) > 20:
                    name = name[:17] + "..."

                file.write(f"{student_id:<12} {name:<20} {grade:<8.2f} {classification:<20} {status}\n")

            file.write("-" * 70 + "\n\n")

            file.write("CLASS STATISTICS\n")
            file.write("-" * 40 + "\n")
            file.write(f"Number of students: {statistics['number_of_students']}\n")
            file.write(f"Class average: {statistics['average']:.2f}\n")
            file.write(f"Passed: {statistics['passed']}\n")
            file.write(f"Failed: {statistics['failed']}\n")
            file.write(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}\n")
            file.write(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}\n")
            file.write("-" * 40 + "\n")

        print(f"Report successfully saved to {filename}")
    except OSError as e:
        print(f"Error saving report: {e}")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        # TODO: Call the appropriate function for choices 1 to 4.
        # TODO: For choice 3, ask for a keyword and display every match.
        # TODO: Use break for choice 5.
        # TODO: Use continue after an invalid choice.

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student ID or name to search: ")
            matches = search_student(students, keyword)
            if matches:
                print(f"\nFound {len(matches)} matching student(s):")
                display_students(matches)
            else:
                print("No matching students found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting Student Grade Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")
            continue


if __name__ == "__main__":
    main()