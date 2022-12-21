number = int(input())
student_grades_dict = {}
for current_student in range(number):
    student, grade = input().split()
    if student not in student_grades_dict:
        student_grades_dict[student] = []
    student_grades_dict[student].append(float(grade))
for key_student, value_list_grades in student_grades_dict.items():
    grades_as_string = " ".join(str(f"{grade:.2f}") for grade in value_list_grades)
    average_grade = sum(value_list_grades) / len(value_list_grades)
    print(f'{key_student} -> {grades_as_string} (avg: {average_grade:.2f})')