
from sqlalchemy.orm import joinedload 
 
# Eager load the courses when querying students 
students_with_courses = session.query(Student).options(joinedload(Student.courses)).all() 
 
for student in students_with_courses: 
    print(f"Student: {student.name}") 
    for course in student.courses: 
        print(f"  Course: {course.course_name}")