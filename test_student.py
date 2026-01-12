from student import student_details

def test_student_details():
    expected_output = (
        "Student_Id:183\n"
        "Student_Name:prajwal\n"
        "age:19\n"
        "course:CS\n"
    )

    assert student_details(183,"prajwal",19,"CS") == expected_output
    
