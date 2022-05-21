from collections import Counter

def bird_id(arr):
    bird_count = Counter(sorted(arr))
    return bird_count.most_common()[0][0]

if __name__ == '__main__':
    n = input().strip()
    arr = list(map(int, input().strip().split()))
    result = bird_id(arr)
    print(result)
