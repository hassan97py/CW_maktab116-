
def convertTuple(tup):
    return list(map(' '.join, tup))
     

tuples_list = [('Hello', 'World'), ('Open', 'AI'), ('GPT', '3')] 
print(convertTuple(tuples_list))


