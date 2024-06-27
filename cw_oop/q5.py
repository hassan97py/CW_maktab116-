class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

st1 = Student('Amir', 22, 5674586)
st1.name = 'Reza'
print(st1.name)
print(st1.age)
print(st1.student_id)
p1 = Person('Ali', 21)
print(p1.name)
print(p1.age)