students = [ {"name": "John", "age": 20},
            {"name": "Alice", "age": 18},
            {"name": "Bob", "age": 22},
            {"name": "Emily", "age": 19} ]

sorted_students = sorted(students, key=lambda x: x["age"])

for i in sorted_students:
    print (i)
