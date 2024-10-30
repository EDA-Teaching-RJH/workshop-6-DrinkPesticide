def safe_divide(a, b):
    """
    The function will take two variables as integers
    The function will output their division
    The function will use try except block to handle the ZeroDivisionError
    input parameters: integers a and b
    returns the quotient of a and b (c) or error messages
    """
    i = 0
    while True:
        try:
            c = a/b
        except ZeroDivisionError: 
            print("Cannot divide by zero")
            c = 0 
            break
        else: 
            break
    return c
print(safe_divide(3, 0))