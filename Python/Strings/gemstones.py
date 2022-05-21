def gems(arr):
    c = [set(i) for i in arr]
    return len(tuple(set(''.join(arr)).intersection(*c)))

def main():
    arr = [input().strip() for _ in range(int(input().strip()))]
    result = gems(arr)
    print(result)

if __name__ == '__main__':
    main()
