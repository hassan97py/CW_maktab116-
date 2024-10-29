from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table 

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import joinedload 



engine = create_engine('sqlite:///students_mtm.db', echo=False)
Base = declarative_base()



 
# Association table for the many-to-many relationship 
student_course_association = Table('student_course', Base.metadata, 
    Column('student_id', Integer, ForeignKey('students.id')), 
    Column('course_id', Integer, ForeignKey('courses.id')) 
) 
 
class Course(Base): 
    __tablename__ = 'courses' 
     
    id = Column(Integer, primary_key=True) 
    course_name = Column(String) 
 
    # Many-to-Many relationship 
    students = relationship("Student", secondary=student_course_association, back_populates="courses") 
 
class Student(Base): 
    __tablename__ = 'students' 
     
    id = Column(Integer, primary_key=True) 
    name = Column(String) 
    age = Column(Integer) 
    grade = Column(String) 
 
    # Many-to-Many relationship 
    courses = relationship("Course", secondary=student_course_association, back_populates="students") 
    
student1 = Student(name='Eve', age=21, grade='A') 
student2 = Student(name='Frank', age=23, grade='B') 
 
course1 = Course(course_name='Math') 
course2 = Course(course_name='Physics') 
 
Base.metadata.create_all(engine) 



# Many-to-Many relationship: enrolling students in courses 
student1.courses.append(course1) 
student1.courses.append(course2) 
student2.courses.append(course1) 


Session = sessionmaker(bind=engine) 
with Session() as session:
    # session.add(student1) 
    # session.add(student2) 
    # session.commit() 
    session.query(Course).filter_by(course_name='Math').first()
    print(math.students)
 