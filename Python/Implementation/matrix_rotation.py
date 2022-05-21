def matrix_rotation(matrix, r):
    final = []
    for i in range(len(matrix) // 2):
        prov = []
        prov_2 = []
        for j in range(i, len(matrix) - i):
            if i == j:
                prov += matrix[j][j:len(matrix) - i]
            elif j > i and j < len(matrix) - i - 1:
                prov += matrix[j][-1:]
                prov_2 += matrix[j][:1]
            else:
                prov += matrix[j][i:len(matrix) - i][::-1]
                prov += prov_2[::-1]

        final += [prov]

    for i in range(len(final)):
        param = r % len(final[i])
        final[i] = final[i][param:] + final[i][:param]

    prov = [[] for _ in range(len(matrix))]
    for i in range(len(matrix) // 2):
        rango = (len(final[i]) - (len(matrix[0]) - (2 * i))) // 2
        if i > 0 : rango += 2
        for j in range(i, rango):
            if i == j:
                prov[j] = prov[i][::2] + final[i][:len(matrix[0]) - 2 * i] + prov[i][1::2]
                del final[i][:len(matrix[0]) - 2 * i]
            elif i == 0 and j == rango - 1:
                prov[-1] = final[0][rango - 2:rango + len(matrix[0]) - 2][::-1]
            elif j > i and j <= rango:
                m = j - i
                prov[j] = prov[j][::2] + [final[i][-m]] + [final[i][m - 1]] + prov[j][1::2]

    return prov

if __name__ == '__main__':
    m, n, r = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(m)]
    result = matrix_rotation(matrix, r)
    [print(*i) for i in result]
