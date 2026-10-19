#Student Grade Analyzer V3

raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

for record in raw_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Invalid record: {record}")
        continue

    name = fields[0].strip()

    try:
        scores = [int(score.strip()) for score in fields[1:]]
    except ValueError:
        print(f"Invalid score in record: {record}")
        continue

    student_scores[name] = scores

print("Original Student RECORDS:")
sorted_names = sorted(student_scores.keys())

for name in sorted_names:
    print(f"{name}: {student_scores[name]}")

ranking = []
passed_count = 0
failed_count = 0
sum_of_average = 0

for name, scores in student_scores.items():
    if len(scores) == 0:
        print(f"Skipped invalid record: {name} (no scores)")
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    sum_of_average += average
    ranking.append((average, name, highest_score, lowest_score, remark))

ranking.sort(reverse=True)

print("\nStudent Grade Report:")
print("Rank Name\tAverage\tHighest\tLowest\tRemark")

for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5}{name:<10}{round(average, 2):<8}{highest_score:<8}{lowest_score:<7}{remark}")

num_students = len(ranking)
class_average = sum_of_average / num_students if num_students > 0 else 0

print("\nClass Summary:")
print(f"Total Students: {num_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {round(class_average, 2)}")

if num_students > 0:
    highest_student = ranking[0]
    lowest_student = ranking[-1]
    print(f"Highest Student: {highest_student[1]} ({round(highest_student[0], 2)})")
    print(f"Lowest Student: {lowest_student[1]} ({round(lowest_student[0], 2)})")
else:
    print("No valid student records to analyze.")