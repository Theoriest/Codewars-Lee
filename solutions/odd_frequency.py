def find_it(seq):
    count = {}
    unique = set(seq)
    unique = list(unique)
    for n in unique:
        repeated = seq.count(n)
        count[n] = repeated
    for key in count:
        if count[key] % 2 == 1:
            return key
        elif count[key] % 2 == 0:
            pass
        else:
            return 0


