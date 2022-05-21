def pages(n, p):
    #if n // 2 >= p:
    #    return p // 2
    #else:
    #    return n // 2 - p // 2

    return (p // 2) if (n // 2) >= p else (n // 2) - (p // 2)


if __name__ == '__main__':
    n, p = int(input().strip()), int(input().strip())
    result = pages(n, p)
    print(result)
