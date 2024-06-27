class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5/9)
    
    @staticmethod
    def to_celcius(fahrenheit):
        return (fahrenheit - 32) * 5/9

temp_celsius = Temperature(25)
print(temp_celsius.celsius)
print(temp_celsius.to_fahrenheit())

temp_fahrenheit = Temperature.from_fahrenheit(77)
print(temp_fahrenheit.celsius)

print(Temperature.to_celcius(100))