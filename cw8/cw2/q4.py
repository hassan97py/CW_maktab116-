gvar=2

def outer():
    lvar=3
    def inner():
        print(f'{gvar=}') 
        print(f'{lvar=}')
        nvar=5
        print(f'{nvar=}') 

    nvar=7
    inner()
    print(f'{nvar=}') 
outer()
# print(f'{nvar=}') 
# print(f'{lvar=}') 
