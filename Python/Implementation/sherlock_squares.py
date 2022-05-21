import math

def squares(s, e):
    total = 0
    if (s ** 0.5).is_integer(): total += 1
    total += math.floor(e ** 0.5) - math.floor(s ** 0.5)

    return total

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s, e = [int(i) for i in input().strip().split()]
        result = squares(s, e)
        print(result)
