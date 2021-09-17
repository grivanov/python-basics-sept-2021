limit_bad_grades = int(input())
count_bad_grades = 0
count_grades = 0
sum_grades = 0
problem_name = str()


while count_bad_grades < limit_bad_grades:

    user_input = input()

    if user_input != "Enough":
        problem_name = user_input
        problem_grade = int(input())
    else:
        break

    if problem_grade <= 4:
        count_bad_grades += 1

    sum_grades += problem_grade
    count_grades += 1
    
if count_bad_grades == limit_bad_grades:
    print(f"You need a break, {count_bad_grades} poor grades.")
else:
    average = sum_grades / count_grades
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {problem_name}")

    