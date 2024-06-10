numbers_input = []
size = int(input("How many? \n"))

for i in range(size):
    numbers_input.append(int(input("Enter number ")))
if numbers_input[0]==numbers_input[size-1]:
    print("ture")
else:
    print("false")
print(numbers_input)
