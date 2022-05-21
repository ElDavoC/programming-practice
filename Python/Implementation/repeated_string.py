import math

def repeated_strings(s, n):
    if not 'a' in s:
        return 0
    elif len(s) == s.count('a'):
        return n

    num_a = math.floor(n / len(s)) * s.count('a') + s[:n % len(s)].count('a')
    return num_a

if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())
    result = repeated_strings(s, n)
    print(result)
