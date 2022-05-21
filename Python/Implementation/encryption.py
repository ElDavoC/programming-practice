import math

def encryption(s):
    r, c = math.floor(len(s) ** 0.5), math.ceil(len(s) ** 0.5)
    m = [list(s[i:i + c]) for i in range(0, len(s), c)]
    if len(m[-1]) < c:
        m[-1] += ' ' * (c - len(m[-1]))

    return ' '.join([''.join(i).strip() for i in zip(*m)])


if __name__ == '__main__':
    #s = ''.join(input().strip().split())
    #result = encryption(s)
    #print(result)


    # Better solution

    s = input()
    sm = s.replace(" ", "")
    r = math.floor(math.sqrt(len(sm)))
    c = math.ceil(math.sqrt(len(sm)))
    for i in range(c):
        print(sm[i::c], end = " ")
