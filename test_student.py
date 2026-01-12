from student import student_details

def test_student_details():
    expected_output = (
        "Student_ID:183\n"
        "Student_Name:Prajwal\n"
        "Student_Age:19\n"
        "Student_Course:CS\n"
    )
    assert student_details(183, "Prajwal", 19, "CS") == expected_output
