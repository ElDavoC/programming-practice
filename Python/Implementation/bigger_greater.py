def bigger_greater(w):
    i = -1
    while i >= -len(w):
        #print(''.join(sorted(w[i:], reverse = True)))
        if w[i:] == ''.join(sorted(w[i:], reverse = True)):
            i -= 1
        else:
            break

    if i < -len(w):
        return 'no answer'
    else:
        pre, suff = list(w[:i + 1]), list(w[i + 1:])
        suff_set = sorted(set(w[i + 1:]))
        for j in suff_set:
            if j > pre[-1]:
                change = j
                break
        
        pre[-1], suff[suff.index(change)] = change, w[i]
        return ''.join(pre + sorted(suff))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        w = input().strip()
        result = bigger_greater(w)
        print(result)

    # Solution

    # for _ in range(int(input())):
    #     w = input().strip()
    #     n = len(w) + 1
    #     for k in range(-2, -n, -1):                                 # So I read the word w from right to left,
    #         if w[k] < w[k + 1]:                                     # searching for the first letter w[k] smaller than the previous (from right).
    #             print(w[:k],end='')                                 # Then I leave the left part of the word unchanged, and print it.
    #             v = w[:k:-1]                                        # The right part is to be rearranged - inversed first of all - to give the smallest possible.
    #             for j in range(-k - 1):                             # Then I look for the right place there to insert w[k] which has been found earlier.
    #                 if w[k] < v[j]:                                 # Right place means the leftmost letter v[j] of the inversed right part v, which is greater than w[k].
    #                     print(v[j] + v[:j] + w[k] + v[j + 1:])      # Inversion of w[k] and v[j] completes the rearrangement of the right part,
    #                     break                                       # so I print it and leave.
    #                 else:                                           # If only one (the rightmost) letter of the inversed right part v is greater than w[k], its inversion with w[k]
    #                     print(v + w[k])                             # means just placing w[k] after the v.
    #                 break
    #         else:                                                   # If no letter of the initial word w is smaller than the previous from right, i.e. the letters are decreasing in the word,
    #             print('no answer')                                  # than no rearrangement gives a lexicographically greater.
