
def my_range(start=0, stop=10, step=1):
    
    if not isinstance(start, int) or not isinstance(stop, int) or (step is not None and not isinstance(step, int)):
        raise ValueError("All parameters must be integers.")
    
    if step == 0:
        raise ValueError("Step cannot be zero.")
    
    num_steps = (stop - start) / step
    # print(num_steps)
    if num_steps>= 0:
        
        for i in range(start,stop,step):
            yield i
    else:
        raise ValueError("Step size is not large enough to reach the stop value.")  
    
result = list(my_range(1, 10, 2))
# result1 = list(my_range(1.5, 10, 2))
# result2 = list(my_range(1, 10, 0))
# result3 = list(my_range(10, 1, 2))
print(result)
# print(result1)
# print(result2)
# print(result3)