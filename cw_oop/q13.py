
class MathUtil:
    @classmethod
    def is_prime(cls, number):

        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

print(MathUtil.is_prime(7))  
print(MathUtil.is_prime(12))  
print(MathUtil.is_prime(17))  
print(MathUtil.is_prime(1))   
