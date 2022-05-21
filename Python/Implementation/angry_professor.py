def angry_prof(k, students):
    # on_time = list(filter(lambda x: x <= 0, students))
    # return 'YES' if len(on_time) < k else 'NO'

    on_time = sorted(students)
    return 'YES' if on_time[k - 1] > 0 else 'NO'



if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().strip().split())
        students = map(int, input().strip().split())
        result = angry_prof(k, students)
        print(result)
