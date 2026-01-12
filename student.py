def student_details(student_id, name, age, course):
    result = (
        f"Student ID: {student_id}\n"
        f"Student Name: {name}\n"
        f"Student Age: {age}\n"
        f"Student Course: {course}\n"
    )
    return result


if __name__ == "__main__":
    id = 183
    name = "Prajwal"
    age = 19
    course = "CS"   

    print(student_details(student_id, name, age, course))
