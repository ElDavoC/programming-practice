def sequance(n, p):
    # final = []
    # for i in range(1, n + 1):
    #     final.append(p.index(p.index(i) + 1) + 1)
    #
    # return final

    return [p.index(p.index(i) + 1) + 1 for i in range(1, n + 1)]

if __name__ == '__main__':
    n = int(input().strip())
    p = [int(i) for i in input().strip().split()]
    result = sequance(n, p)
    print(*result, sep = '\n')
