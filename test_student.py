from student import student_details

def test_student_details():
    expected_output = (
        "id: 183\n"
        "name: Prajwal\n"
        "age: 19\n"
        "course: CS\n"
    )

    assert student_details(183, "Prajwal", 19 , "CS") == expected_output
    