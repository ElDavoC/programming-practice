import math

def howManyGames(p, d, m, s):
    if p > s:
        return 0
    elif p == s:
        return 1

    total = 0

    while s >= p:
        total += 1
        s -= p
        p = max(p - d, m)

    return total

# Better Solution
def howManyGames(p, d, m, s):
    kmax = ((p-m) // d)
    fmax = (kmax+1)*p-((kmax+1)*kmax*d) / 2

    if (s >= fmax):
        return int(kmax+1 + (s-fmax)/m)
    else:
        b = p*1.0/d - 0.5
        g = b - ((b*b-2/d*(s-p))**0.5)
        return int(math.ceil(g))



if __name__ == '__main__':
    p, d, m, s = map(int, input().strip().split())
    # result = howManyGames(p, d, m, s)
    result = many_games(p, d, m, s)
    print(result)
