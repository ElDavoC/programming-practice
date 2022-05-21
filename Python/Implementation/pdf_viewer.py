def pdf_viewer(height, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    max_hgt = max([height[letters.index(i)] for i in set(word)])
    return max_hgt * len(word)

if __name__ == '__main__':
    height = [int(i) for i in input().strip().split()]
    word = input().strip()
    result = pdf_viewer(height, word)
    print(result)

    # better solution
    word = [height[ord(c) - ord('a')] for c in input()]
    print(max(word)*len(word))
