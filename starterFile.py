#Your code goes here. 

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
    outputs: error report, output_list with elements removed.
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
            # silently skips these failures
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
    Converts both a and b to integers
    divides a by b 
    find the square root of the result
    input: a / b
    output: ValueError, ZeroDivisionError and sqrt(a/b)
    structure: nested try-except block
    """


def process_input():


main()
