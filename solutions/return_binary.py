def add_binary(a,b):
    sum = a + b
    binary = ""
    while sum !=0:
        if sum % 2 == 1:
            binary = binary + "1"
            sum = sum // 2
        else:
            binary = binary + "0"
            sum = sum // 2 
    return binary[::-1]