def get_student_grade(percentage):
    # Validate the input
    assert 0 <= percentage <= 100, "Percentage must be between 0 and 100."
    
    # Determine the grade based on the percentage
    if 90 <= percentage <= 100:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'

# Example usage:
try:
    print(get_student_grade(85))  # Output: B
    print(get_student_grade(55))  # Output: F
    print(get_student_grade(110))  # This will raise an assertion error
except AssertionError as e:
    print(e)
