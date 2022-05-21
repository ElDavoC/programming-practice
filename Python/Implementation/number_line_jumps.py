def kangaroo(x1, v1, x2, v2):
    # Write your code here
    while True:
        if (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1) or ((x1 > x2 or x1 < x2) and v1 == v2):
            return 'NO'
        elif x1 == x2:
            return 'YES'
        else:
            x1 += v1
            x2 += v2

    # Better solution
    if (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1) or ((x1 > x2 or x2 > x1) and v1 == v2): return 'NO'
    if (x1 - x2) % (v2 - v1) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
