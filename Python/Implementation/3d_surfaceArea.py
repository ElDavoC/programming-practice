def surface_area(A):
    total = len(A) * len(A[0]) * 2 + sum(A[0]) + sum(A[-1])
    for i in A:
        total += i[0] + i[-1]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if i < len(A) - 1:
                total += abs(A[i][j] - A[i + 1][j])

            if j < len(A[i]) - 1:
                total += abs(A[i][j] - A[i][j + 1])

    # for i in range(len(A)):
    #     total += (max(A[i]) - A[i][0]) + (max(A[i]) - A[i][-1])
    #
    # for j in range(len(A[0])):
    #     total += (max([A[k][j] for k in range(len(A))]) - A[0][j]) + (max([A[k][j] for k in range(len(A))]) - A[-1][j])

    return total



if __name__ == '__main__':
    H, W = map(int, input().strip().split())
    A = [[int(i) for i in input().strip().split()] for _ in range(H)]
    result = surface_area(A)
    print(result)
