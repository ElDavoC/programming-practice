def breakingRecords(scores):
    # Write your code here
    min, max, n_min, n_max = None, None, 0, 0
    for i in scores:
        if min is None and max is None:
            min, max = i, i
        elif i > max:
            max = i
            n_max += 1
        elif i < min:
            min = i
            n_min += 1

    return n_max, n_min

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
