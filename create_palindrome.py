"""
def solve(st):
    half_point = len(st)//2 
    first_half = st[0:half_point-1]
    second_half = st[half_point:]
    if st == st[::-1]:
        return True
    elif abs(ord(st[0]) - ord(st[-1])) <=2 and abs(ord(st[half_point-1]) - ord(st[half_point])) <=2:
        return True
    else:
        return False

"""
def solve(st):
    if len(st) == 2 and abs(ord(st[0]) - ord(st[1])) == 1:
        return False
    elif len(st) % 2 == 1:
        half_point = len(st)//2 
        if abs(ord(st[half_point]) - ord(st[half_point-1])) == 1 and abs(ord(st[half_point]) - ord(st[half_point+1])) == 1:
            first_half = st[0:half_point]
            second_half = st[half_point+1:]
            st = first_half + second_half
            return _solve_helper(st)
        else:
            return False
    else:
        return _solve_helper(st)
def _solve_helper(st):
    half_point = len(st)//2 
    first_half = st[0:half_point]
    second_half = st[half_point:]
    while len(st) > 0:
        if abs(ord(st[0]) - ord(st[-1])) <=2 and abs(ord(st[half_point-1]) - ord(st[half_point])) <=2:
            st = first_half[1:-1:] + second_half[1:-1:]
            return _solve_helper(st)
        else:
            return False
    return True