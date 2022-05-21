def camelcase(s):
    return sum([i.isupper() for i in s]) + 1


if __name__ == '__main__':
    s = input().strip()
    result = camelcase(s)
    print(result)
