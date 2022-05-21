import math

def viral(n):
    l = 2
    total = l
    for _ in range(1, n):
        l = math.floor(l * 3 / 2)
        total += l

    return total


# Intento recursivo.
# def viral(n):
#     if n == 1:
#         return 2
#     else:
#         return math.floor(viral(n - 1) * 3 / 2) + viral(n - 1)

if __name__ == '__main__':
    n = int(input())
    result = viral(n)
    print(result)

    # Other option
    m = [2]
    for i in range(int(input()) -1):
        m.append(int(3 * m[i] / 2))
        
    print(sum(m))
