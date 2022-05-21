def grid_search(G, P, C, c):
    for i in range(len(G)):
        if len(G) - i < len(P): return 'NO'
        for j in range(C):
            if C - j < c: break
            if G[i][j:c + j] == P[0] and all([G[i + k][j:c + j] == P[k] for k in range(len(P))]):
                return 'YES'

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        R, C = map(int, input().strip().split())
        G = [input().strip() for _ in range(R)]
        r, c = map(int, input().strip().split())
        P = [input().strip() for _ in range(r)]
        result = grid_search(G, P, C, c)
        print(result)
