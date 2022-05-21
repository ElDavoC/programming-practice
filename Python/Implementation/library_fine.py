def library_fine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    elif d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
    else:
        return 0

if __name__ == '__main__':
    d1, m1, y1 = [int(i) for i in input().strip().split()]
    d2, m2, y2 = [int(i) for i in input().strip().split()]
    result = library_fine(d1, m1, y1, d2, m2, y2)
    print(result)
