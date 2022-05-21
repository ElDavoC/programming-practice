def condition(x):
    b = pow(x, 2, 100)
    a = (x ** 2 - b) // 100

    if b >= 0 and b < 10: b = '0' + str(b)

    ab = str(a) + str(b)

    return int(ab[:len(ab) - len(str(x))]) + int(ab[len(ab) - len(str(x)):]) == x

def kaprekarNumbers(p, q):
    return list(filter(condition, range(p, q + 1)))


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())

    result = kaprekarNumbers(p, q)
    print(*result if len(result) != 0 else ['INVALID', 'RANGE'], sep = ' ')
