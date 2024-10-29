from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///students_address.db', echo=False)
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_name = Column(String)
    student = relationship("Student", back_populates="courses")

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    street = Column(String)
    city = Column(String)
    student = relationship("Student", back_populates="address")

    def __repr__(self):
        return f"<Address(City='{self.city}'>"

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(String)
    # One-to-One relationship
    address = relationship("Address", uselist=False, back_populates="student")
    courses = relationship("Course", back_populates="student")

    def __repr__(self):
        return f"<Student(name='{self.name}'>"
# Create the students table in the database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# • Here, a Student has one Address, and each Address is linked to one Student.
# • uselist=False ensures this is a one-to-one relationship.
# 2. Creating and Associating Data
# python
# Copy code
# 
# # Add a student and their address
# student = Student(name='Charlie', age=25, grade='B')
# address = Address(street='123 Main St', city='New York', student=student)
# session.add(student)
# session.add(address)

# Charlie = session.query(Student).filter_by(name='Charlie').first()
# print(Charlie)
# print(Charlie.address)
# print(type(Charlie.address))

# Add a student with multiple courses
student = Student(name='Diana', age=22, grade='A')
course1 = Course(course_name='Math', student=student)
course2 = Course(course_name='Physics', student=student)
session.add(student)
session.add(course1)
session.add(course2)

session.commit()
# session.close()