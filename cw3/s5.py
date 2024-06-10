
# import functools 

# lis = [1,3,2,4,5] 

# print(functools.reduce(lambda a, b: a*b, lis)) 


from functools import reduce

def multiply_numbers():

    numbers_str = input("Enter numbers: \n")
    numbers = [float(x) for x in numbers_str.split()]
    
    return reduce(lambda x, y: x * y, numbers)

result = multiply_numbers()
print(f"The product of the numbers is: {result}")
