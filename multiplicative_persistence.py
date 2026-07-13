"""
### initial solution but faced challenge as I could not reset the global variable count to zero to handle a different number for the function 
as these required settiong count to 0 through assignment. 

### for these i was actually counting the number of times the function was called.

### could also be solved using while loop but i wanted to implement recursion 

### ended up defining a helper function allowing me  to recent counter to 0 in the main function.

count = 0
def persistence(n):
    global count
    count += 1
    length = len(str(n))
    number = str(n)
    result = 1

    for digit in number:
        result = result * int(digit)
    if len(str(result)) != 1:
        return persistence(result)
    else:
        return count

"""
def persistence(n):
    global count
    count = 0
    return _persist_helper(n)

def _persist_helper(n):
    global count
    number = str(n)
    if len(number) == 1:
        return count
    result = 1
    for digit in number:
        result *= int(digit)
    count += 1
    return _persist_helper(result)