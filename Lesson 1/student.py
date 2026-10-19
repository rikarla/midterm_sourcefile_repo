#Define students score
student_scores = [89, 99, 90, 68, 90]

#display students scores
print("Student Scores:")
for score in student_scores:
    print(score)
print()

#Calculation
total_score = 0
highest_score = student_scores[0]
lowest_score = student_scores[0]
passed_count = 0
failes_count = 0

#Analyzed Scores
for i, score  in enumerate(student_scores, start=1):
    #Determine grade and pass/fail
    if 90 <= score <= 100:
        grade = "Excellent"
        status = "Pass"
        passed_count += 1
    elif 80 <= score <= 89:
        grade = "Very Good"
        status = "Pass"
        passed_count += 1
    elif 75 <= score <= 79:
        grade = "Good"
        status = "Pass"
        passed_count += 1      
    else:
        grade = "Failed"
        status = "Failed"
        failes_count += 1

       #Display results
    print(f"Student {i}: {score} - {grade} - {status}")

    #Update totals
    total_score += score

    #update highest and lowest scores
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

#Calculate average score
average_score = total_score / len(student_scores)

#display summary
print(f"\nTotal Score: {total_score}")
print(f"Average Score: {average_score:.0f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Number of Students who passed: {passed_count}")
print(f"Number of Students who failed: {failes_count}")