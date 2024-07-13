def fibonacci(max):
    """
    Generate a list of Fibonacci numbers up to a maximum value.

    Args:
        max (int): The upper limit for the Fibonacci sequence. The function will
                   generate Fibonacci numbers up to but not exceeding this value.

    Returns:
        list: A list containing the Fibonacci sequence up to the specified limit.
    """
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    """
    Calculate the factorial of a given number.

    Args:
        value (int): The number to calculate the factorial of. Must be a non-negative integer.

    Returns:
        int: The factorial of the input number. If the input is 0, the function returns 1.
    """
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

