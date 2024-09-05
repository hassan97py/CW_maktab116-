def sum1(n):
    s=0
    while n>0:
        s=n+s
        n-=1
    return s
a=sum1(3)
print(a)  


# def sum(num):
#     if num <= 1 :
#         return num
#     return num + sum(num - 1)

# inp = int(input("Number: \n"))
# print(f"Result: {sum(inp)}")
    
    