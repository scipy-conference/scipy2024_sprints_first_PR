def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values

# Factorial Of Negative Numbers Shouldnt Give Output
def factorial(value):
    if value < 0:
        raise Exception("Factorial Not defined for Negative numbers")
        return 0
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

if __name__ == "__main__":
    print(factorial(-1))