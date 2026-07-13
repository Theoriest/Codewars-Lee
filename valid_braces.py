test_cases = ["()","(}","[]","[(])","{}","{}()[]","([{}])","([}{])","{}({})[]","(({{[[]]}}))","(((({{",")(}{][","())({}}{()][]["]

"""
def valid_braces(string):
    pair = {"(":")","{":"}","[":"]"}
    open = ("{","(","[")
    close = (")","}","]")
    if string.count("(") != string.count(")") or string.count("{") != string.count("}") or string.count("[") != string.count("]"):
        return False
    else:
        for ch in range(len(string) - 1 ):
            if string[ch] in open:
                if string[ch + 1] == pair[string[ch]] or string[ch + 1] in open:
                    pass
                else:
                    return False
        return True
    
"""

"""
version Two

def valid_braces(string):
    pair = {"(":")","{":"}","[":"]"}
    open = ("{","(","[")
    close = (")","}","]")
    if string.count("(") != string.count(")") or string.count("{") != string.count("}") or string.count("[") != string.count("]"):
        return False
    else:
        for ch in range(len(string) - 1 ):
            if string[ch] in open:
                if string[ch + 1] == pair[string[ch]] or string[ch + 1] in open:
                    pass
                else:
                    return False
            elif string[ch] in close:
                if ch == 0:
                    return False
                elif string[ch -1] in close:
                    return False
        return True
    

"""

"""
version Three

def valid_braces(string):
    pair = {"(":")","{":"}","[":"]"}
    open = ("{","(","[")
    close = (")","}","]")
    if string.count("(") != string.count(")") or string.count("{") != string.count("}") or string.count("[") != string.count("]"):
        return False
    else:
        for ch in range(len(string) - 1 ):
            if string[ch] in open:
                if string[ch + 1] == pair[string[ch]] or string[ch + 1] in open:
                    pass
                else:
                    return False
            elif string[ch] in close:
                if ch == 0:
                    return False
                else:
                    split = string[0:ch + 1]
                    keys = list(pair.keys())
                    values = list(pair.values())
                    key_name = keys[values.index(string[ch])]
                    if split.count(key_name) != split.count(string[ch]):
                                  return False
        return True
    

"""
