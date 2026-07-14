"""
My intial solution_1 is as follows
I tried to used ord() method to identify uppercase letters by defining a list of the ord equivalents of all the uppercase letters
My mistake was taking the input string which is iterable and converting it into a set. 
These caused me to miss cases where a string has two similar uppercase letters
That is a char that appears twice as an upper case letter in the same string
I did these in the hope of reducing search as I could use the intersect method of sets to identify uppercase letters from the sets of
    ord equivalents of all uppercase letters and ord equivalent of the string
"""
def solution_1(s):
    #Define Uppercase Alphabet
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Find ord equivalents for the Uppercase Alphabet and Camel Case String and store them as lists
    ord_upper = [ord(up) for up in upper_case]
    ord_equivalent = [ord(ch) for ch in s]

    #Convert the ord equivalent lists to sets
    ord_upper = set(ord_upper)
    ord_equivalent = set(ord_equivalent)
    
    #Find the Intersection Between the two sets and store it as a list
    uppercase_letters = ord_upper.intersection(ord_equivalent)
    uppercase_letter = list(uppercase_letters)
    
    #iterate over the intersection list to break the Camel Case string and return the final string.
    for uc in uppercase_letter:
        uc_index = s.index(chr(uc))
        s = s[:uc_index] + " " + s[uc_index:]
    return s

"""
My final solution is as follows
I used the isupper() method for characters, iterating over the Camel case string 
I stored characters that were not Uppercase as char in a list and char that were Upper were stored as a string of an empty space and the 
    Upper case char.
These was all achieved using a List comprehension.
"""
def solution(s):
    return "".join(" " + ch if ch.isupper() else ch for ch in s)