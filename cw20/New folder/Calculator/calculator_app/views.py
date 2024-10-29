from django.shortcuts import render

def home(request):
    return render(request, 'calculator.html')

def add(request, a, b):
    result = a + b
    return render(request, 'result.html', {'a': a, 'b': b, 'operation': 'Addition', 'result': result})

def subtract(request, a, b):
    result = a - b
    return render(request, 'result.html', {'a': a, 'b': b, 'operation': 'Subtraction', 'result': result})

def multiply(request, a, b):
    result = a * b
    return render(request, 'result.html', {'a': a, 'b': b, 'operation': 'Multiplication', 'result': result})

def divide(request, a, b):
    if b != 0:
        result = a / b
    else:
        result = 'undefined'
    return render(request, 'result.html', {'a': a, 'b': b, 'operation': 'Division', 'result': result})
