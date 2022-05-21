def find_digit(n):
    return len(list(filter(lambda x: int(x) != 0 and int(n) % int(x) == 0, n)))

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = input().strip()
        result = find_digit(n)
        print(result)
