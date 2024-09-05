class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return RationalNumber(new_numerator, new_denominator)
        else:
            raise TypeError("Can only add RationalNumber objects.")

    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return RationalNumber(new_numerator, new_denominator)
        else:
            raise TypeError("Can only subtract RationalNumber objects.")

    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return RationalNumber(new_numerator, new_denominator)
        else:
            raise TypeError("Can only multiply RationalNumber objects.")

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return RationalNumber(new_numerator, new_denominator)
        else:
            raise TypeError("Can only divide RationalNumber objects.")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def gcd(a, b):
        while b:
            a=b
            b=a%b
            # a, b = b, a % b
        return a


# r1 = RationalNumber(9, 3)
# print(r1)
print(RationalNumber.gcd(9,3))
# r2 = RationalNumber(1, 3)

# print(r1 + r2) # Output: 5/6
# print(r1 - r2) # Output: 1/6
# print(r1 * r2) # Output: 1/6
# print(r1 / r2) # Output: 3/2