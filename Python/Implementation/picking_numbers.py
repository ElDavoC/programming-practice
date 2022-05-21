def subarr(s):
    st_s, max_len = list(set(s)), 0
    if len(st_s) == 1: return len(s)
    for i in range(len(st_s) - 2):
        if abs(st_s[i] - st_s[i + 1]) <= 1:
            len_s = s.count(st_s[i]) +  s.count(st_s[i + 1])
        else:
            len_s = s.count(st_s[i])

        if max_len < len_s: max_len = len_s

    return max_len

    Other Solution

def subarr(s):
    maximum = 0
    for i in s:
        c = s.count(i)
        d = s.count(i-1)
        c = c + d
        if c > maximum:
            maximum = c

    return maximum

def subarr(s):
    maximum = 0
    for i in list(set(s)):
        c = s.count(i)
        d = s.count(i - 1)
        c = c + d
        if c > maximum:
            maximum = c

    return maximum

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().strip().split()))

    result = subarr(s)

    print(result)
