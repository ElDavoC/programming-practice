def theLoveLetterMystery(s):
    return sum(map(lambda x: abs(ord(s[x]) - ord(s[-(x + 1)])), range(len(s) // 2)))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s = input()
        result = theLoveLetterMystery(s)
        print(result)
