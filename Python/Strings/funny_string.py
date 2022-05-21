def funnyString(s):
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[-(i + 1)]) - ord(s[-(i + 2)])):
            return 'Not Funny'

    return 'Funny' 

def main():
    for _ in range(int(input().strip())):
        s = input().strip()
        result = funnyString(s)
        print(result)

if __name__ == '__main__':
    main()
