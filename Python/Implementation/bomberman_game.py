def conversion(grid):
    final = [list('O' * (len(grid[0]) + 2)) for _ in range(len(grid) + 2)]
    for i in range(len(grid)):
        if 'O' in grid[i]:
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    final[i + 1][j] = final[i + 1][j + 1] = final[i + 1][j + 2] = final[i][j + 1] = final[i + 2][j + 1] = '.'

    return [''.join(final[i][1:-1]) for i in range(1, len(final) - 1)]

def bomberMan(n, grid):
    if n == 0 or n == 1: return '\n'.join(grid)

    if n % 4 == 0 or n % 4 == 2:
        return '\n'.join([i.replace('.','O') for i in grid])
    elif n % 4 == 3:
        return '\n'.join(conversion(grid))
    elif n % 4 == 1:
        return  '\n'.join(conversion(conversion(grid)))


if __name__ == '__main__':
    r, c, n = map(int, input().strip().split())
    grid = [input().strip() for _ in range(r)]
    result = bomberMan(n, grid)
    print(result)
