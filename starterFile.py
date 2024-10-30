import math

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
            # outputs as 0 to avoid errors when c is returned
            break
        else: 
            break
    return c

def process_list(input_list):
    """
    Multiple exception handling.
    The functionill take an input list;
    a Try-except block will handle Typeerrors and ValueErrors
    inputs: input_list
    outputs: error_list, output_list with elements removed.
    structure: try-except block in for loop
    """
    error_list = []
    # list of indexes with their errors 
    square_sum = 0 
    for x in input_list: 
        try:
            output = (x*x)
            # attempts to square the of element in input_list to an output_list.
        except (ValueError):
            error_list.append(f"{x}, ValueError")
            pass
            # silently skips these failures but records the error into error_list
        except (TypeError):
            error_list.append(f"{x}, TypeError")
            pass
        else: 
            error_list.append(f"{x}, Works")
            # adds output to square_sum
            square_sum = square_sum + output
    return square_sum

def nested_operations(a, b):
    """
    1. Converts both a and b to integers
        Implement except ValueError to catch conversion issues
    2. divides a by b 
    3. find the square root of the result
    input: a / b
    output: ValueError message, ZeroDivisionError and c(sqrt(a/b))
    structure: nested try-except block
    """
    try:
        a = int(a)
        b = int(b) 
        try:
            c = a/b
        except ZeroDivisionError: 
            c = 0
            return f"You cannot divide any number by 0:\n {a}/{b} = error"
    except ValueError:
        # branch of loop catches ValueError exception
        c = 0
        return f"You entered non-integer numbers:\n {a}/{b} = error"
    else:
        return f"{a}/{b} = {c}"
    
def process_input():
    """
    1. Take input a from the user
    2. try: block to convert input into a float and square it
    3. except: block to handle value error and output the appropriate message
    4. else: print result
    5. finally: print "Processing complete" then output either the value of C
    """
    a = input("Please input an int or float: ")
    try:
        a = float(a)
        # attempt to convert a
        c = a*a
        # attempts to execute arithmetic on converted a 
    except ValueError:
        output = f"Processing complete... \nInput: {a} is not a floating point :<"
    else:
        output = f"Processing complete... \n{a} to the power of 2 = {c}"
    finally: 
        return output
    
def main():
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(process_list([1, '2', 3, 'four', 5]))    
    print(nested_operations(16, 4))
    print(nested_operations(10, 0))
    print(nested_operations('a', 5))
    print(process_input())

main()