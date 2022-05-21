def rec_array(A):
    if A[0] == sorted(A)[0] and len(A) == 3:
        return A

    if A[0] == sorted(A)[0]:
        return A[0:1] + rec_array(A[1:])
    else:
        next = sorted(A)[0]
        next_pos = A.index(next)
        if next_pos == len(A) - 1:
            prov = A[-3:]
        else:
            prov = A[next_pos - 1: next_pos + 2]

        if prov[1] == next:
            prov = [next] + prov[2:] + prov[0:1]
        elif prov[2] == next:
            prov = [next] + prov[0:2]

        if next_pos == len(A) - 1:
            A = A[:-3] + prov
        else:
            A = A[0:next_pos - 1] + prov + A[next_pos + 2:]

        return rec_array(A)

def larrysArrays(A):
    return 'YES' if sorted(A) == rec_array(A) else 'NO'

def larrysArrays2(A):
    inversions = 0
    for i in range(len(A)):
        if sorted(A)[i] < A[i]:
            print(i)
            resta = A.index(sorted(A)[i]) - i
            print(resta)
            inversions = inversions + resta if resta > 0 else inversions
            print(inversions)

    return 'YES' if inversions % 2 == 0 else 'NO'

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        A = list(map(int, input().strip().split()))
        result = larrysArrays2(A)
        print(result)
