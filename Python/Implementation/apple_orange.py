def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_apples = sum([(1 if a + i >= s and a + i <= t else 0) for i in apples])
    count_oranges = sum([(1 if b + i >= s and b + i <= t else 0) for i in oranges])
    print(count_apples, count_oranges, sep = '\n')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
