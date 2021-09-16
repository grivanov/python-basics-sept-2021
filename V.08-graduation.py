student_name = input()

failed_years = 0
passed_years = 1
sum_of_grades = 0

while passed_years <= 12:
    year_grade = float(input())

    if year_grade >= 4:
        sum_of_grades += year_grade
        passed_years += 1
    else:
        failed_years += 1
    
    if failed_years == 2:
        break


if failed_years == 2:
    print(f"{student_name} has been excluded at {passed_years} grade")
else:
    average_grade = sum_of_grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
