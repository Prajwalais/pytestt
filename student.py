def student_details(student_id,name,age,course):
    result = (
        f"Student_ID:{student_id}\n"
        f"Student_Name:{name}\n"
        f"Student_Age:{age}\n"
        f"Student_Course:{course}\n"
    )
    return result


if __name__ == "__main__":
    id=183
    name="Prajwal"
    age=19
    course="CS"   

    print(student_details(id,name,age,course))
