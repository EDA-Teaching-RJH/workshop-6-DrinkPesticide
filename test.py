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
print(process_input())