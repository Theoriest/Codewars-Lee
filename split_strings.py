test = ["asdfadsf","asdfads","","x"]


def solution(s):
    result = []
    if len(s) % 2 == 0:
        s = s
    else:
        s += "_"
    for n in range(0,len(s),2):
        sub = s[n] + s[n + 1]
        result.append(sub)

    return result

for t in test:
    print(solution(t))

