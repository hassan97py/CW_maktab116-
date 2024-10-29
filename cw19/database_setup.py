from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db', echo=True)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(String)
    def __repr__(self):
        return f"<Student(name='{self.name}', age={self.age}, grade='{self.grade}')>"

# Create the students table in the database 
Base.metadata.create_all(engine) 
  
Session = sessionmaker(bind=engine) 
session = Session()

# Add students 
# student1 = Student(name='Alice', age=20, grade='A') 
# student2 = Student(name='Bob', age=22, grade='B') 
 
# # Add to the session and commit the changes 
# session.add(student1) 
# session.add(student2) 
# session.commit()

# print("Students added successfully!")

# Query all students 
# students = session.query(Student).all() 
# for student in students: 
#     print(student)
    
# # Query a student by name 
# alice = session.query(Student).filter_by(name='Alice').first() 
# print(alice)

# Update Bob's grade 
# bob = session.query(Student).filter_by(name='Bob').first() 
# bob.grade = 'A+' 
# session.commit() 
 
# print(f"Updated {bob.name}'s grade to {bob.grade}")

# Delete a student from the database 
# student_to_delete = session.query(Student).filter_by(name='Alice').first() 
# session.delete(student_to_delete) 
# session.commit() 
 
# print(f"Deleted student {student_to_delete.name}")

session.close()
