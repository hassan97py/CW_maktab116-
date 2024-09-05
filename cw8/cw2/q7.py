import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Execution time: {elapsed_time:.6f} seconds")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True
    
with Timer():
    x = 0
    for i in range(10000000):
        x += i

print("Result:", x)

