from student import student_details

def test_student_details():
      expected_output = (
        "Student_ID:183\n"
        "Student_Name:prajwal\n"
        "Student_Age:19\n"
        "Student_Course:CS\n"
      )

    assert student_details(183,"prajwal",19,"CS") == expected_output
    
