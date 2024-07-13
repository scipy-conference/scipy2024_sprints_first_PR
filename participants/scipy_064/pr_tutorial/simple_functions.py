def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
    
def is_prime(intNumber):
    
    if type(i) != int:
        raise OSError("Need to pass int")
    if i <= 1:
        raise OSError("Need to pass integer > 1")
    
    for i in range(1,intNumber):
        if (intNumber % i) == 0:
            return True
    return False
