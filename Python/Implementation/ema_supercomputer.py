import copy

def calc(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 0:
                for k in range(i, -1, -1):
                    if grid[k][j] == -1:
                        top = i - k - 1
                        break
                    elif k == 0:
                        top = i

                for k in range(i, len(grid)):
                    if grid[k][j] == -1:
                        bot = k - i - 1
                        break
                    elif k == len(grid) - 1:
                        bot = k - i

                for k in range(j, -1, -1):
                    if grid[i][k] == -1:
                        left = j - k -1
                        break
                    elif k == 0:
                        left = j

                for k in range(j, len(grid[i])):
                    if grid[i][k] == -1:
                        right = k - j - 1
                        break
                    elif k == len(grid[i]) - 1:
                        right = k - j

                grid[i][j] = min([top, bot, left, right])

    return grid


def twoPluses(grid):
    grid = [[-1 if i[j] == 'B' else 0 for j in range(len(i))] for i in grid]
    perm = copy.deepcopy(grid)
    grid = calc(grid)
    areas = [0]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] > 0:
                prov_areas = []
                value = grid[i][j]
                while value > 0:
                    prov = copy.deepcopy(perm)
                    for k in range(i - value, i + value + 1):
                        prov[k][j] = -1
                    for k in range(j - value, j + value + 1):
                        prov[i][k] = -1

                    prov = calc(prov)
                    prov_area = ((value * 4) + 1) * (max([max(i) for i in prov]) * 4 + 1)
                    prov_areas.append(prov_area)
                    value -= 1

                areas.append(max(prov_areas))

    if len(areas) == 1 and sum([i.count(0) for i in grid]) >= 2: return 1
    return max(areas)




if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    grid = [list(input().strip()) for _ in range(n)]
    result = twoPluses(grid)
    print(result)
