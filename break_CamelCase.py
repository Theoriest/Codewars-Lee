def solution(s):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ord_upper = [ord(up) for up in upper_case]
    ord_equivalent = [ord(ch) for ch in s]
    
    ord_upper = set(ord_upper)
    ord_equivalent = set(ord_equivalent)
    
    uppercase_letters = ord_upper.intersection(ord_equivalent)
    
    uppercase_letter = list(uppercase_letters)
    
    for uc in uppercase_letter:
        uc_index = s.index(chr(uc))
        s = s[:uc_index] + " " + s[uc_index:]
    
    return s