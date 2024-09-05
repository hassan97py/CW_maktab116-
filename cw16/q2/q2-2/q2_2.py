class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, grade):
        if self.is_student_exist(student_id):
            raise ValueError(f"Student with ID {student_id} already exists.")
        new_student = Student(student_id, name, grade)
        self.students.append(new_student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return
        raise ValueError(f"Student with ID {student_id} does not exist.")

    def get_student_grade(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.grade
        raise ValueError(f"Student with ID {student_id} does not exist.")

    def is_student_exist(self, student_id):
        return any(student.student_id == student_id for student in self.students)

# Example Usage:
if __name__ == "__main__":
    manager = StudentManager()
    manager.add_student(1, "Alice", 90)
    manager.add_student(2, "Bob", 85)

    print(manager.get_student_grade(1))  # Output: 90
    print(manager.is_student_exist(2))    # Output: True

    manager.remove_student(1)
    print(manager.is_student_exist(1))    # Output: False
