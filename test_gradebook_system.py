import os
import instructors
import gradebook

def test_get_instructor_by_id():
    # Clear the instructors_list and add a dummy instructor.
    instructors.instructors_list.clear()
    dummy_inst = instructors.Instructor("123", "John", "CS101", "Intro to CS")
    instructors.instructors_list.append(dummy_inst)
    
    # Test valid retrieval.
    result = instructors.get_instructor_by_id("123")
    assert result is not None, "Instructor should be found."
    assert result.name == "John", "Instructor name should be 'John'."
    
    # Test retrieval with a non-existent ID.
    result_none = instructors.get_instructor_by_id("999")
    assert result_none is None, "Non-existent instructor should return None."

def test_load_and_save_grades():
    # Set up a test file for the gradebook.
    test_file = "test_grades.csv"
    gradebook.GRADEBOOK_FILE = test_file
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # Initially, load_grades should return an empty list.
    grades = gradebook.load_grades()
    assert grades == [], "Expected empty grade list for a new file."
    
    # Create a dummy grade record.
    dummy_grade = {"course_ID": "CS101", "student_ID": "s001", "grade": "A"}
    grades.append(dummy_grade)
    gradebook.save_grades(grades)
    
    # Reload and check the grade.
    loaded_grades = gradebook.load_grades()
    assert len(loaded_grades) == 1, "Should have one grade record."
    assert loaded_grades[0]["grade"] == "A", "Grade should be 'A'."
    
    """
    # Clean up the test file.
    if os.path.exists(test_file):  #Remove the " for this function to remove test grades
        os.remove(test_file)
    """
def run_tests():
    test_get_instructor_by_id()
    test_load_and_save_grades()
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
