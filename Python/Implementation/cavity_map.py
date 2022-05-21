def cond_x(grid, i, j):
    return grid[i + 1][j] == 'X' or grid[i - 1][j] == 'X' or grid[i][j + 1] == 'X' or grid[i][j - 1] == 'X'

def cond_max(grid, i, j):
    return all((grid[i][j] > grid[i + 1][j], grid[i][j] > grid[i - 1][j], grid[i][j] > grid[i][j + 1], grid[i][j] > grid[i][j - 1]))

def cavityMap(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            # if cond_x(grid, i, j): continue
            if cond_max(grid, i, j): grid[i][j] = 'X'

    return [''.join(i) for i in grid]


if __name__ == '__main__':
    grid = [list(input().strip()) for _ in range(int(input().strip()))]
    result = cavityMap(grid)
    print(*result, sep = '\n')
