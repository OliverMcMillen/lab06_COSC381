import os
import instructors
import gradebook
from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"  # Define the date format for timestamp storage


def test_get_instructor_by_id():
    # Clear the instructors_list and add a dummy instructor.
    instructors.instructors_list.clear()
    dummy_inst = instructors.Instructor("123", "John", "CS101", "Intro to CS")
    instructors.instructors_list.append(dummy_inst)
    
    # Test valid retrieval.
    result_list = instructors.get_instructor_by_id("123")
    assert result_list, "Instructor should be found."  # Ensure the list is not empty
    result = result_list[0]  # Get the first instructor

    assert result.name == "John", "Instructor name should be 'John'."
    
    # Test retrieval with a non-existent ID.
    result_none = instructors.get_instructor_by_id("999")
    assert result_none == [], "Non-existent instructor should return None."

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
    
def test_add_and_edit_grade():
    """Test adding a grade with a timestamp and editing it within the allowed time."""
    
    # Set up a test file for the gradebook.
    test_file = "test_grades.csv"
    gradebook.GRADEBOOK_FILE = test_file
    if os.path.exists(test_file):
        os.remove(test_file)

    # Add a dummy instructor (since grade entry requires an instructor)
    instructor_dummy = instructors.Instructor("101", "Dr. Smith", "CS101", "Intro to CS")

    # Create a grade entry
    initial_timestamp = datetime.now().strftime(DATE_FORMAT)
    dummy_grade = {
        "course_ID": "CS101",
        "student_ID": "s001",
        "grade": "A",
        "timestamp": initial_timestamp  # Store timestamp at creation
    }

    # Save the grade
    grades = [dummy_grade]
    gradebook.save_grades(grades)

    # Reload to verify it was saved
    loaded_grades = gradebook.load_grades()
    assert len(loaded_grades) == 1, "There should be exactly one grade record."
    assert loaded_grades[0]["grade"] == "A", "Initial grade should be 'A'."
    assert loaded_grades[0]["timestamp"] == initial_timestamp, "Timestamp should be set at creation."

    # Edit the grade (simulate within the 7-day allowed window)
    new_grade = "B"
    for entry in loaded_grades:
        if entry["student_ID"] == "s001":
            entry["grade"] = new_grade  # Change grade
            preserved_timestamp = entry["timestamp"]  # Keep timestamp unchanged

    # Save changes
    gradebook.save_grades(loaded_grades)

    # Reload to verify timestamp remains unchanged
    reloaded_grades = gradebook.load_grades()
    assert reloaded_grades[0]["grade"] == "B", "Grade should be updated to 'B'."
    assert reloaded_grades[0]["timestamp"] == preserved_timestamp, "Timestamp should not change after editing."

    print("Test Passed: Grade added and edited successfully within allowed time.")

    """
    # Clean up the test file.
    if os.path.exists(test_file):  #Remove the " for this function to remove test grades
        os.remove(test_file)
    """
def run_tests():
    test_get_instructor_by_id()
    test_load_and_save_grades()
    test_add_and_edit_grade()
    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
