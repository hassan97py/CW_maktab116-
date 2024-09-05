class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract money with different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare money with different currencies")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot compare money with different currencies")
        return self.amount > other.amount

    def display(self):
        print(f"{self.amount:.2f} {self.currency}")


# Create some money objects
usd_10 = Money(10, "USD")
usd_5 = Money(5, "USD")
eur_7 = Money(7, "EUR")

# Perform operations
# print("USD 10 + USD 5:")
# (usd_10 + usd_5).display()  # Output: 15.00 USD

# print("USD 10 - USD 5:")
# (usd_10 - usd_5).display()  # Output: 5.00 USD

# print("USD 10 == USD 10:")
# print(usd_10 == Money(10, "USD"))  # Output: True

print("USD 10 < USD 15:")
print(usd_10 < Money(15, "USD"))  # Output: True

# print("USD 10 > USD 5:")
# print(usd_10 > usd_5)  # Output: True

# try:
#     print("USD 10 + EUR 7:")
#     (usd_10 + eur_7).display()
# except ValueError as e:
#     print(e)  # Output: Cannot add money with different currencies
