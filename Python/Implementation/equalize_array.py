from collections import Counter

def equalize_array(arr):
    ctr = Counter(arr)
    return sum([i[1] for i in ctr.most_common()[1:]])

# Other Solution
def equalizeArray(arr):
    return len(arr) - max([arr.count(i) for i in arr])

# The Best Solution
def equalizeArray(arr):
    return len(arr) - max(Counter(arr).values())

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().split()]
    result = equalize_array(arr)
    print(result)
