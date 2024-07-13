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
    # This may have been stolen from stack overflow
    is_prime = True

    for i in range(2, int(user_input)):
        if int(user_input) % i == 0 :
            is_prime = False
            break #break out of the for loop since the number isn't prime

    if is_prime:
        print("Your number is prime")
    else:
        print("your number is not prime")
	

