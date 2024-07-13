# simple_functions.py 
This script contains two simple functions:
```python
fibonacci(max):
        """ 
    Generate a list of Fibonacci numbers up to a maximum value.

    Args:
        max (int): The upper limit for the Fibonacci sequence. The function will
                   generate Fibonacci numbers up to but not exceeding this value.

    Returns:
        list: A list containing the Fibonacci sequence up to the specified limit.
    """
```

and

```python
def factorial(value):
    """ 
    Calculate the factorial of a given number.

    Args:
        value (int): The number to calculate the factorial of. Must be a non-negative integer.

    Returns:
        int: The factorial of the input number. If the input is 0, the function returns 1.
    """
```

# buggy_function.py
The following function
```python
def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """ 
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
```

is still buggy and shall therefore not be used.
