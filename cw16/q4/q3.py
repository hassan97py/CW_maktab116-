def calculate_average(numbers):
    # Validate the input
    assert len(numbers) > 0, "The list of numbers must not be empty."
    
    # Calculate the average
    average = sum(numbers) / len(numbers)
    return average

# Example usage:
try:
    print(calculate_average([10, 20, 30]))  # Output: 20.0
    print(calculate_average([]))             # This will raise an assertion error
except AssertionError as e:
    print(e)
