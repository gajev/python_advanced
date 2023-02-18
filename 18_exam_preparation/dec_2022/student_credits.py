def students_credits(*args):
    student_credits = 0
    student_dict = {}
    for current_course in args:
        name, course_credits, max_points, diyan_points = current_course.split("-")
        current_credits = (int(diyan_points) / int(max_points)) * int(course_credits)
        student_credits += current_credits
        if name not in student_dict:
            student_dict[name] = 0
        student_dict[name] = float(current_credits)
    sorted_dict = sorted(student_dict.items(), key=lambda x: -x[1])
    result = ""
    if student_credits >= 240:
        result += f"Diyan gets a diploma with {student_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {(240 - student_credits):.1f} credits more for a diploma.\n"
    for final_tuple in sorted_dict:
        result += f"{final_tuple[0]} - {final_tuple[1]:.1f}\n"
    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)