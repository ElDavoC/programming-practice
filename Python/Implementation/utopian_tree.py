def u_tree(cicles):
    x = 1
    for i in range(1, round((cicles / 2) + 0.1) + 1):
        x *= 2
        if cicles == i * 2 - 1: return x
        x += 1
        if cicles == i * 2: return x

    #return x
    return ~(~1<<(cicles>>1)) << cicles%2;

if __name__ == '__main__':
    for _ in range(int(input())):
        cicles = int(input())
        result = u_tree(cicles)
        print(result)
