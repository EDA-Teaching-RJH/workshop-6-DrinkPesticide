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
print(process_list([1, 2, 3, "5", 56]))

