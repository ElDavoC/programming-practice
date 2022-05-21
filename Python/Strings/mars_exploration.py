def mars_exploration(s):
    return sum(s[i] != 'SOS'[i % 3] for i in range(len(s)))

if __name__ == '__main__':
    s = input().strip()
    result = mars_exploration(s)
    print(result)
