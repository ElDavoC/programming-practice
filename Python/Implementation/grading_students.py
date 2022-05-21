def gradingStudents(grades):
    # Write your code here
    return [i if i < 38 or round(i / 5) * 5 < i else round(i / 5) * 5 for i in grades]

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
