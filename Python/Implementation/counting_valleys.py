def counting_valleys(steps, path):
    valleys = level = 0
    for letter in path:
        if letter == 'U':
            level += 1
        else:
            if level == 0: valleys += 1
            level -= 1

    # Compactly
    level = valleys = 0
    for step in s:
        level += 1 if step == "U" else -1
        valleys += level == 0 and step == "U"

    return valleys

if __name__ == '__main__':
    steps, path = int(input().strip()), input().strip()
    result = counting_valleys(steps, path)
    print(result)
