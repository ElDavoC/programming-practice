def separetaNumbers(s):
    for i in range(1, len(s)//2 + 1):
        n = int(s[:i])
        if ''.join(map(str, [n + j for j in range(len(s)//i)]))[:len(s)] == s:
            return "YES " + str(n)

    return "NO"

def main():
    for _ in range(int(input().strip())):
        s = input()
        result = separetaNumbers(s)
        print(result)

if __name__ == '__main__':
    main()
