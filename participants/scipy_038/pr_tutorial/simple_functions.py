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

def is_prime(number):
    # I've learned my lesson and will no longer steal from stackoverflow.
    # Now I am stealing from TruDarkSider
    if value %2 == 0 or value == 0:
        return False
    else:
        return True  
