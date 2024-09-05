import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Todo item structure
class TodoItem:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

# HTTP request handler
class TodoHandler(BaseHTTPRequestHandler):
    todos = []  # Initialize an empty todo list
    next_id = 1  # To keep track of the next ID for new todo items
    def __repr__(self) -> str:
        return f"User(id=(self.id))"
    def do_GET(self):
        # Handle GET request
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            # Convert todo items to JSON
            response = json.dumps([todo.__dict__ for todo in self.todos])
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # Handle POST request
        if self.path == '/':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            todo_data = json.loads(post_data)

            
            # Create a new TodoItem
            new_todo = TodoItem(self.next_id, todo_data['title'], todo_data['description'])
            self.todos.append(new_todo)
            self.next_id += 1

            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps(new_todo.__dict__)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=TodoHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    
    run()

# curl -X POST http://localhost:8080/ -H "Content-Type: application/json" -d '{"title": "Sample Todo", "description": "This is a sample todo item."}'
# curl -X POST http://localhost:8080/ -H "Content-Type: application/json" -d '{"id": 1, "title": "Test Todo", "description": "This is a test todo."}' 
# from typing import List
# from typing import Optional
# from sqlalchemy import ForeignKey
# from sqlalchemy import String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationshclass 
# class Base(DeclarativeBase):
#     pass
# class User(Base):
#     __tablename__ = "user_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship
#     (back_populates="user", cascade="all, delete-orphan")
# def __repr__(self) -> str:
#     return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"