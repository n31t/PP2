n = int(input())
students = [tuple(map(int, input().split())) for _ in range(n)]

q = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(q)]

country = []
for test_case in test_cases:
    for j, student in enumerate(students):
        if student[2] == 1 and j + 1 == test_case[2]:
            country.append(str(j + 1))
            break
        elif test_case[1] >= student[1] and test_case[0] >= student[0]:
            country.append(str(j + 1))
            break
    else:
        country.append('0')

print(' '.join(country))
