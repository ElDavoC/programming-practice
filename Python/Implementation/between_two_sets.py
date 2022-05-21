def getTotalX(a, b):
    # Write your code here
    a, b, i = sorted(a), sorted(b), 0
    for j in range(a[-1], b[0] + 1):
        if not all([j % i == 0 for i in a]): continue
        if not all([i % j == 0 for i in b]): continue
        i += 1

    return i

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
