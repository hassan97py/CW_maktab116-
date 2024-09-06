import math

def calculate_circle_area(radius):
    # Validate the input
    assert radius >= 0, "Radius must be non-negative."
    
    # Calculate the area of the circle
    area = math.pi * (radius ** 2)
    return area

# Example usage:
try:
    print(calculate_circle_area(5))  # Output: 78.53981633974483
    print(calculate_circle_area(-3))  # This will raise an assertion error
except AssertionError as e:
    print(e)
