def pangram(s):
    return 'pangram' if len(set(s.lower())) == 27 else 'not pangram'

if __name__ == '__main__':
    s = input().strip()
    result = pangram(s)
    print(result)
