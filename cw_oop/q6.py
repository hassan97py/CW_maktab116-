class Calculator:
    @classmethod
    def add(cls, a, b):
        return a + b

c = Calculator.add(4, 5)
print(f"c: {c}")