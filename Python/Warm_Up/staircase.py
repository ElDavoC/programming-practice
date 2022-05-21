def staircase(n):
    # Write your code here
    [print(('#' * i).rjust(n)) for i in range(1, n + 1)]

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
