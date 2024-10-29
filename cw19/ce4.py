
​from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table, func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()

# Many-to-Many relationship between Books and Authors
book_author_association = Table(
    'book_author', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

# Many-to-Many relationship between Books and Members (via Loans)
class Loan(Base):
    __tablename__ = 'loans'
    
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    borrowed_date = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime, default=datetime.now() + timedelta(days=14))

    book = relationship('Book', back_populates='loans')
    member = relationship('Member', back_populates='loans')

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    isbn = Column(String, unique=True)

    authors = relationship('Author', secondary=book_author_association, back_populates='books')
    loans = relationship('Loan', back_populates='book')

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', secondary=book_author_association, back_populates='authors')

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    membership_card_id = Column(Integer, ForeignKey('membership_cards.id'))

    membership_card = relationship('MembershipCard', back_populates='member')
    loans = relationship('Loan', back_populates='member')

class MembershipCard(Base):
    __tablename__ = 'membership_cards'
    
    id = Column(Integer, primary_key=True)
    card_number = Column(String, unique=True)

    member = relationship('Member', back_populates='membership_card')

# Database setup
engine = create_engine('sqlite:///library_management.db')  # Replace with your database URL
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example CRUD Operations
def add_book(title, isbn, authors):
    book = Book(title=title, isbn=isbn)
    book.authors.extend(authors)
    session.add(book)
    session.commit()

def add_member(name, card_number):
    membership_card = MembershipCard(card_number=card_number)
    member = Member(name=name, membership_card=membership_card)
    session.add(member)
    session.commit()

def record_loan(book_id, member_id):
    loan = Loan(book_id=book_id, member_id=member_id)
    session.add(loan)
    session.commit()

def get_books_borrowed_by_member(member_id):
    return session.query(Book).join(Loan).filter(Loan.member_id == member_id).all()

def get_members_with_more_than_n_books(n):
    return session.query(Member).join(Loan).group_by(Member.id).having(func.count(Loan.id) > n).all()

def find_books_not_borrowed_in_last_days(days):
    cutoff_date = datetime.now() - timedelta(days=days)
    return session.query(Book).outerjoin(Loan).filter(Loan.borrowed_date < cutoff_date).all()

# Transaction Management
def create_loan_with_transaction(book_id, member_id):
    try:
        loan = Loan(book_id=book_id, member_id=member_id)
        session.add(loan)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Transaction failed: {e}")

# Example Usage
# Add books, members, and record loans as needed.
