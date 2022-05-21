class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Coordinates(x, y)

    def __repr__(self):
        return f'Coordinates({self.x},{self.y})'

    def __str__(self):
        return f'({self.x},{self.y})'

def queens_attack(n, k, queen, obs):
    h1, h2 = queen.y - 1, n - queen.y
    v1, v2 = queen.x - 1, n - queen.x
    d1 = n - queen.x if n - queen.x < n - queen.y else n - queen.y
    d2 = n - queen.x if n - queen.x < queen.y - 1 else queen.y - 1
    d3 = queen.x - 1 if queen.x - 1 < queen.y - 1 else queen.y - 1
    d4 = queen.x - 1 if queen.x - 1 < n - queen.y else n - queen.y
    for i in obs:
        prov = i - queen
        if prov.x == 0:
            if prov.y < 0 and h1 > abs(prov.y) - 1:
                h1 = abs(prov.y) - 1
            elif prov.y > 0 and h2 > prov.y - 1:
                h2 = prov.y - 1
        elif prov.y == 0:
            if prov.x < 0 and v1 > abs(prov.x) - 1:
                v1 = abs(prov.x) - 1
            elif prov.x > 0 and v2 > prov.x - 1:
                v2 = prov.x - 1
        elif prov.x > 0 and prov.x == prov.y and prov.x - 1 < d1:
            d1 = prov.x - 1
        elif prov.x > 0 and prov.x == -prov.y and prov.x - 1 < d2:
            d2 = prov.x - 1
        elif prov.x < 0 and prov.x == prov.y and abs(prov.x) - 1 < d3:
            d3 = abs(prov.x) - 1
        elif prov.x < 0 and prov.x == -prov.y and abs(prov.x) - 1 < d4:
            d4 = abs(prov.x) - 1

        # print(i)

    return sum([h1, h2, v1, v2, d1, d2, d3, d4])



if __name__ == '__main__':
    n, k = map(int, input().split())
    queen = Coordinates(*list(map(int, input().split())))
    obs = [Coordinates(*list(map(int, input().strip().split()))) for _ in range(k)]
    result = queens_attack(n, k, queen, obs)
    print(result)
